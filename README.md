# Password Vault

A command-line password manager built with Python and JSON.

## Features

* Add and save account credentials
* List saved accounts
* Search by website or username
* Edit saved passwords
* Delete accounts with password confirmation
* Master password prompt

## Requirements

* Python 3
* No external dependencies

## Usage

Run the program:

```bash
python password_vault.py
```

On first launch, create a master password. On subsequent launches, enter it to access the menu.

## Data Storage

The application stores account data in `pass.json` and the master password in `master.json`.

**Security warning:** This is a learning project, not a secure password manager. Passwords are stored as plain text and the master password is not securely hashed. Do not use it to store real credentials.

The `.gitignore` file excludes `pass.json` and `master.json` from Git to help prevent accidental publication of private data.

## Technologies

* Python
* JSON
* `getpass`
* Object-oriented programming
