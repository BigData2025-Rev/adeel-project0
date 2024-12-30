class Color:
    RED = '\033[91m'
    END = '\033[0m'
    GREEN = '\033[32m'
    CYAN = '\033[36m'

class Messages:
    def error(message: str):
        print("\n"  + Color.RED + message + Color.END + "\n" )
    def success(message: str):
        print("\n" + Color.GREEN + message + Color.END + "\n" )
    def standard(message: str):
        print("\n"  + Color.CYAN + message + Color.END + "\n" )
    def title(message: str):
        print("================")
        print(message.center(16))
        print("================")
    def pause():
        input('Press ENTER to continue... ')
    def end_message():
        print("================\n")