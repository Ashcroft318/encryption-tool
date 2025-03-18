from cryptography.fernet import Fernet
from key_management import load_key
import os


OUTPUT_DIR = "output_files"

def output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)



def encrypt_message(message):
    key = load_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message.encode())
    return encrypted

def decrypt_message(encrypted_message):
    key = load_key()
    cipher = Fernet(key)
    decrypted = cipher.decrypt(encrypted_message).decode()
    return decrypted


def  encrypt_file(input_path, output_filename):
    key = load_key()
    cipher = Fernet(key)
    
    output_dir()
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    print(f"🔹 Encrypting file: {input_path}")
    print(f"📁 Saving to: {output_path}")

    with open(input_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(file_data)
    with open(output_path, 'wb') as file:
        file.write(encrypted_data)
    return output_path

def decrypt_file(input_path, output_filename):
    key = load_key()
    cipher = Fernet(key)

    output_dir()
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    print(f"🔹 Decrypting file: {input_path}")
    print(f"📁 Saving to: {output_path}")

    with open(input_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(output_path, 'wb') as file:
        file.write(decrypted_data)
    return output_path

