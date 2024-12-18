def create_account():
    account_number = input("Enter your desired account number: ")
    account_holder_name = input("Enter your name: ")
    initial_deposit = eval(input("Enter your initial deposit amount: "))
    return account_number, account_holder_name, initial_deposit

def deposit(balance):
    deposit_amount = eval(input("Enter the amount to deposit: "))
    balance += deposit_amount
    dep = round(deposit_amount,-1)

    print("Your deposit breakdown in peso denomination:")
    onek = dep//1000
    k = dep % 1000
    print(onek, "- 1000")

    fiveh = k//500
    fh = k%500
    print(fiveh,"- 500")

    twoh = fh//200
    th = fh%200
    print(twoh,"- 200")

    oneh = th//100
    oh = th%100
    print(oneh,"- 100")

    fifty = oh//50
    ft = oh%50
    print(fifty,"- 50")

    twenty = ft//20
    tw = ft%20
    print(twenty,"- 20")

    ten = tw//10
    t= tw%10
    print(ten,"- 10")

    five = t//5
    f = t%5
    print(five,"- 5")

    one = f//1
    print(one,"- 1")
    o = f%1

    print("Your deposit is successful!")
    return balance

def withdraw(balance):
    withdraw_amount = eval(input("Enter the amount to withdraw: "))
    if withdraw_amount > balance:
        print("Insufficient funds!")
    else:
        balance -= withdraw_amount
        print("Withdrawal successful!")
    return balance

def check_balance(balance):
    print("Your current balance is:", balance)

def main():
    account_number, account_holder_name, balance = create_account()
    print("\nAccount created successfully!")
    print("Account Number:", account_number)
    print("Account Holder:", account_holder_name)

    while True:
        print("\n What do you want to do?\n 1 - Deposit\n 2 - Withraw\n 3 - Check Current Balance\n 4 - Exit\n" )

        choice = int(input("Enter your choice: "))

        if choice == 1:
            deposit(balance)
        elif choice == 2:
            balance = withdraw(balance)
        elif choice == 3:
            check_balance(balance)
        elif choice == 4:
            print("Thank you for using our banking system!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()