import os
from rich.console import Console
from cryptography.fernet import Fernet

KEY_FILE = "secret.key"
console = Console()

def generate_key():
    if not os.path.exists(KEY_FILE):
        key=Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
        console.print("Encryption key generated and saved.", style="green")
    else:
        console.print("Key already exists.",style="cyan" )

def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            return key_file.read()
    else:
        raise FileNotFoundError("Key not found! Please generate a key with --generate-key.")