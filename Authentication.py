
def verify_pin():
    CYAN = "\033[96m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    correct_pin = "1234"
    
    print(f"\n{CYAN}🔒 " + "─" * 28 + f" 🔒{RESET}")
    print(f"{CYAN}{'SECURE LOGIN' : ^30}{RESET}")
    print(f"{CYAN}" + "─" * 30 + f"{RESET}")
    
    entered_pin = input(f"{YELLOW}👉 Enter 4-Digit PIN: {RESET}").strip()
    
    if entered_pin == correct_pin:
        print(f"\n{GREEN}✅ Access Granted. Welcome back!{RESET}")
        return True
    else:
        print(f"\n{RED}❌ [ERROR] Incorrect PIN. Access Denied.{RESET}")
        return False