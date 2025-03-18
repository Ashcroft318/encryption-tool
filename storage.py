import os
from rich.console import Console
from rich.syntax import Syntax
import datetime


console = Console()
STORAGE_FILE = "message.txt"


def save_encrypted_message(encrypted_message):
    with open(STORAGE_FILE, 'ab') as file:
        file.write(encrypted_message + b"\n")

def save_encrypted_message_time(encrypted_message):
    timestamp = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    with open(STORAGE_FILE, 'ab') as file:
        file.write(f"[{timestamp}]".encode() + encrypted_message + b"\n")


def load_encrypted_message():
    if not os.path.exists(STORAGE_FILE):
        return[]
    with open(STORAGE_FILE, 'rb') as file:
        return file.readlines()


def find_encrypt_message(target_message):
    try:
        with open(STORAGE_FILE,"r") as file:
            for line in file:
                if line.strip() == target_message:
                    return target_message.encode()
    except FileNotFoundError:
        return None
    return None

def view_file(file_path):
    try:
        if not os.path.exists(file_path):
            console.print(f"[bold red]❌ Error: the file  '{file_path}' does not exist[/bold red]")
            return
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        if not content.strip():
            console.print("[bold yellow]⚠️ Warning: The file is empty.[/bold yellow]")
            return
        
        syntax = Syntax(content, "plaintext", theme = "monokai", line_numbers=True)
        console.print(syntax)

    except Exception as e:
        console.print(f"[bold red]❌ Error reading file: {e}[/bold red]")

