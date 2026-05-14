# Secure Vault System 🛡️

An enterprise-grade, full-stack secure authentication and document management system built with Flask, adhering to **Clean Architecture** principles. This project was developed to demonstrate advanced security concepts including AES-256 encryption, RSA digital signatures, Multi-Factor Authentication (MFA), and OAuth2 integration.

---

## 🌟 Key Features

### 1. Identity & Access Management
- **Secure Authentication**: Password hashing using **Bcrypt** with adaptive salt.
- **Multi-Factor Authentication (2FA)**: Time-based One-Time Password (TOTP) integration with Google Authenticator/Authy.
- **OAuth 2.0 Integration**: Support for real **Google** and **GitHub** sign-in.
- **JWT-based Sessions**: Stateless authentication using JSON Web Tokens (HS256).
- **Role-Based Access Control (RBAC)**: Granular permissions for **Admin**, **Manager**, and **User** roles.

### 2. Advanced Document Security
- **AES-256 Encryption**: All uploaded files are encrypted at rest using AES-256-CBC.
- **Digital Signatures**: **RSA-2048** signatures ensure non-repudiation and authenticity.
- **Integrity Verification**: Real-time **SHA-256** hash checking to detect file tampering.
- **Metadata Management**: Detailed audit trails for every document.

### 3. Secure Communication
- **End-to-End TLS**: Full **HTTPS** support with self-signed certificate generation.
- **Secure Headers**: Protection against common web vulnerabilities.

---

## 🚀 Quick Start

### 1. Installation
```bash
# Clone the repository
git clone <your-repo-url>
cd secure-auth-system

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration
Create a `.env` file from the example:
```bash
cp .env.example .env
```
Update the `.env` file with your secret keys and OAuth credentials.

### 3. Generate Security Certificates
```bash
python generate_certs.py
```

### 4. Run the Application
```bash
python run.py
```
Access the system at: **`https://127.0.0.1:5000`**

---

## 🏗️ Architecture
The project follows a **Clean Architecture** pattern to ensure maintainability and scalability:

- `app/auth`: Handles identity, 2FA, and OAuth logic.
- `app/documents`: Manages encryption, signing, and file storage.
- `app/admin`: User management and role enforcement.
- `app/models`: Database schemas (SQLAlchemy).
- `app/utils`: Shared security helpers (Crypto, JWT, Password Policy).

---

## 🛡️ MITM Demonstration (Wireshark)
To demonstrate the importance of HTTPS:
1. **HTTP Mode**: Delete `cert.pem` and run the app. Capture traffic in Wireshark to see plain-text credentials.
2. **HTTPS Mode**: Restore `cert.pem` and run the app. Observe that all traffic is now encrypted and unreadable to attackers.

---

## 📝 License
This project is for educational purposes.
