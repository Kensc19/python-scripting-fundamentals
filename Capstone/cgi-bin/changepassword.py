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

# --- Database connection helper ---
def connect_db():
    return pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=yourServerName;'
        'DATABASE=yourDatabaseName;'
        'Trusted_Connection=yes;'
    )

# --- Read form data ---
form = cgi.FieldStorage()
username = form.getvalue("user")
role = form.getvalue("role")  # "employee" or "customer"
current_password = form.getvalue("current_password")
new_password = form.getvalue("new_password")
confirm_password = form.getvalue("confirm_password")

# --- Function to show the form ---
def show_form(message=""):
    print(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Change Password</title>
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
            input[type=password] {{
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
    <div class="login-card">
        <h2>Change Password</h2>
        <p style='color:red;'>{message}</p>
        <form method='post' action='/cgi-bin/changepassword.py'>
            <input type='hidden' name='user' value='{username}'>
            <input type='hidden' name='role' value='{role}'>
            
            <label>Current Password:</label><br>
            <input type='password' name='current_password' required><br><br>
            
            <label>New Password:</label><br>
            <input type='password' name='new_password' required><br><br>
            
            <label>Confirm New Password:</label><br>
            <input type='password' name='confirm_password' required><br><br>
            
            <input type='submit' value='Change Password'>
        </form>
        <a href='/cgi-bin/login.py'>Return to Application</a>
    </div>
    </body>
    </html>
    """)

# --- If no input, show form ---
if not current_password:
    show_form()
else:
    try:
        conn = connect_db()
        cursor = conn.cursor()
        table = "Employees" if role == "employee" else "Customers"

        # Verify current password
        cursor.execute(f"SELECT * FROM dbo.{table} WHERE Username=? AND Password=?", (username, current_password))
        user = cursor.fetchone()

        if not user:
            show_form(" Incorrect current password.")
        elif new_password != confirm_password:
            show_form(" New passwords do not match.")
        else:
            cursor.execute(f"UPDATE dbo.{table} SET Password=? WHERE Username=?", (new_password, username))
            conn.commit()
            print(f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Password Changed</title>
                <link rel="stylesheet" href="/styles.css">
            </head>
            <body>
            <div class="login-card">
                <h2> Password successfully changed!</h2>
                <a href='/cgi-bin/login.py'>Return to Application</a>
            </div>
            </body>
            </html>
            """)
    except Exception as e:
        print(f"<h3>Error: {e}</h3>")
    finally:
        cursor.close()
        conn.close()
