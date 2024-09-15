# ⚠️DONT USE ENCRYPTOR IN THE SAME DIRECTORY IN WHICH YOU ARE IN⚠️

# Encryption Tool

A simple Python-based file and directory encryption tool that uses XOR-based encryption to secure files. This tool allows you to encrypt and decrypt files and directories recursively.

### MADE AN OBFUSCATED VERSION IF USED FOR STUFF I CANT SAY HERE

## Features

- Encrypt individual files using a provided encryption key.
- Decrypt files that were encrypted using the same key.
- Encrypt an entire directory, including all subdirectories and files, recursively.
- Decrypt an entire directory recursively.
- Automatic renaming of files during encryption to prevent filename disclosure.
- Simple XOR encryption using a single-byte key.

## Requirements

- Python 3.x
- No external dependencies

## How It Works

1. The tool encrypts files using an XOR operation with the provided key.
2. During encryption, files are renamed to a random string with a `.encrypted` extension.
3. During decryption, files are restored to their original names and decrypted with the provided key.

## Usage

### Encrypting a Directory

To encrypt a directory and all its subdirectories, run:

```bash
python3 main.py encrypt <directory_path> <encryption_key>
```

Example:

```bash
python3 main.py encrypt /path/to/directory 123
```

This will encrypt all files under `/path/to/directory` recursively.

### Decrypting a Directory

To decrypt a directory and all its subdirectories, run:

```bash
python3 main.py decrypt <directory_path> <encryption_key>
```

Example:

```bash
python3 main.py decrypt /path/to/directory 123
```

This will decrypt all `.encrypted` files in `/path/to/directory` recursively.

### Notes

- Be careful with file permissions, especially when trying to encrypt system directories (e.g., `/etc`).
- The encryption key must be the same for both encryption and decryption.
- Encrypted files are renamed during the encryption process, so ensure you have the proper key to restore them.

## License

This project is licensed under the MIT License.
