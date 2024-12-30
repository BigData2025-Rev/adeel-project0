from colors import Messages

# MAIN MENU

def main_menu() -> int:
    while True:
        Messages.title("Main Menu")
        print("1. Log In")
        print("2. Create Account")
        print("3. Exit")

        login_screen_select = input("\nSelection: ")

        try:
            if (int(login_screen_select) not in [1, 2, 3]):
                Messages.error("Invalid Selection... Please try again.")
                continue
            return int(login_screen_select)
        except ValueError:
            Messages.error("Invalid Input... Please enter a number.")

# BANKING MENUS

def bank_menu() -> int:
    while True:
        Messages.title("Bank Menu")
        print("1. View Account Balance(s)")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Transfer Funds")
        print("5. Exit Menu")
        bank_screen_select = input("\nSelection: ")

        try:
            if (int(bank_screen_select) not in [1, 2, 3, 4, 5]):
                Messages.error("Invalid Selection... Please try again.")
                continue
            return int(bank_screen_select)
        except ValueError:
            Messages.error("Invalid Input... Please enter a number.")

def account_select_menu(account_list):
    print("\nYour Accounts:")
    i = 1
    for account_type in account_list:
        print(f"{i}. {account_type.upper()}")
        i += 1
    while True:
        account_choice = input("Please select an account (or type 'exit' to exit): ").strip()
        if account_choice.lower() == "exit":
            return "exit"
        try:
            account_choice = int(account_choice)
            if account_choice not in range(1, i):
                Messages.error("Invalid Selection... Please try again.")
            else:
                break
        except ValueError:
            Messages.error("Invalid Input... Please enter a number.")
    selected = account_list[account_choice - 1]
    return selected

def amount_deposit_menu() -> int:
    while True:
        amount_input = input("Enter the amount you would like to deposit (or type 'exit' to exit): ").strip()
        if amount_input.lower() == "exit":
            return "exit"
        try:
            amount = float(amount_input)
            if amount > 0:
                break
            else:
                Messages.error("Invalid Input... Please enter a positive number.")
        except ValueError:
            Messages.error("Invalid Input... Please enter a number.")
    return amount

def amount_withdraw_menu(user_balance: int) -> int:
    while True:
        amount_input = input("Enter the amount you would like to withdraw (or type 'exit' to exit): ").strip()
        if amount_input.lower() == "exit":
            return "exit"
        try:
            amount = float(amount_input)
            if 0 < amount <= user_balance:
                break
            else:
                Messages.error("Invalid Input... Please enter an amount less than or equal to your balance.")
        except ValueError:
            Messages.error("Invalid Input... Please enter a number.")
    return amount

def amount_transfer_menu(user_balance: int) -> int:
    while True:
        amount_input = input("Enter the amount you would like to transfer (or type 'exit' to exit): ").strip()
        if amount_input.lower() == "exit":
            return "exit"
        try:
            amount = float(amount_input)
            if 0 < amount <= user_balance:
                break
            else:
                Messages.error("Invalid Input... Please enter an amount less than or equal to your balance.")
        except ValueError:
            Messages.error("Invalid Input... Please enter a number.")
    return amount

def transfer_multaccounts_menu() -> int:
    while True:
        print("1. Transfer between your accounts")
        print("2. Transfer to another user")
        user_choice = input("Selection (or type 'exit' to exit): ").strip()
        if user_choice.lower() == "exit":
            return "exit"
        try:
            user_choice = int(user_choice)
            if user_choice not in [1, 2]:
                Messages.error("Invalid Selection... Please try again.")
            else:
                return user_choice
        except ValueError:
            Messages.error("Invalid Input... Please enter a number.")



# ACCOUNT MENUS
def login_form() -> str:
    Messages.title("Login")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if not username or not password:
        Messages.error("Username and Password cannot be empty.")
        return login_form()

    return username, password
