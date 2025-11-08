#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os, csv, pyodbc, datetime, cgi, cgitb

cgitb.enable()
print("Content-type: text/html\n\n")

# === CONFIG ===
LOG_DIR = os.path.join(os.path.dirname(__file__), '..', 'logs')
LOG_DIR = os.path.abspath(LOG_DIR)

DB_CONN_STR = (
        'DRIVER={SQL Server};'
        'SERVER=yourServerName;'
        'DATABASE=yourDatabaseName;'
        'Trusted_Connection=yes;'
)

# === Connect to DB ===
def connect_db():
    return pyodbc.connect(DB_CONN_STR)

# === Process CSV Logs ===
def process_logs():
    files = [f for f in os.listdir(LOG_DIR) if f.lower().endswith(".csv")]
    if not files:
        return

    conn = connect_db()
    cursor = conn.cursor()

    for filename in files:
        file_path = os.path.join(LOG_DIR, filename)
        try:
            customer_id = int(filename.split("_")[0])
        except:
            customer_id = 1

        arp_tracker = {}
        syn_tracker = {}

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                proto = row.get("Protocol", "").upper()
                info = row.get("Info", "")
                src_ip = row.get("Source", "")
                dst_ip = row.get("Destination", "")
                src_mac = row.get("Source MAC", "")
                dst_port = row.get("Destination Port", "")
                timestamp = row.get("Date", "") or row.get("Time", "")

                # --- Detect ARP Poisoning ---
                if proto == "ARP" and src_mac:
                    if src_mac not in arp_tracker:
                        arp_tracker[src_mac] = set()
                    if "who has" in info.lower():
                        advertised_ip = info.split("who has")[-1].strip().split()[0]
                        arp_tracker[src_mac].add(advertised_ip)

                # --- Detect SYN Flood ---
                if "[SYN]" in info and src_ip == dst_ip:
                    port = dst_port if dst_port else "Unknown"
                    key = (port, timestamp)
                    syn_tracker[key] = syn_tracker.get(key, 0) + 1

        # --- Save ARP Poisoning Attacks ---
        for mac, ips in arp_tracker.items():
            if len(ips) > 1:
                cursor.execute("""
                    INSERT INTO Incidents (CustomerID, Date, Protocol, SourceMAC, Info, AttackType)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    customer_id,
                    datetime.datetime.now(),
                    "ARP",
                    mac,
                    f"{len(ips)} IPs advertised",
                    "ARP Poisoning"
                ))

        # --- Save SYN Flood Attacks ---
        for (port, date), count in syn_tracker.items():
            cursor.execute("""
                INSERT INTO Incidents (CustomerID, Date, Protocol, DestinationPort, Info, AttackType)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                customer_id,
                date or datetime.datetime.now(),
                "TCP",
                port,
                f"{count} SYN packets",
                "SYN Flood"
            ))

        conn.commit()
        # Rename file to .old
        new_name = filename.replace(".csv", f"_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.old")
        os.rename(file_path, os.path.join(LOG_DIR, new_name))

    cursor.close()
    conn.close()

# === Show Incidents for a Customer ===
def show_incidents(username):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT CustomerID FROM Customers WHERE Username=?", (username,))
    result = cursor.fetchone()
    if not result:
        print("<p>No customer record found.</p>")
        return
    cust_id = result[0]

    cursor.execute("""
        SELECT AttackType, Protocol, Info, Date
        FROM Incidents
        WHERE CustomerID=?
        ORDER BY Date DESC
    """, (cust_id,))
    incidents = cursor.fetchall()
    cursor.close()
    conn.close()

    if not incidents:
        print("<p>No detected attacks for your company.</p>")
        return

    print("""
    <h2>Detected Attacks</h2>
    <table border='1' style='width:100%; border-collapse:collapse; text-align:center;'>
        <tr style='background-color:#333; color:#f1c40f;'>
            <th>Attack Type</th>
            <th>Protocol</th>
            <th>Info</th>
            <th>Date</th>
        </tr>
    """)

    for atk in incidents:
        print(f"""
        <tr>
            <td>{atk[0]}</td>
            <td>{atk[1]}</td>
            <td>{atk[2]}</td>
            <td>{atk[3]}</td>
        </tr>
        """)

    print("</table>")

# === MAIN ===
form = cgi.FieldStorage()
user = form.getvalue("user")

process_logs()

print("<html><body class='login-card'>")
if user:
    show_incidents(user)
    print("<br><a href='/cgi-bin/login.py'>Return to Application</a>")
else:
    print("<h3>Error: No user specified.</h3>")
print("</body></html>")
