import sys
import pyfiglet

# Banner maker
def ascii_maker():
    print('-' * 70)
    ascii_banner = pyfiglet.figlet_format("A C I I banner").upper()
    print(ascii_banner)
    print('-' * 70)
    
    text = input("\nEnter Your Text: ")
    banner = pyfiglet.figlet_format(f"{text}").upper()
    print(banner)
