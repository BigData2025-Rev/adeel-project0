import json
import os
from colors import Color

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ACCOUNT_FILE = os.path.join(BASE_DIR, "../data/accounts.json")

def load_accounts():
    if os.path.exists(ACCOUNT_FILE):
        with open(ACCOUNT_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_account(account):
    with open(ACCOUNT_FILE, 'w') as file:
        json.dump(account, file, indent=4)

def log_in():
    accounts = load_accounts()

    print("Log In")

    while True:
        print("================")
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if username not in accounts:
            print('\n' + Color.RED + "Username or password incorrect. Please try again..." + Color.END + '\n')
            continue
        
        if accounts[username]["password"] == password:
            print(f"Welcome back, {username}!")
            break
        else:
            print('\n' + Color.RED + "Username or password incorrect. Please try again..." + Color.END + '\n')
    
    return username

def register():
    accounts = load_accounts()
    print("\nRegister")
    print("================")

    while True:
        username = input("Enter a username: ")
        
        if username in accounts:
            print("Username already exists. Please try a different one.")
            continue
        break
    
    while True:
        password = input("Enter a password: ")
        confirm_password = input("Confirm your password: ")
        if password == confirm_password:
            break
        print('\n' + Color.RED + "Passwords do not match. Please try again." + Color.END + '\n')

    while True:
        print("\nWhat type of account would you like?")
        print("1. Checking 2. Savings 3. Both")

        user_accounts = {}

        account_choice = input("Enter your choice: ")
        if (account_choice.lower().strip() in ['1', 'c', 'checking']):
            user_accounts["checking"] = {"balance": 0.0}
            break
        elif (account_choice.lower().strip() in ['2', 's', 'saving', 'savings']):
            user_accounts["savings"] = {"balance": 0.0, "rate": 3.9}
            print('Your saving account interest rate is 3.9%')
            break
        elif (account_choice.lower().strip() in ['3', 'b', 'both']):
            user_accounts["savings"] = {"balance": 0.0, "rate": 3.9}
            user_accounts["checking"] = {"balance": 0.0}
            break
        else:
            print('\n' + Color.RED + "Invalid Choice. Please try again..." + Color.END + '\n')

    accounts[username] = {
        "password": password,
        "accounts": user_accounts
    }

    save_account(accounts)

    print('Registered!')

    return username