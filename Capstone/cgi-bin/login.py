#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, os, cgi, pyodbc

# Ensure UTF-8 output for CGI
os.environ['PYTHONIOENCODING'] = 'utf-8'
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

print("Content-type: text/html\n\n")

# === HTML HEADER ===
print("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Login Result</title>
<link rel="stylesheet" href="/styles.css">
<style>
/* --- Fallback CSS if external styles.css fails to load --- */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #0d0d0d;
    color: #f1f1f1;
    margin: 0;
    padding: 0;
}
.login-card {
    background-color: #1a1a1a;
    color: #f1f1f1;
    max-width: 600px;
    margin: 100px auto;
    padding: 40px;
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(241, 196, 15, 0.3);
    text-align: center;
    border: 2px solid #f1c40f;
}
.login-card h1 {
    color: #f1c40f;
    text-shadow: 2px 2px 4px #000;
    font-size: 2em;
    margin-bottom: 10px;
}
.login-card h3 {
    color: #ff4d4d;
    font-weight: normal;
    margin-top: 0;
}
.login-card p {
    font-size: 1.1em;
    margin: 10px 0;
}
.login-card a {
    display: inline-block;
    margin-top: 15px;
    padding: 10px 20px;
    background-color: #f1c40f;
    color: #000;
    font-weight: bold;
    border-radius: 8px;
    text-decoration: none;
    transition: all 0.3s ease;
}
.login-card a:hover {
    background-color: #e0b40e;
    transform: scale(1.05);
}
</style>
</head>
<body>
<div class="login-card">
""")

# === Retrieve form data ===
form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")
is_employee = form.getvalue("employee")

if not username or not password:
    print("<h3> Error: Username and password are required.</h3>")
    print("<a href='/login.html'>Return to login</a>")
    print("</div></body></html>")
    raise SystemExit

# === Connect to SQL Server ===
try:
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=yourServerName;'
        'DATABASE=yourDatabaseName;'
        'Trusted_Connection=yes;'
    )
except Exception as e:
    print("<h3> Database connection error.</h3>")
    print(f"<pre>{e}</pre>")
    print("</div></body></html>")
    raise SystemExit

cursor = conn.cursor()

# === Query Employees and Customers ===
try:
    cursor.execute("SELECT * FROM Employees WHERE Username=? AND Password=?", (username, password))
    employee = cursor.fetchone()

    cursor.execute("SELECT * FROM Customers WHERE Username=? AND Password=?", (username, password))
    customer = cursor.fetchone()
except Exception as e:
    print("<h3>⚠️ Error querying tables:</h3>")
    print(f"<pre>{e}</pre>")
    cursor.close()
    conn.close()
    print("</div></body></html>")
    raise SystemExit

# === Check login conditions ===
if is_employee and not employee:
    print("<h3> You are not registered as an employee.</h3>")
    print("<a href='/login.html'>Return to login</a>")

elif not is_employee and not customer:
    print("<h3> Invalid customer credentials.</h3>")
    print("<a href='/login.html'>Return to login</a>")

elif is_employee and employee:
    # Expected columns: [0]=EmpID, [1]=FirstName, [2]=LastName, [3]=Position, [4]=Email, [5]=Username, [6]=Password
    first_name = employee[1]
    last_name = employee[2]
    position = employee[3]
    email = employee[4]
    username_db = employee[5]

    print(f"""
    <h1>Welcome, {first_name} {last_name}!</h1>
    <p><strong>Position:</strong> {position}</p>
    <p><strong>Email:</strong> {email}</p>
    <p><strong>Username:</strong> {username_db}</p>
    <a href='/cgi-bin/changepassword.py?user={username_db}&role=employee'>Change Password</a>
    """)

elif not is_employee and customer:
    # Expected columns: [0]=CustID, [1]=FirstName, [2]=LastName, [3]=Company, [4]=Email, [5]=Phone, [6]=Username, [7]=Password
    first_name = customer[1]
    last_name = customer[2]
    company = customer[3]
    email = customer[4]
    username_db = customer[6]

    print(f"""
    <h1>Welcome, {first_name} {last_name}!</h1>
    <p><strong>Company:</strong> {company}</p>
    <p><strong>Email:</strong> {email}</p>
    <p><strong>Username:</strong> {username_db}</p>
    <a href='/cgi-bin/changepassword.py?user={username_db}&role=customer'>Change Password</a>
    <a href='/cgi-bin/updatecontact.py?user={username_db}'>Update Contact Info</a>
    <a href='/cgi-bin/incidents.py?user={username_db}'>View Detected Attacks</a>
    """)

# === Close DB connection ===
cursor.close()
conn.close()

# === End of HTML ===
print("</div></body></html>")
