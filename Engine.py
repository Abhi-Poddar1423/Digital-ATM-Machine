import datetime

G = "\033[92m"  
R = "\033[91m"  
Y = "\033[93m"  
B = "\033[94m"  
C = "\033[96m"  
RESET = "\033[0m"

def record_transaction(trans_type, amount, balance):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("transactions.txt", "a", encoding="utf-8") as f:
        f.write(f"{now} | {trans_type:<10} | Amt: ₹{amount:<8,.2f} | Bal: ₹{balance:,.2f}\n")

def deposit(balance):
    try:
        amount = float(input(f"\n{Y}💰 Enter deposit amount: ₹{RESET}"))
        if amount > 0:
            balance += amount
            print(f"{G}✅ SUCCESS: ₹{amount:,.2f} credited to your account.{RESET}")
            record_transaction("DEPOSIT", amount, balance)
        else:
            print(f"{R}❌ ERROR: Invalid Amount.{RESET}")
    except ValueError:
        print(f"{R}❌ ERROR: Please enter numbers only.{RESET}")
    return balance

def withdraw(balance):
    try:
        amount = float(input(f"\n{Y}💸 Enter withdrawal amount: ₹{RESET}"))
        if 0 < amount <= balance:
            balance -= amount
            print(f"{G}✅ SUCCESS: Please collect your cash.{RESET}")
            record_transaction("WITHDRAWAL", amount, balance)
        elif amount > balance:
            print(f"{R}⚠️  DENIED: Insufficient Funds.{RESET}")
        else:
            print(f"{R}❌ ERROR: Invalid Amount.{RESET}")
    except ValueError:
        print(f"{R}❌ ERROR: Please enter numbers only.{RESET}")
    return balance

def show_statement():
    print(f"\n{B}═" * 60)
    print(f"{'📜 MINI STATEMENT' : ^60}")
    print("═" * 60 + f"{RESET}")
    print(f"{C}{'DATE & TIME' : <18} | {'TYPE' : <10} | {'AMOUNT' : <12} | {'BALANCE'}{RESET}")
    
    try:
        with open("transactions.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
            
                if "DEPOSIT" in line:
                    print(f"{G}{line.strip()}{RESET}")
                else:
                    print(f"{R}{line.strip()}{RESET}")
    except FileNotFoundError:
        print(f"{Y}No transactions recorded yet.{RESET}")
    print(f"{B}═" * 60 + f"{RESET}")