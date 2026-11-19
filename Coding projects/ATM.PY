current_balance = 10000

def start(): 
    print("ATM simulator")
    print("Menu")
    print("1. check balance\n2. deposit\n3. withdraw \n")
    current_balance = 10000

def option1(): 
    print("\n\n\n\nyour balance")
    print(current_balance)
    print ("\n enter 1 to return to menu")
    opt2 = int(input("(1): "))
    if opt2 == 1: 
        start()
    else: 
        error()

def option2(): 
    print("\n\n\n\nHow much would you like to deposit?")
    dep = int(input(": "))
    current_balance += dep
    print(f"\n\nYour Current Balance is\n${current_balance}")
    print ("\n enter 1 to return to menu")
    opt3 = int(input("(1): "))
    if opt3 == 1: 
        start()
    else: 
        error()

def option3(): 
    print("\n\n\n\nHow much would you like to withdraw?")
    wid = int(input(": "))
    if current_balance > wid:
        current_balance -= wid
        print(f"\n\nYour current balance is ${current_balance} ")
    elif current_balance < wid:
        print("\n\nwithdrawals exceed the balance")
    print ("\n enter 1 to return to menu")
    opt4 = int(input("(1): "))
    if opt4 == 1: 
        start()
    else: 
        error()

def error(): 
    print("error")

start()
opt = int(input("(1/2/3): "))
if opt == 1: 
    option1()
elif opt == 2: 
    option2()
elif opt == 3: 
    option3()
elif opt == 4: 
    start()
else:
    error()
    
# def option1(): 
#     print("\n\n\n\nyour balance")
#     print(current_balance)

# def option2(): 
#     print("\n\n\n\nHow much would you like to deposit?")
#     dep = int(input(": "))
#     current_balance += dep
#     print(f"\n\nYour Current Balance is\n${current_balance}")

# def option3(): 
#     print("\n\n\n\nHow much would you like to withdraw?")
#     wid = int(input(": "))
#     if current_balance > wid:
#         current_balance -= wid
#         print(f"\n\nYour current balance is ${current_balance} ")
#     elif current_balance < wid:
#         print("\n\nwithdrawals exceed the balance")

# def error(): 
#     print("error")