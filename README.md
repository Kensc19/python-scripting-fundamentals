
# 🐍 Python Scripting Fundamentals  
### Practical Exercises + Full Capstone Project  

This repository contains all the **Python exercises, mini-projects, and the final capstone project** developed during the **Akamai Python Scripting Fundamentals** program.  
It includes scripting essentials, input validation utilities, a word-guessing game, text-adventure logic, and a complete mini web application built with **Python CGI, HTML, CSS, and SQLite**.

---

## 📁 Project Structure

### 🔹 Practice Scripts  
Small independent Python scripts demonstrating core programming concepts:

| Script | Description |
|--------|--------------|
| `check_even.py` | Even/odd number checker |
| `connect-DB.py` | Basic database connection example |
| `count_vowels.py` | Counts vowels in a string |
| `Creating-Word-Guessing-Game.py` | Simple interactive guessing game |
| `lemonade.py` | Basic arithmetic exercise |
| `Testing-User-Input.py` | User input handling and validation |
| `text_adventure.py` | Console-based mini adventure |
| `using-modules.py` | Demonstrates importing and using modules |
| `validate_name.py` / `validate_number.py` | Input validation utilities |

These exercises reinforce Python fundamentals such as loops, functions, conditionals, file handling, and modular programming.

---

## 🎓 Capstone Project — Mini Web Application  

The `Capstone/` folder contains a fully functional web application built using **Python CGI**, **HTML**, and **SQLite**.

### 📌 Key Components

#### 🔸 CGI Scripts (`Capstone/cgi-bin/`)
- `login.py` — Simple login/authentication logic  
- `incidents.py` — Logs or displays incident information  
- `updatecontact.py` — Updates user contact details  
- `changepassword.py` — Password update handler  
- `createdatabase.sql` — SQL script for creating the SQLite database  

#### 🔸 Frontend (`Capstone/`)
- `index.html`, `login.html`, `contact.html`, `services.html`  
- `style.css`  
- `images/batcave.jpg`  

#### 🔸 Sample Log Files (`Capstone/logs/`)
- `1_synattack.csv`  
- `2_arppoison.csv`  

These log files are used by the incident-handling CGI scripts.

---

## 🚀 Running the Capstone Web Application

1. **Start a local CGI server**  
   From inside the `Capstone` folder, run:
   ```bash
   python -m http.server --cgi 8000

2. **Open in your browser**
   [http://localhost:8000/index.html](http://localhost:8000/index.html)

> Make sure your environment allows executing scripts inside the `cgi-bin/` directory.

---

## 🛠 Technologies Used

* Python 3.x
* CGI scripting
* HTML & CSS
* SQLite
* CSV processing

---

## 📈 Learning Objectives

This project demonstrates:

* Python scripting fundamentals
* Error handling and input validation
* Working with CSV and external files
* Interactive console programming
* Basic database creation with SQLite
* Building simple web applications using CGI
* Structuring a multi-component project

---

## 🔮 Future Improvements

* Convert the CGI project to **Flask** or **FastAPI**
* Add **unit tests** for all scripts
* Improve **UI/UX** with a modern frontend
* Add **advanced logging** and error handling
* Build **interactive dashboards** to analyze incident logs

---

## 📄 License

This project is intended for **educational purposes only**.

---
