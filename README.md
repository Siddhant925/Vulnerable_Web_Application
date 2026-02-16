# Vulnerable Flask Blog Application

## 📌 Overview

This project is an intentionally vulnerable web application built using Flask and SQLite for educational purposes. 

The objective of this project is to demonstrate common web application security vulnerabilities in a controlled environment. The application simulates a simple blog system with user authentication and post management features.

⚠️ This application is intentionally insecure and should NOT be deployed in a production environment.

---

## 🚀 Features

- User Registration
- User Login & Session Management
- Create Posts
- View Posts
- User Profile Page

---

## 🔥 Implemented Vulnerabilities

### 1️⃣ SQL Injection
Authentication bypass by manipulating SQL queries in the login functionality.

### 2️⃣ Stored Cross-Site Scripting (XSS)
Malicious JavaScript code can be injected into posts and executed in other users' browsers.

### 3️⃣ Insecure Direct Object Reference (IDOR)
Users can access other users’ profile data by modifying the user ID in the URL.

### 4️⃣ Plaintext Password Storage
Passwords are stored directly in the database without hashing.

### 5️⃣ Cross-Site Request Forgery (CSRF)
The application does not implement CSRF protection for form submissions.

### 6️⃣ Debug Mode Enabled
Application runs with debug mode enabled, exposing internal error details.

---

## 🛠️ Technologies Used

- Python
- Flask
- SQLite
- HTML (Basic Templates)

---

## 🎯 Learning Objectives

This project was developed to:

- Understand how common web vulnerabilities work
- Learn how attackers exploit insecure coding practices
- Analyze the impact of insecure authentication and authorization
- Demonstrate secure coding improvements after identifying vulnerabilities

---

## ⚠️ Disclaimer

This project is strictly for academic and educational purposes. It is inspired by security awareness practices promoted by organizations like OWASP.

Do not deploy this application publicly.

---

## 👨‍💻 Author

Siddhant Gaikwad
