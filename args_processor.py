import argparse
from rich_argparse import RichHelpFormatter

def create_parser():
    parser = argparse.ArgumentParser(description ="[bold cyan]C.A.S.T.L.E.[/bold cyan][bold purple]- Encryption Tool for privacy on messaging[/bold purple]",
                                     formatter_class= RichHelpFormatter)

    parser.add_argument("--generate-key", action="store_true", help="[bold yellow]Generate a new encryption key[/bold yellow]")
    parser.add_argument("--encrypt", type=str, help="[bold yellow]Encrypt a message and store it[/bold yellow]")
    parser.add_argument("--decrypt", type=str, help="[bold yellow]Decrypt a specific provided encrypted message[/bold yellow]")
    parser.add_argument("--decrypt_all", action="store_true", help="[bold yellow]Decrypt all stored message[/bold yellow]")
    
    parser.add_argument("--encrypt-file", type=str, help="[bold yellow]Encrypt a file; provide the input file path[/bold yellow]")
    parser.add_argument("--decrypt-file", type=str, help="[bold yellow]Decrypt a file; provide the input file path[/bold yellow]")
    parser.add_argument("--output", type=str, help="[bold yellow]Output file path for file encryption/decryption[/bold yellow]", default= None)
    parser.add_argument("--view-file", type=str, help= "[bold yellow]View the contents of a decrypted file.[/bold yellow]")
   

    return parser