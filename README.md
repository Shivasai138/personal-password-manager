# Personal Password Manager

A command-line Password Manager developed using Python for learning file handling, dictionaries, functions, exception handling, and secure password generation.

> Note: This project is intended for educational purposes. Passwords are stored in a plain-text file, so real credentials should not be used.

## Features

- Save website and password details
- View saved entries
- Search passwords by website
- Generate random 16-character passwords
- Update existing passwords
- Delete stored website/password entries
- Persist data using file handling
- Prevent duplicate website entries

## Technologies and Concepts

- Python
- Dictionaries
- File Handling
- Functions
- Exception Handling
- `secrets` module
- `string` module

## Password Generation

The application uses Python's `secrets` module to generate 16-character passwords using:

- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

## Application Menu

1. Save Password
2. View Passwords
3. Generate Password
4. Search Site
5. Update Password
6. Delete Password
7. Exit

## Data Storage

The application stores data locally in:

`passwords.txt`

The file is excluded from Git using `.gitignore`.

## Important Security Notice

This application was created as a Python learning project and is not intended to be used as a production password manager. Stored passwords are not encrypted. Do not use real or sensitive credentials with this application.

## Run the Project

```bash
python password_manager.py