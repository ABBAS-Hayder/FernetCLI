# 🔐  FernetCLI

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Cryptography-Fernet-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/CLI-Application-black?style=for-the-badge&logo=gnu-bash">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge">
</p>

<p align="center">
  <b>A simple command-line text encryption & decryption tool built with Python.</b>
</p>

---

## 📝 About 

**FernetCLISec_Project** is a lightweight command-line application written in Python that allows you to:

* 🔒 Encrypt text securely
* 🔓 Decrypt previously encrypted text
* 🔑 Automatically generate and store an encryption key
* 🎨 Display a clean and interactive terminal interface
* ⚡ Work completely from the command line

The project uses the **Fernet symmetric encryption** implementation provided by the `cryptography` library.

> ⚠️ **Note:** This project is primarily intended for learning and experimentation with Python and symmetric cryptography. It should not be considered a production-grade password manager or secure storage solution.

---
⤵️ The Interface 

![image alt](https://github.com/ABBAS-Hayder/Sec_project/blob/7fb75a0eb9a0953b0ae26b66589db36f1abbbe07/Screenshot%20from%202026-09-04%2017-35-52.png)

---

## 🛠️ Technologies

* 🐍 **Python**
* 🔐 **Cryptography / Fernet**
* 🎨 **Rich**
* 🔤 **PyFiglet**
* 📁 **OS / File Handling**

### Python Libraries
---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/ِABBAS-Hayder/Sec_Project.git
cd Sec_Project
```

### 2. Install Libraries

```bash
pip install -r requirements.txt
```

### 3. Run the program

```bash
python FernetCIL.py
```

---

## 🚀 Usage

After starting the program, you will see a menu similar to:

![image alt](https://github.com/ABBAS-Hayder/Sec_project/blob/7fb75a0eb9a0953b0ae26b66589db36f1abbbe07/Screenshot%20from%202026-09-04%2017-35-52.png)


### 🔒 Encrypt Text

Choose:

```text
1
```

Then enter your plaintext:

```text
Enter Your Text 📩 : Hello World
```

The program will generate a Fernet ciphertext:

```text
Your Cipher : ---> gAAAAAB...
```

---

### 🔓 Decrypt Text

Choose:

```text
2
```

Then provide the encrypted ciphertext:

```text
Enter The Cipher 🔐 : gAAAAAB...
```

The program will decrypt it using the locally stored key.

```text
Your Clean Text: ---> Hello World
```

---

## 🔑 How the Key Works

When the program starts, it checks whether:

```text
Critical_File.key
```

exists.

### If the key does not exist

A new Fernet key is generated automatically:

```python
key = Fernet.generate_key()
```

and saved into:

```text
Critical_File.key
```

### If the key already exists

The existing key is loaded and used for encryption/decryption.

```text
Program
   │
   ▼
Check Secure.key
   │
   ├── Not Found ──► Generate Key
   │                    │
   │                    ▼
   │               Save Secure.key
   │
   └── Found ─────► Load Key
                        │
                        ▼
                  Fernet Cipher
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
          Encrypt              Decrypt
```

---

---

## 📂 Project Structure

```text
Sec_Project/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── Secure.key        # Generated locally - DO NOT COMMIT
```

---

---

## 🎯 Project Goals

This project was created as a practical exercise to improve my understanding of:

* Python programming
* File handling
* Symmetric cryptography
* Key management
* CLI application development
* Terminal UI design

---

## 👨‍💻 Author

**ABBAS**

> Built with Python, curiosity for knowledge How cryptography works, and a little bit of 🔐 security.

---
