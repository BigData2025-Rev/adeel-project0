from account import load_accounts, save_account
from menu import account_select_menu, amount_deposit_menu, amount_withdraw_menu, transfer_multaccounts_menu, amount_transfer_menu
from colors import Messages

def view(username):
    accounts = load_accounts()
    user_account = accounts[username]["accounts"]

    Messages.title("Balance")

    if not user_account:
        Messages.error("No accounts found...")
    else:
        for account_type, account_data in user_account.items():
            balance = account_data.get("balance", 0.0) 
            print(f"{account_type.upper()}: ${balance:.2f}")
    Messages.end_message()

def deposit(username):
    accounts = load_accounts()
    user_account = accounts[username]["accounts"]

    account_list = list(user_account.keys())

    Messages.title("Deposit")

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

    Messages.title("Withdraw")

    selected = account_select_menu(account_list)
    amount = amount_withdraw_menu(balance)

    user_account[selected]["balance"] -= amount

    save_account(accounts)
    new_balance = user_account[selected]["balance"]
    print(f"Successfully withdrew ${amount:.2f} from your {selected.upper()} account.\nYour new {selected.upper()} balance is ${new_balance:.2f}")
    Messages.end_message()

def transfer(username):
    accounts = load_accounts()
    user_account = accounts[username]["accounts"]

    Messages.title("Transfer")

    if (len(user_account) > 1):
        transfer_account_choice = transfer_multaccounts_menu()
    else:
        transfer_account_choice = 2
    
    if (transfer_account_choice == 1):
        account_list = list(user_account.keys())
        selected = account_select_menu(account_list)
        balance = user_account[selected]["balance"]

        print(f"The current balance of your {selected.capitalize()} account is: ${balance:.2f}")

        amount = amount_transfer_menu(balance)

        user_account[selected]["balance"] -= amount

        if selected == "checking":
            user_account["savings"]["balance"] += amount
            destination = "savings"
            origin_new_balance = user_account[selected]["balance"]
            destination_new_balance = user_account["savings"]["balance"]
        else:
            user_account["checking"]["balance"] += amount
            destination = "checking"
            origin_new_balance = int(user_account[selected]["balance"])
            destination_new_balance = int(user_account["checking"]["balance"])
        
        save_account(accounts)

        print(
            f"Successfully transferred ${amount:.2f} from your {selected.upper()} account to your {destination.upper()} account.\n"
            f"Your new {selected.upper()} balance is ${origin_new_balance:.2f}\n"
            f"Your new {destination.upper()} balance is ${destination_new_balance:.2f}"
        )
    else:
        pass
