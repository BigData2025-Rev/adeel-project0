from account import load_accounts, save_account
from menu import account_select_menu, amount_deposit_menu, amount_withdraw_menu
from colors import Messages

def view(username):
    accounts = load_accounts()
    user_account = accounts[username]["accounts"]

    if not user_account:
        Messages.error("No accounts found...")
    else:
        Messages.title("Accounts")
        for account_type, account_data in user_account.items():
            balance = account_data.get("balance", 0.0) 
            print(f"{account_type.upper()}: ${balance:.2f}")
            Messages.end_message()

def deposit(username):
    accounts = load_accounts()
    user_account = accounts[username]["accounts"]

    account_list = list(user_account.keys())

    selected = account_select_menu(account_list)
    amount = amount_deposit_menu()

    user_account[selected]["balance"] += amount

    save_account(accounts)
    new_balance = user_account[selected]["balance"]
    print(f"Successfully deposited ${amount:.2f} to your {selected.upper()} account.\nYour new {selected.upper()} balance is ${new_balance:.2f}")
    Messages.end_message()

def withdraw(username):
    accounts = load_accounts()
    user_account = accounts[username]["accounts"]
    balance = int(user_account[selected]["balance"])
    account_list = list(user_account.keys())

    selected = account_select_menu(account_list)
    amount = amount_withdraw_menu(balance)

    user_account[selected]["balance"] -= amount

    save_account(accounts)
    new_balance = user_account[selected]["balance"]
    print(f"Successfully withdrew ${amount:.2f} from your {selected} account.\nYour new {selected} balance is ${new_balance:.2f}")
    Messages.end_message()

