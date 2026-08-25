# 🔍 Hash Identifier

![Wallpaper Image]([https://github.com/Jeewaka15/My-Projects---First-Phase/blob/00bde57f39143f025f7b845eeeba9723a4b11142/Hash%20Identifier/Hash%20Identifier%20(1).png](https://github.com/Jeewaka15/My-Projects---First-Phase/blob/00bde57f39143f025f7b845eeeba9723a4b11142/Hash%20Identifier/Hash%20Identifier%20Project%20Wallpaper.png))

<br><br>

A Python and Flask-based Hash Identifier built as part of my **Cybersecurity Foundations (Phase 01)** learning journey. This project analyzes an input hash and identifies its possible hash algorithm based on its length, format, prefix, and character set.

## 🚀 Overview

Hash Identifier is a practical cybersecurity tool designed to help identify common hash types without attempting to crack them. It provides a clean web interface and a REST API for identifying hashes, making it useful for learning digital forensics, password security, and penetration testing fundamentals.

![First Image](https://github.com/Jeewaka15/My-Projects---First-Phase/blob/00bde57f39143f025f7b845eeeba9723a4b11142/Hash%20Identifier/Hash%20Identifier%20(1).png)

<br><br>

![Second Image](https://github.com/Jeewaka15/My-Projects---First-Phase/blob/00bde57f39143f025f7b845eeeba9723a4b11142/Hash%20Identifier/Hash%20Identifier%20(2).png)

<br><br>

![Third Image](https://github.com/Jeewaka15/My-Projects---First-Phase/blob/00bde57f39143f025f7b845eeeba9723a4b11142/Hash%20Identifier/Hash%20Identifier%20(3).png)





## ✨ Features

* Identify common hash algorithms
* Pattern-based hash detection
* Confidence score for each result
* Web-based user interface using Flask
* REST API endpoints
* Batch scanning from text files
* Save scan results automatically
* Lightweight and easy to extend

## 🔐 Supported Hash Types

* MD5
* SHA-1
* SHA-224
* SHA-256
* SHA-384
* SHA-512
* bcrypt
* Argon2
* NTLM
* LM
* MySQL Hashes
* And other common formats

## 🛠️ Technologies Used

* Python
* Flask
* HTML5
* CSS3
* JavaScript
* Regular Expressions
* REST API

## 📂 Project Structure

```text
Hash-Identifier/
│
├── api.py
├── hash_identifier.py
├── hashes.txt
├── results.txt
├── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md
```

## 📡 API Endpoints

| Method | Endpoint      | Description                |
| ------ | ------------- | -------------------------- |
| POST   | /api/identify | Identify a single hash     |
| POST   | /api/scan     | Scan hashes from a file    |
| GET    | /api/results  | View previous scan results |

## 📚 What I Learned

During this project I gained practical experience with:

* Cryptographic hash functions
* Differences between hashing and encryption
* Flask API development
* Regular expression pattern matching
* RESTful API design
* JSON request and response handling
* File handling in Python
* Cybersecurity tool development
* Modular Python programming

## 🎯 Future Improvements

* Drag-and-drop hash file upload
* Hash database integration
* Dark mode dashboard
* Export results to CSV and JSON
* Hash statistics dashboard
* Docker support
* Deployment on Render
* Additional hash format detection

## 👨‍💻 About This Project

This project is part of my **Cybersecurity Foundations – Phase 01** series, where I build practical cybersecurity tools to strengthen my understanding of Python programming, web development, and information security concepts through hands-on implementation.
