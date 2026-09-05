###################################################################         (Libary & outhers)
from cryptography.fernet import Fernet
import os
from pyfiglet import figlet_format
from rich import print
from rich.console import Console
from rich.theme import Theme

console_theme = Theme({"g": 'bold green', "u": 'reverse red'})
console = Console()
console = Console(theme=console_theme)


def line():
    print("\n")


##################################################################          (Key_file & generate KEY)

KEY_FILE = "Secure.key"


def generate_key():
    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as f:
        f.write(key)

    return key


#################################################################           (Chack Key_file & )

def load_key():
    if not os.path.exists(KEY_FILE):
        return generate_key()

    with open(KEY_FILE, "rb") as f:
        return f.read()


key = load_key()

cipher = Fernet(key)

#################################################################           (Bunner & Arts)
line()

print(figlet_format("FernetCLI", font="doom"))


def main():
    while True:
        console.print("[purple]=[purple]" * 45)
        console.print("\n 1. Encrypt Text 📥", style="italic")
        console.print("\n 2. Decrypt Text 📤 ", style="italic")
        console.print("\n 3. Exit 👋 ", style="bold")

        console.print("[purple]=[bold purple]" * 45)

        choice = console.input("\nChoose ---> [red]1[red] / [green]2[green] / [blue]3[blue] :")

        ##################################################################

        if choice == "1":

            text = input("\n Enter Your Text 📩 : ")

            encrypted = cipher.encrypt(text.encode())

            console.print(f"\nYour Cipher : ---> [bold yellow]{encrypted.decode()}[bold yellow]")

        elif choice == "2":
            encrypted = input("\n Enter The Cipher 🔐 : ")

            try:
                decrypted = cipher.decrypt(encrypted.encode())

                console.print(f"\n Your Clean Text: ---> [green]{decrypted.decode()}[green]")

            except Exception as e:
                print("\n[red]Failed![red]")
                print(e)

        elif choice == "3":
            print("\n[cyan]Bye!,[cyan]", "TryHarder 👾\n")
            break

        else:
            print("\n[red]Invalied Option![red]")


##################################################################

if __name__ == "__main__":
    main()

# This project build by me __N17__ :)
