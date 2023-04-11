import colorama
from colorama import Fore, Style
import os

colorama.init()

def encode(str_to_encode, key):
    byte_seq = [ord(char) for char in str_to_encode]
    encoded_byte_seq = [byte ^ key for byte in byte_seq]
    encoded_str = "".join([chr(byte) for byte in encoded_byte_seq])
    return encoded_str

def decode(encoded_str, key):
    encoded_byte_seq = [ord(char) for char in encoded_str]
    decoded_byte_seq = [byte ^ key for byte in encoded_byte_seq]
    decoded_str = "".join([chr(byte) for byte in decoded_byte_seq])
    return decoded_str

def main():
    os.system("cls")
    os.system("title Axeos")
    print(Fore.RED + '''
      _                        
    / \   __  _____  ___  ___ 
   / _ \  \ \/ / _ \/ _ \/ __|
  / ___ \  >  <  __/ (_) \__ \\
 /_/   \_\/_/\_\___|\___/|___/
''')



    key = None
    while not key:
        key_input = input(Fore.YELLOW + "Veuillez entrer une clé de substitution en hexadécimale: ")
        try:
            key = int(key_input, 16)
        except ValueError:
            print(Fore.RED + "Clé invalide. Veuillez entrer une valeur hexadécimale.")
    os.system("cls")
    print(Fore.GREEN + f"Axeos - Clé de substitution : {hex(key)}")
    while True:
        print(Fore.YELLOW + "1 -", Fore.YELLOW + "Encoder")
        print("2 -", Fore.YELLOW + "Décoder")
        print("3 -", Fore.RED + "Quitter")
        choice = input(Style.RESET_ALL + "Entrez votre choix : ")
        os.system("cls")
        if choice == "1":
            str_to_encode = input(Fore.YELLOW + "Veuillez entrer une chaîne de caractères : ")
            try:
                encoded_str = encode(str_to_encode, key)
                print( Fore.YELLOW + "Chaîne encodée : ", Fore.CYAN + encoded_str)
            except Exception as e:
                print("Erreur : ", Fore.RED + str(e))
        elif choice == "2":
            encoded_str = input(Fore.YELLOW + "Veuillez entrer une chaîne encodée : ")
            try:
                decoded_str = decode(encoded_str, key)
                print("Chaîne décodée : ", Fore.CYAN + decoded_str)
            except Exception as e:
                print("Erreur : ", Fore.RED + str(e))
        elif choice == "3":
            break
        else:
            print(Fore.RED + "Veuillez sélectionner une opération.")

        input(Fore.YELLOW + "Appuyez sur Entrée pour continuer...")
        os.system("cls")

if __name__ == "__main__":
    main()
