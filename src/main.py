def main_menu() -> int:
    while(True):
        print("Menu")
        print("================")
        print("1. Log In")
        print("2. Create Account")
        print("3. Exit")
        login_screen_select = input("Selection: ")

        if (int(login_screen_select) not in [1, 2, 3]):
            print("Invalid Selection... Please try again.")
            continue;
        else:
            return int(login_screen_select)


def main():
    print("Welcome to the Simple Bank app")

    main_menu_option = main_menu()

    print (main_menu_option)

main()