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

> ⚠️ **Note:** This project is primarily intended for learning and experimentation with Python and symmetric cryptography.

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

---
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
# The Story Behind My Encryption Project

## Introduction

Hello everyone,

I want to share the story behind one of my projects and explain how I got the idea for it.

One day, I was learning Python and I was still studying the basics. At that time, I had a friend named **Abdullah**. His uncle was very experienced in cybersecurity.

My friend sometimes asked his uncle to give us cybersecurity challenges so we could practice and improve our skills. At first, the challenges were quite simple.

One day, I asked my friend:

**"Why doesn't your uncle give us a bigger or more difficult challenge?"**

He told me:

**"I will ask him when I see him."**

A few days later, my friend came back with a new challenge.

He told me:

**"My uncle gave us a very big challenge. It requires programming, and we have to create our own encryption method."**

At that moment, I was surprised by how difficult the challenge sounded. Honestly, my first thought was:

**"Maybe I won't be able to finish this project."**

His uncle gave us one full month to complete it.

I agreed, but then I asked:

**"How are we going to create our own encryption method when we don't even know much about encryption?"**

So, we decided to learn the basic concepts of encryption first and then decide how to build our project.

---

## The First Idea

During the first week, we realized that the project was not going to be easy.

I then told my friend:

**"Ask your uncle what kind of encryption method he wants us to create."**

He agreed.

The next day, my friend came back and explained his uncle's idea.

The basic concept was very simple:

Every character would have its own special symbol.

For example:

**ا = !**
**ب = @**
**ت = #**

This is a very simple example of how a substitution system can work.

At first, the idea seemed easy. However, I quickly noticed a problem.

The system was very limited.

### Why was it limited?

Because we would need to create a unique symbol for every character we wanted to support.

For example, if we wanted to support Arabic, we would need symbols for all Arabic letters. If we wanted to support English, numbers, and other characters, we would need to create symbols for them too.

This would make the system very large and difficult to manage.

Even after my friend finished his project, it was mainly designed for the Arabic characters that had been assigned symbols, with only a few additional symbols.

I am not saying that my friend's project was bad.

Actually, it was the opposite.

His project helped me notice an important problem and gave me the idea for my own project.

---

## The Problem I Noticed

The main problem was **language and character limitations**.

I started thinking:

**"Why should the system only support Arabic?"**

What if the user speaks English?

What if they use Chinese?

What if they use another language?

There are thousands of different characters and symbols used around the world.

This made me think about a different approach.

Instead of creating a special symbol for every character, I wanted to create a system where **any text could be encrypted and later decrypted**.

This was the beginning of my project.

---

## The Idea Behind My Project

The main idea of my project is simple:

> **Take any text as input, encrypt it, and allow the user to decrypt it later.**

The goal was to avoid the limitation of supporting only a specific language or a fixed list of characters.

Of course, this project is **not designed to replace professional encryption tools**, and it should not be considered a fully secure solution for protecting sensitive information.

However, it was an important learning project for me.

My goal was to experiment with encryption, understand how the process works, and solve the character limitation that I noticed in the original idea.

I also wanted the encryption and decryption process to be stable and reliable for the text supported by my implementation.

---

## The Result

After I finished the project, I sent it to my friend.

He then sent it to his uncle.

After about two or three days, my friend came back and told me:

**"I sent the project to my uncle, and he said it was very good for a first project."**

However, there was one more thing.

His uncle reminded us that we had originally agreed to create the project with a **Graphical User Interface (GUI)**.

I had completely forgotten about that part!

So, I started learning **CustomTkinter** to build the graphical interface for the project.

At the moment, I am still working on it and I have completed around half of the learning process.

I am also thinking about starting another project after I finish my CustomTkinter course.

---

## What I Learned

This project taught me more than just programming.

I learned that sometimes a simple idea can reveal a bigger problem.

I also learned that when you find a limitation in an existing idea, you can use that limitation as a starting point for creating something better.

Most importantly, this project gave me more motivation to continue learning **Python, cybersecurity, encryption, and GUI development**.

This is only one step in my learning journey, and I hope to build more advanced projects in the future.

## The End

**Mr. ABBAS**
**September 5, 2026**

---
