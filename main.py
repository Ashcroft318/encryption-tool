from args_processor import create_parser
from rich.console import Console
from handler import (
    handle_generate_key, handle_encrypt, handle_decrypt, handle_decrypt_all,
    handle_encrypt_file, handle_decrypt_file, handle_view_file
)


console = Console()

def main():
   parser = create_parser()
   args = parser.parse_args()
  

   command_map = {
        "generate_key": handle_generate_key,
        "encrypt": lambda: handle_encrypt(args.encrypt),
        "decrypt": lambda: handle_decrypt(args.decrypt),
        "decrypt_all": handle_decrypt_all,
        "encrypt_file": lambda: handle_encrypt_file(args.encrypt_file, args.output),
        "decrypt_file": lambda: handle_decrypt_file(args.decrypt_file, args.output),
        "view_file": lambda: handle_view_file(args.view_file),
    }
   
   for arg, func in command_map.items():
        if getattr(args, arg, None):
            func()
            break
   else:
        parser.print_help()


if __name__=="__main__":
   main()