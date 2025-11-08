#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pyodbc, cgi, cgitb, sys, os
cgitb.enable()

# Ensure UTF-8 output for web
os.environ['PYTHONIOENCODING'] = 'utf-8'
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

print("Content-type: text/html\n\n")

# --- Database Connection ---
def connect_db():
    return pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=yourServerName;'
        'DATABASE=yourDatabaseName;'
        'Trusted_Connection=yes;'
    )

# --- Get Form Data ---
form = cgi.FieldStorage()
username = form.getvalue("user")
name = form.getvalue("name")
company = form.getvalue("company")
email = form.getvalue("email")
phone = form.getvalue("phone")

# --- Function to Display Form ---
def show_form(msg=""):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT Name, Company, Email, Phone FROM dbo.Customers WHERE Username=?", (username,))
        data = cursor.fetchone()
        cursor.close()
        conn.close()

        if not data:
            print("""
            <html><body class='login-card'>
            <h3>User not found.</h3>
            <a href='/login.html'>Return to login</a>
            </body></html>
            """)
            return

        print(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Update Contact Information</title>
            <link rel="stylesheet" href="/styles.css">
            <style>
                .login-card {{
                    background-color: #1a1a1a;
                    color: #f1f1f1;
                    max-width: 500px;
                    margin: 80px auto;
                    padding: 40px;
                    border-radius: 15px;
                    box-shadow: 0 0 20px rgba(241, 196, 15, 0.3);
                    border: 2px solid #f1c40f;
                    text-align: center;
                }}
                input[type=text], input[type=email] {{
                    width: 100%;
                    padding: 10px;
                    margin: 8px 0;
                    border: 1px solid #555;
                    background-color: #333;
                    color: #f1f1f1;
                    border-radius: 5px;
                    box-sizing: border-box;
                }}
                input[type=submit] {{
                    background-color: #f1c40f;
                    color: #000;
                    border: none;
                    border-radius: 6px;
                    padding: 10px 20px;
                    font-weight: bold;
                    cursor: pointer;
                    transition: 0.3s ease;
                }}
                input[type=submit]:hover {{
                    background-color: #e0b40e;
                }}
                a {{
                    display: inline-block;
                    margin-top: 15px;
                    color: #f1c40f;
                    text-decoration: none;
                }}
            </style>
        </head>
        <body>
        <div class='login-card'>
            <h2>Update Contact Information</h2>
            <p style='color:red;'>{msg}</p>
            <form method='post' action='/cgi-bin/updatecontact.py'>
                <input type='hidden' name='user' value='{username}'>
                <label>Name:</label><br>
                <input type='text' name='name' value='{data[0]}' required><br>
                <label>Company:</label><br>
                <input type='text' name='company' value='{data[1]}' required><br>
                <label>Email:</label><br>
                <input type='email' name='email' value='{data[2]}' required><br>
                <label>Phone:</label><br>
                <input type='text' name='phone' value='{data[3] or ""}'><br><br>
                <input type='submit' value='Update'>
            </form>
            <a href='/cgi-bin/login.py'>Return to Application</a>
        </div>
        </body>
        </html>
        """)
    except Exception as e:
        print(f"<h3>Error displaying form: {e}</h3>")

# --- If no POST data, show the form ---
if not name:
    show_form()
else:
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Customers 
            SET Name=?, Company=?, Email=?, Phone=? 
            WHERE Username=?;
        """, (name, company, email, phone, username))
        conn.commit()
        cursor.close()
        conn.close()

        print("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Contact Updated</title>
            <link rel="stylesheet" href="/styles.css">
        </head>
        <body>
        <div class='login-card'>
            <h2> Contact information updated successfully!</h2>
            <a href='/cgi-bin/login.py'>Return to Application</a>
        </div>
        </body>
        </html>
        """)
    except Exception as e:
        print(f"<h3>Error updating record: {e}</h3>")
# --- End of Script ---