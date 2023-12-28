import secrets
import string
from colorama import *

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

def generate_and_savelinks(file_name, Links_Amount):
    with open(file_name, 'a') as file:
        for i in range(Links_Amount):
            first_string = generate_random_string(16) #Generate random 16 letters and digits
            second_string = generate_random_string(302) #Generate random 302 letters and digits
            third_string = generate_random_string(22) #Generate random 22 letters and digits
            link = f"https://discord.com/billing/partner-promotions/1180231712274387115/eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..{first_string}.{second_string}.{third_string}\n" #Create the Link
            file.write(link) #Save the link in the txt file
            print(f"{Fore.LIGHTGREEN_EX}[{Fore.LIGHTWHITE_EX}+{Fore.LIGHTGREEN_EX}] {Fore.LIGHTWHITE_EX}{link}") #Print the Link

Links_Amount = int(input("How much Links you want to generate?: ")) #Ask the Amount of links

generate_and_savelinks('links.txt', Links_Amount)

input(f"Succesfully generated and saved {Links_Amount} Links. Press enter to close!")