# 🔐 SecureVault – Encrypted Password Manager

SecureVault is a secure password manager built with **Python** and **Flask** as part of my Cybersecurity Foundations journey. The project focuses on applying modern cryptographic principles rather than simply storing passwords in plain text.

## 🚀 Overview

SecureVault allows users to securely store, manage, and retrieve account credentials through a web-based dashboard protected by a master password.

The application uses industry-recognized security practices, including:

* Argon2id for secure master password hashing and key derivation
* AES-GCM authenticated encryption for protecting vault data
* Session-based authentication
* Encrypted local password vault
* CRUD operations for password management
* Search functionality for stored accounts
* Responsive Flask web interface


![First Image](https://github.com/Jeewaka15/My-Projects-First-Phase/blob/d8fac9ad9c6b9a1b0ed62d5313d6b35734a91d84/SecureVault/SecureVault%20(1).png)

<br><br>

![Second Image](https://github.com/Jeewaka15/My-Projects-First-Phase/blob/d8fac9ad9c6b9a1b0ed62d5313d6b35734a91d84/SecureVault/SecureVault%20(2).png)

<br><br>

![Third Image](https://github.com/Jeewaka15/My-Projects-First-Phase/blob/d8fac9ad9c6b9a1b0ed62d5313d6b35734a91d84/SecureVault/SecureVault%20(3).png)


---

## ✨ Features

* 🔐 Master Password Authentication
* 🛡️ Argon2id Password Hashing
* 🔑 AES-GCM Vault Encryption
* ➕ Add New Accounts
* ✏️ Update Existing Credentials
* 🗑️ Delete Stored Accounts
* 🔍 Search Saved Passwords
* 🌐 Flask Web Dashboard
* 📁 Encrypted Local Storage
* 📱 Responsive User Interface

---

## 🏗️ Project Structure

```text
SecureVault/
│
├── app.py
├── config.py
├── services/
│   ├── auth.py
│   ├── encryption.py
│   └── vault_service.py
│
├── templates/
├── static/
│
└── vault/
    ├── vault.enc
    ├── master.hash
    └── salt.bin
```

---

## 🔒 Security Concepts Implemented

This project helped me understand and implement several cybersecurity concepts:

* Password Hashing (Argon2id)
* Cryptographic Salt Generation
* Key Derivation
* AES-GCM Authenticated Encryption
* Secure Local Storage
* Authentication Workflows
* Session Management
* Confidentiality and Data Protection
* Secure Software Design

---

## 🛠️ Technologies Used

* Python
* Flask
* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* Argon2-cffi
* Cryptography (AES-GCM)

---

## 📚 What I Learned

Through this project, I improved my understanding of:

* Secure authentication systems
* Cryptography fundamentals
* Password hashing vs encryption
* Flask web development
* Backend architecture
* Building secure CRUD applications
* Project organization and modular design
* Applying cybersecurity best practices in software development

---

## 🎯 Future Improvements

* Password Generator
* Password Strength Meter
* Edit Account Modal
* Dark/Light Theme
* Security Analytics Dashboard
* Import & Export Encrypted Vault
* Multi-user Support
* Docker Deployment
* Cloud Backup
* Two-Factor Authentication (2FA)

---

## 👨‍💻 About This Project

This project is part of my **Cybersecurity Learning Journey (Phase 01 – Foundations)**, where I build practical projects to strengthen both my software engineering and cybersecurity skills. My goal is to create production-inspired applications while learning the security principles behind them.
