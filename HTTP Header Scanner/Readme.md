# 🌐 HTTP Header Scanner

![Wallpaper Image](https://github.com/Jeewaka15/My-Projects---First-Phase/blob/bfc2bfe0cd8015a9ecd71577b4cda884abb5464c/HTTP%20Header%20Scanner/Project%20Wallpaper.png)

<br><br>

A Python and Flask-based HTTP Header Scanner built as part of my **Cybersecurity Foundations (Phase 01)** learning journey. This project analyzes HTTP response headers and evaluates whether a website follows security best practices by checking for missing or misconfigured security headers.

## 🚀 Overview

HTTP Header Scanner is a web security auditing tool that sends HTTP requests to a target website, retrieves its response headers, and evaluates the presence of important security headers. It provides a security score along with recommendations to improve the website's security posture.




![First Image](https://github.com/Jeewaka15/My-Projects---First-Phase/blob/ed79628800a66f2f587efcb29682a9eb36dabd4a/HTTP%20Header%20Scanner/HTTP%20Header%20Scanner%20(1).png)

<br><br>

![Second Image](https://github.com/Jeewaka15/My-Projects---First-Phase/blob/542feeb59718a47b3723da43ab74270a5eb21b71/HTTP%20Header%20Scanner/HTTP%20Header%20Scanner%20(2).png)





## ✨ Features

* Scan any public website
* Automatic HTTPS URL handling
* Detect missing security headers
* Calculate a security score
* Display recommendations for improvement
* Flask-powered web dashboard
* Responsive user interface
* Easy-to-understand security report

## 🔒 Security Headers Checked

* Content-Security-Policy (CSP)
* Strict-Transport-Security (HSTS)
* X-Frame-Options
* X-Content-Type-Options
* Referrer-Policy
* Permissions-Policy
* Cross-Origin-Opener-Policy
* Cross-Origin-Embedder-Policy
* Cross-Origin-Resource-Policy

## 🛠️ Technologies Used

* Python
* Flask
* HTTPX
* HTML5
* CSS3
* Bootstrap 5
* JavaScript

## 📂 Project Structure

```text id="6ev8ha"
HTTP-Header-Scanner/
│
├── app.py
├── scanner.py
├── config.py
├── requirements.txt
│
├── templates/
│   ├── layout.html
│   ├── index.html
│   └── report.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── README.md
```

## 🔍 Security Concepts Covered

* HTTP Protocol Fundamentals
* HTTP Response Headers
* Browser Security Mechanisms
* Clickjacking Protection
* MIME Type Protection
* HTTPS Enforcement
* Content Security Policy (CSP)
* Cross-Origin Security
* Secure Web Configuration

## 📚 What I Learned

Building this project helped me improve my understanding of:

* HTTP request and response lifecycle
* Security header analysis
* Flask web application development
* Python networking with HTTPX
* Secure web application practices
* Building cybersecurity auditing tools
* Report generation and security scoring
* Backend and frontend integration

## 🎯 Future Improvements

* Export reports as PDF
* Multi-site scanning
* Historical scan comparison
* OWASP Security Checks
* SSL/TLS Certificate Analysis
* HTTP/2 and HTTP/3 Detection
* REST API Support
* Docker Deployment
* Cloud Deployment (Render)

## 👨‍💻 About This Project

This project is part of my **Cybersecurity Foundations – Phase 01** series, where I build practical cybersecurity tools to strengthen my understanding of secure web technologies, networking, and Python application development through hands-on implementation.
