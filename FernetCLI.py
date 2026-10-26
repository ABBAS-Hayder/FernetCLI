###################################################################         (Libary & outhers)
from cryptography.fernet import Fernet, InvalidToken
import os
from pyfiglet import figlet_format
from pygments.styles.dracula import yellow
from rich import print
from rich.console import Console
from rich.theme import Theme

console_theme = Theme({"g": 'bold green', "u": 'reverse red'})
console = Console()
console = Console(theme=console_theme)


def line():
    print("\n")


##################################################################          (Key_file & generate KEY)

KEY_FILE = "Critical_File.key"


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

#################################################################           (Interface & Arts)
line()

print(figlet_format("FernetCLI", font="doom"))


def main():
    while True:
        console.print("[purple]=[bold purple]" * 45)
        console.print("\n 1. Encrypt Text 📥", style="italic")
        console.print("\n 2. Decrypt Text 📤 ", style="italic")
        console.print("\n 3. Exit 👋 ", style="bold")

        console.print("[purple]=[bold purple]" * 45)

        choice = console.input("\nChoose ---> [red]1[red] / [green]2[green] / [blue]3[blue] :")

        ##################################################################

        if choice == "1":

            text = input("\n Enter Your Text 📩 : ")

            encrypted = cipher.encrypt(text.encode("utf-8"))

            console.print(f"\nYour Cipher : ---> [bold yellow]{encrypted.decode()}[bold yellow]")
        elif choice == "2":

            print()

            print("Put Here The Cipher Text ")

            console.print(f"[yellow]Click Enter Two Time[yellow]")

            parts = []

            while True:
                part = input()

                if not part.strip():
                    break

                parts.append(part)

            encrypted = "".join("".join(parts).split())

            if not encrypted:
                console.print("You are not set the cipher ", style="bold red")
                continue

            try:
                decrypted = cipher.decrypt(encrypted.encode("utf-8"))

                console.print(f"[green]\nYour Clean Text Is : [green]")
                print()
                console.print( decrypted.decode("utf-8"), markup=False , style="bold yellow")
                print()

            except InvalidToken:
                console.print( "Invalid token, wrong key, or corrupted data.",
                              style="bold red",
                )

        elif choice == "3":
            print("\n[cyan]Bye!,[cyan]", "TryHarder 👾\n")
            break

        else:
          console.print("\n Please Choose Any One  ( 1 / 2 / 3 ) ", style="bold red")

##################################################################

if __name__ == "__main__":
    main()

# This project build by me __ABBAS__ :)
