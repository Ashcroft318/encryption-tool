from encryption import encrypt_message, decrypt_message, encrypt_file, decrypt_file
from storage import save_encrypted_message, load_encrypted_message, find_encrypt_message, view_file
from key_management import generate_key
from rich.console import Console
from rich.syntax import Syntax

console = Console()

def handle_generate_key():
    generate_key()
    console.print("✅ Encryption key generated successfully!", style="green")

def handle_encrypt(message):
    encrypted = encrypt_message(message)
    save_encrypted_message(encrypted)
    console.print(f"🔒 Encrypted Message:\n{encrypted.decode()}", style="cyan")

def handle_decrypt(message):
    found_message = find_encrypt_message(message)
    if found_message:
       try:
            decrypted = decrypt_message(found_message)
            syntax = Syntax(decrypted, "python", theme = "dracula")
            console.print(f"🔓 Decrypted Message:", syntax)
       except Exception as e:
          console.print(f"❌ Error decrypting message: {e}", style="red")

def handle_decrypt_all():
  messages = load_encrypted_message()
  if not messages:
        console.print("⚠️ No stored messages found.", style="yellow")
        return
  decrypted_messaging = f"🔓 Decrypted Messages:"
  theme_syntax = Syntax(decrypted_messaging,"python",theme="dracula")
  console.print(theme_syntax)
  for msg in messages:
        try:
            decrypted = decrypt_message(msg.strip())
            syntax = Syntax(decrypted, "python", theme="dracula")
            console.print(syntax)
        except Exception as e:
            console.print(f"❌ Error decrypting a message: {e}", style="red")

def handle_encrypt_file(input_path, output_path):
    try:
        output_path = encrypt_file(input_path, output_path)
        console.print(f"📁 File '{input_path}' has been encrypted and saved as '{output_path}'", style="cyan")
    except Exception as e:
        console.print(f"❌ Error encrypting file: {e}", style="red")

def handle_decrypt_file(input_path, output_path):
    try:
        output_path = decrypt_file(input_path, output_path)
        console.print(f"📂 File '{input_path}' has been decrypted and saved as '{output_path}'", style="green")
    except Exception as e:
        console.print(f"❌ Error decrypting file: {e}", style="red")

def handle_view_file(file_path):
    view_file(file_path)



    
