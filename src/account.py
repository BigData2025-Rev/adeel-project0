import json
import os
from menu import login_form
from colors import Messages

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

def log_in() -> str:
    accounts = load_accounts()

    while True:
        retry_count = 3
        while retry_count > 0:
            username, password = login_form()
            if username not in accounts or accounts[username]["password"] != password:
                retry_count -= 1
                Messages.error(f"Username or password incorrect. {retry_count} attempts left...")
            else:
                print(f"Welcome back, {username}!")
                Messages.end_message()
                return username
        Messages.error("Too many failed login attempts. Please try again later.")
        return None

def register() -> str:
    accounts = load_accounts()

    while True:
        username = input("Enter a username: ")
        
        if username in accounts:
            Messages.error("Username or password incorrect. Please try again...")
            continue
        break
    
    while True:
        password = input("Enter a password: ")
        confirm_password = input("Confirm your password: ")
        if password == confirm_password:
            break
        Messages.error("Passwords do not match. Please try again.")

    while True:
        print("\nWhat type of account would you like?")
        print("1. Checking\n2. Savings\n3. Both")

        user_accounts = {}

        account_choice = input("Enter your choice: ")
        if (account_choice.lower().strip() in ['1', 'c', 'checking']):
            user_accounts["checking"] = {"balance": 0.0}
            break
        elif (account_choice.lower().strip() in ['2', 's', 'saving', 'savings']):
            user_accounts["savings"] = {"balance": 0.0}
            break
        elif (account_choice.lower().strip() in ['3', 'b', 'both']):
            user_accounts["savings"] = {"balance": 0.0}
            user_accounts["checking"] = {"balance": 0.0}
            break
        else:
            Messages.error("Invalid Choice. Please try again...")

    accounts[username] = {
        "password": password,
        "accounts": user_accounts
    }

    save_account(accounts)

    Messages.success("Account created!")
    Messages.end_message()
    return username