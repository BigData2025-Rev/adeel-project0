from colors import Color

def main_menu() -> int:
    while True:
        print("Menu")
        print("================")
        print("1. Log In")
        print("2. Create Account")
        print("3. Exit")
        login_screen_select = input("\nSelection: ")

        try:
            if (int(login_screen_select) not in [1, 2, 3]):
                print('\n' + Color.RED + "Invalid Selection... Please try again."
                + Color.END + '\n')
                continue
            return int(login_screen_select)
        except ValueError:
            print('\n' + Color.RED + "Invalid Input... Please enter a number." + Color.END + '\n')