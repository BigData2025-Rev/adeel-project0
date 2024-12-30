import sys
import menu
import account
import banking
from colors import Messages

def main():
    # CURRENT AUTHENTICATED USER
    current_user = ""

    # MENU TITLE
    Messages.title("Simple Bank")

    # MENU LOOP
    while True: 
        main_menu_option = menu.main_menu()

        # MAIN MENU SELECT
        if main_menu_option == 1:
            current_user = account.log_in()
        elif main_menu_option == 2:
            current_user = account.register()
        else:
            Messages.standard("Have a good day!")
            sys.exit()
        
        # IF AUTHENTICATED -> BANK MENU
        # ELSE -> BACK TO MAIN MENU
        if current_user:
            while True:
                bank_user_option = menu.bank_menu()
                if bank_user_option == 1:
                    banking.view(current_user)
                    Messages.pause()
                elif bank_user_option == 2:
                    banking.deposit(current_user)
                    Messages.pause()
                elif bank_user_option == 3:
                    banking.withdraw(current_user)
                    Messages.pause()
                elif bank_user_option == 4:
                    banking.transfer(current_user)
                    Messages.pause()
                elif (bank_user_option == 5):
                    Messages.standard("Returning to main menu...")
                    break
        elif current_user is None:
            pass
        else:
            Messages.error("Unknown Error, exiting...")
            sys.exit()

main()
