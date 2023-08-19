"""
    Password Generator
"""
import random
import string
import pyperclip
import os
from colorama import Fore, Style, init
import pyfiglet

init()

def generate_password(length:int,
                      use_lower:bool=True,
                      use_upper:bool = True,
                      use_number : bool = True,
                      use_specials:bool  = False
                      ):
    """
        Generate a password of the specified length.
        Args:
            length (int): The desired number of characters in your generated password
        Keyword Arguments:
            use_lower {bool} -- Whether to include lowercase letters [default: True]
            use_upper {bool} -- Whether ot not to include uppercase letters [default: True]
            use_number {bool} -- Whether or not to include numbers[default: True]
            use_specials{bool}--Whether or not to include special symbols[default:False].
        Returns:
            str -- A string containing randomly selected alphanumeric 
            and/or special character values based on user input.
            
    """
    # Create an empty list for storing our final password
    passwrd= ''
    char = ''
    if use_lower:
        char +=string.ascii_lowercase
        passwrd+=random.choice(string.ascii_lowercase)
    if use_upper:
        char +=string.ascii_uppercase
        passwrd += random.choice(string.ascii_uppercase)
    if use_number:
        char += string.digits
        passwrd += random.choice(string.digits)
    if use_specials:
        char += string.punctuation
        passwrd += random.choice(string.punctuation)

    if not passwrd:
        raise ValueError(Fore.RED,"Invalid!!Choose atleast one character type.",Style.RESET_ALL)

    remaining_len = length - len(passwrd)
    if remaining_len<0:
        remaining_len = 0
    pswd = list(passwrd) + [random.choice(char) for _ in range(remaining_len)]
    random.shuffle(pswd)
    return ''.join(pswd)
    
def main():
    """
        Display the Password and save into the clipboard
    """
    title = pyfiglet.figlet_format("Password Generator",font='big')
    print(Style.BRIGHT + Fore.CYAN + title + Style.RESET_ALL)
    try:
        num_pass = int(input(f"\
                             {Fore.CYAN}How many passwords do you want to generate? "))
        length = int(input("\
                      Enter the desired length of the password:"))
        lower = input('\
                      Do you wish to include LOWERCASE letters?(y/n)').lower()=='y'
        upper = input('\
                      Do you wish to include UPPERCASE letters?(y/n)').lower()=='y'
        digit = input("\
                      Do you wish to include NUMBERS ?(y/n)").lower() == "y"
        special = input("\
                      Do you wish to include SPECIAL SYMBOLS?(y/n)").lower()=="y"
        print(Style.RESET_ALL)
        for _ in range(num_pass):
            password = generate_password(length,
                                   use_lower = lower,
                                   use_upper = upper,
                                   use_number = digit,
                                   use_specials=special)
            print(Fore.GREEN+"Generated Password: "+password)
            copy_choice = input('copy this password to clipboard? (y/n)').lower()
            if copy_choice=='y':
                pyperclip.copy(password)
                print("Password copied to clipboard!"+Style.RESET_ALL)
    except ValueError as error:
        print (Fore.RED,"Invalid Input!! Please enter valid values",error,Style.RESET_ALL)

if __name__ == '__main__':
    os.system('cls' if os.name =='nt' else 'clear')
    main()
    