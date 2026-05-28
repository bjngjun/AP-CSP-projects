#bingjun
#atm

balance = 100

#functions
def main():
    print("please choose a option:")
    print("1: total balance")
    print("2: withdraw")
    print("3: deposit")
    choice = int(input())
    if choice == 1:
        total()
        main()
    elif choice == 2:
        withdraw()
        main()
    elif choice == 3:
        deposit()
        main()
    else:
        print("please choose a valid choice")
        main()
def total():
    global balance
    print("")
    print(f"balance: ${balance}")
    print("")

def withdraw():
    global balance
    amount = int(input("how much would you like to withdraw?: "))
    balance = balance - int(amount)
    print("")
    print(f"withdrew ${amount}")
    print("")

def deposit():
    global balance
    amount = int(input("how much would you like to deposit?: "))
    balance = balance + int(amount)
    print("")
    print(f"deposited ${amount}")
    print("")


#main
main()
