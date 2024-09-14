import sys
import os
from encryptor import encrypt_directory, decrypt_directory

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 main.py <encrypt|decrypt> <directory_path> <encryption_key>")
        sys.exit(1)

    action = sys.argv[1]
    directory = sys.argv[2]
    try:
        key = int(sys.argv[3])  # Convert key to an integer (1-byte key)
    except ValueError:
        print("The encryption key must be an integer.")
        sys.exit(1)

    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        sys.exit(1)

    if action == "encrypt":
        encrypt_directory(directory, key)
        print(f"Encryption completed for directory: {directory}")
    elif action == "decrypt":
        decrypt_directory(directory, key)
        print(f"Decryption completed for directory: {directory}")
    else:
        print("Invalid action. Use 'encrypt' or 'decrypt'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
