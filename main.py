import Authentication
import Engine

def menu():
    current_balance = 5000  
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

    if not Authentication.verify_pin():
        return

    while True:
        print(f"\n{MAGENTA}╔" + "═" * 28 + "╗")
        print(f"║{'🏦 DIGITAL ATM MENU 🪙🏧' : ^28}║ ")
        print("╠" + "═" * 28 + "╣")
        print(f"║ {CYAN}1. View Balance🪙{MAGENTA}           ║")
        print(f"║ {CYAN}2. Withdraw Cash💴{MAGENTA}          ║")
        print(f"║ {CYAN}3. Deposit Funds💰{MAGENTA}          ║")
        print(f"║ {CYAN}4. Mini Statement📜{MAGENTA}         ║")
        print(f"║ {CYAN}5. Secure Logout‼️{MAGENTA}          ║")
        print("╚" + "═" * 28 + f"╝ {RESET}")
        
        choice = input(f"\033[93m👉 Select option (1-5): \033[0m").strip()

        if choice == '1':
            print(f"\n\033[92m⭐ Your Current Balance: ₹{current_balance:,.2f}\033[0m")
        elif choice == '2':
            current_balance = Engine.withdraw(current_balance)
        elif choice == '3':
            current_balance = Engine.deposit(current_balance)
        elif choice == '4':
            Engine.show_statement()
        elif choice == '5':
            print(f"\n\033[95m✨ Thank you for using Digital ATM. Goodbye!\033[0m\n")
            break 
        else:
            print("\n\033[91m⚠️  Invalid Choice. Try again.\033[0m")

if __name__ == "__main__":
    menu()