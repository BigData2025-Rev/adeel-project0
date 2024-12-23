import sys
import menu
import account

def main():
    print("Welcome to the Simple Bank app")

    main_menu_option = menu.main_menu()

    if main_menu_option == 1:
        print("Logging in...")
        account.log_in()
    elif main_menu_option == 2:
        print("Register...")
        account.register()
    else:
        print("\nHave a good day!\n")
        sys.exit()

main()
