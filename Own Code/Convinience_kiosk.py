def gcash(Cash_In):
    GcashNum = int(input("What is your Gcash Number: "))
    GcashIn = eval(input("Enter the amount of cash in: "))
    print(f"You are about to cash-in an amount of {GcashIn}")
    warning = input(f"This transaction will charge you an additional 5% of the amount, do you want to proceed?(yes/no):  ")
    Ppayment = GcashIn * 0.05
    Total_payment = Ppayment + GcashIn
    Isrepeat = True

    if warning.lower() == "yes": 
        while Isrepeat == True:
            print(f"Your total amount to pay is {Total_payment}")
            GcashPayment = eval(input("Payment amount: "))
            PChange = GcashPayment - Cash_In
            Pround = round(PChange,3)

            if GcashPayment >= Total_payment:
                print(f"Your Gcash number: {GcashNum} has been credited an amount of {GcashIn}")
                print("Thank you for using the system")
                break
                Isrepeat= False

            else:
                print(f"Sorry, your payment amount is not enough, please pay an amount of {Total_payment}")
                continue
    else: 
        print("Thank you for using the system")

    return

def maya(Cash_In):
    MayaNum = int(input("What is your Maya Number: "))
    amount = eval(input("Enter the amount of cash in: "))
    print(f"You are about to cash-in an amount of {amount}")
    warning = input(f"This transaction will charge you an additional 5% of the amount, do you want to proceed?(yes/no):  ")
    Ppayment = amount * 0.05
    Total_payment = Ppayment + amount
    Isrepeat = True

    if warning.lower() == "yes": 
        while Isrepeat == True:

            print(f"Your total amount to pay is {Total_payment}")
            MayaPayment = eval(input("Payment amount: "))
            PChange = MayaPayment - Cash_In
            Pround = round(PChange,3)

            if MayaPayment >= Total_payment:
                print(f"Your Maya number: {MayaNum} has been credited an amount of {amount}")
                print("Thank you for using the system")
                break
                Isrepeat= False

            else:
                print(f"Sorry, your payment amount is not enough, please pay an amount of {Total_payment}")
                continue
    else: 
        print("Thank you for using the system")

    return

def paypal(Cash_In):
    PaypalNum = int(input("What is your PayPal Number: "))
    amount = eval(input("Enter the amount of cash in: "))
    print(f"You are about to cash-in an amount of {amount}")
    warning = input(f"This transaction will charge you an additional 5% of the amount, do you want to proceed?(yes/no):  ")
    Ppayment = amount * 0.05
    Total_payment = Ppayment + amount
    Isrepeat = True

    if warning.lower() == "yes": 
        while Isrepeat == True:

            print(f"Your total amount to pay is {Total_payment}")
            PaypalPayment = eval(input("Payment amount: "))
            PChange = PaypalPayment - Cash_In
            Pround = round(PChange,3)

            if PaypalPayment >= Total_payment:
                print(f"Your PayPal number: {PaypalNum} has been credited an amount of {amount}")
                print("Thank you for using the system")
                break
                Isrepeat= False

            else:
                print(f"Sorry, your payment amount is not enough, please pay an amount of {Total_payment}")
                continue
    else: 
        print("Thank you for using the system")

    return

def shopeepay(Cash_In):
    ShopeeNum = int(input("What is your ShopeePay Number: "))
    amount = eval(input("Enter the amount of cash in: "))
    print(f"You are about to cash-in an amount of {amount}")
    warning = input(f"This transaction will charge you an additional 5% of the amount, do you want to proceed?(yes/no):  ")
    Ppayment = amount * 0.05
    Total_payment = Ppayment + amount
    Isrepeat = True

    if warning.lower() == "yes": 
        while Isrepeat == True:

            print(f"Your total amount to pay is {Total_payment}")
            ShopeePayment = eval(input("Payment amount: "))
            PChange = ShopeePayment - Cash_In
            Pround = round(PChange,3)

            if ShopeePayment >= Total_payment:
                print(f"Your ShopeePay number: {ShopeeNum} has been credited an amount of {amount}")
                print("Thank you for using the system")
                break
                Isrepeat= False

            else:
                print(f"Sorry, your payment amount is not enough, please pay an amount of {Total_payment}")
                continue
    else: 
        print("Thank you for using the system")

    return

def tala(Cash_In):
    TalaNum = int(input("What is your Tala account number: "))
    amount = eval(input("Enter the amount of cash in: "))
    print(f"You are about to cash-in an amount of {amount}")
    warning = input(f"This transaction will charge you an additional 5% of the amount, do you want to proceed?(yes/no):  ")
    Ppayment = amount * 0.05
    Total_payment = Ppayment + amount
    Isrepeat = True

    if warning.lower() == "yes": 
        while Isrepeat == True:

            print(f"Your total amount to pay is {Total_payment}")
            TalaPayment = eval(input("Payment amount: "))
            PChange = TalaPayment - Cash_In
            Pround = round(PChange,3)

            if TalaPayment >= Total_payment:
                print(f"Your Tala account number: {TalaNum} has been credited an amount of {amount}")
                print("Thank you for using the system")
                break
                Isrepeat= False

            else:
                print(f"Sorry, your payment amount is not enough, please pay an amount of {Total_payment}")
                continue
    else: 
        print("Thank you for using the system")

    return

def tnt(Load):
    print("Your service provider is Talk n text")
    num = int(input("Enter your mobile number: "))
    amount = eval(input("Enter the amount of load: "))
    warning = input(f"This transaction will charge you an additional 5% of the amount, do you want to proceed?(yes/no):  ")
    Ppayment = amount * 0.05
    Total_payment = Ppayment + amount
    isrepeat = True

    if warning.lower() == "yes": 

        while isrepeat == True:
            
            print(f"Your total amount to pay is {Total_payment}")
            print(Total_payment)
            payment = eval(input("Payment amount: "))
            Fpayment = payment - Total_payment
            Pround = round(Fpayment, 3)
            

            if payment >= Total_payment:
                print(f"You mobile number {num} has been credited load amount of {amount} pesos")
                print(f"Your change is {Pround} pesos")
                print("Thank you for using DX kiosk")
                break
                isrepeat = False 
            else:
                print(f"Sorry, your payment amount is not enough, please pay an amount of {Total_payment} pesos")
                continue
    else: 
        print("Thank you for using the system")
            
    return 

def globe(Load):
    print("Your service provider is Globe")
    num = int(input("Enter your mobile number: "))
    amount = eval(input("Enter the amount of load: "))
    warning = input(f"This transaction will charge you an additional 5% of the amount, do you want to proceed?(yes/no):  ")
    Ppayment = amount * 0.05
    Total_payment = Ppayment + amount
    isrepeat = True

    if warning.lower() == "yes": 

        while isrepeat == True:
            
            print(f"Your total amount to pay is {Total_payment}")
            print(Total_payment)
            payment = eval(input("Payment amount: "))
            Fpayment = payment - Total_payment
            Pround = round(Fpayment, 3)
            

            if payment >= Total_payment:
                print(f"You mobile number {num} has been credited load amount of {amount} pesos")
                print(f"Your change is {Pround} pesos")
                print("Thank you for using DX kiosk")
                break
                isrepeat = False 

            else:
                print(f"Sorry, your payment amount is not enough, please pay an amount of {Total_payment} pesos")
                continue
    else: 
        print("Thank you for using the system")

    return 

def tm(Load):
    print("Your service provider is TM")
    num = int(input("Enter your mobile number: "))
    amount = eval(input("Enter the amount of load: "))
    warning = input(f"This transaction will charge you an additional 5% of the amount, do you want to proceed?(yes/no):  ")
    Ppayment = amount * 0.05
    Total_payment = Ppayment + amount
    isrepeat = True

    if warning.lower() == "yes": 

        while isrepeat == True:
            
            print(f"Your total amount to pay is {Total_payment}")
            print(Total_payment)
            payment = eval(input("Payment amount: "))
            Fpayment = payment - Total_payment
            Pround = round(Fpayment, 3)
            

            if payment >= Total_payment:
                print(f"You mobile number {num} has been credited load amount of {amount} pesos")
                print(f"Your change is {Pround} pesos")
                print("Thank you for using DX kiosk")
                break
                isrepeat = False 

            else:
                print(f"Sorry, your payment amount is not enough, please pay an amount of {Total_payment} pesos")
                continue
    else: 
        print("Thank you for using the system")

    return 

def smart(Load):
    print("Your service provider is Smart")
    num = int(input("Enter your mobile number: "))
    amount = eval(input("Enter the amount of load: "))
    warning = input(f"This transaction will charge you an additional 5% of the amount, do you want to proceed?(yes/no):  ")
    Ppayment = amount * 0.05
    Total_payment = Ppayment + amount
    isrepeat = True

    if warning.lower() == "yes": 

        while isrepeat == True:
            
            print(f"Your total amount to pay is {Total_payment}")
            print(Total_payment)
            payment = eval(input("Payment amount: "))
            Fpayment = payment - Total_payment
            Pround = round(Fpayment, 3)
            

            if payment >= Total_payment:
                print(f"You mobile number {num} has been credited load amount of {amount} pesos")
                print(f"Your change is {Pround} pesos")
                print("Thank you for using DX kiosk")
                break
                isrepeat = False 

            else:
                print(f"Sorry, your payment amount is not enough, please pay an amount of {Total_payment} pesos")
                continue
    else: 
        print("Thank you for using the system")

    return 

def dito(Load):
    print("Your service provider is Dito")
    num = int(input("Enter your mobile number: "))
    amount = eval(input("Enter the amount of load: "))
    warning = input(f"This transaction will charge you an additional 5% of the amount, do you want to proceed?(yes/no):  ")
    Ppayment = amount * 0.05
    Total_payment = Ppayment + amount
    isrepeat = True

    if warning.lower() == "yes": 

        while isrepeat == True:
            
            print(f"Your total amount to pay is {Total_payment}")
            print(Total_payment)
            payment = eval(input("Payment amount: "))
            Fpayment = payment - Total_payment
            Pround = round(Fpayment, 3)
            

            if payment >= Total_payment:
                print(f"You mobile number {num} has been credited load amount of {amount} pesos")
                print(f"Your change is {Pround} pesos")
                print("Thank you for using DX kiosk")
                break
                isrepeat = False 

            else:
                print(f"Sorry, your payment amount is not enough, please pay an amount of {Total_payment} pesos")
                continue
    else: 
        print("Thank you for using the system")

    return 

def sun(Load):
    print("Your service provider is Sun")
    num = int(input("Enter your mobile number: "))
    amount = eval(input("Enter the amount of load: "))
    warning = input(f"This transaction will charge you an additional 5% of the amount, do you want to proceed?(yes/no):  ")
    Ppayment = amount * 0.05
    Total_payment = Ppayment + amount
    isrepeat = True

    if warning.lower() == "yes": 

        while isrepeat == True:
            
            print(f"Your total amount to pay is {Total_payment}")
            print(Total_payment)
            payment = eval(input("Payment amount: "))
            Fpayment = payment - Total_payment
            Pround = round(Fpayment, 3)
            

            if payment >= Total_payment:
                print(f"You mobile number {num} has been credited load amount of {amount} pesos")
                print(f"Your change is {Pround} pesos")
                print("Thank you for using DX kiosk")
                break
                isrepeat = False 

            else:
                print(f"Sorry, your payment amount is not enough, please pay an amount of {Total_payment} pesos")
                continue
    else: 
        print("Thank you for using the system")

    return 


def quezelco(electrical):
    print("Welcome!")
    AccNum = input("Enter your account number:  ")
    AccName = input("Enter the account name:  ")
    BillNum = input("Enter your bill number:  ")
    BillAmount = eval(input("Enter the bill amount:  "))
    warning = input(f"This transaction will charge you an additional 1% of the amount, do you want to proceed?(yes/no):  ")
    Ppayment = BillAmount * 0.01
    Total_payment = Ppayment + BillAmount
    Tpayment = round(Total_payment,3)

    isrepeat = True
    
    if warning.lower() == "yes": 

        while isrepeat == True:
            
            print(f"Your total amount to pay is {Tpayment}")
            payment = eval(input("Payment amount: "))
            Fpayment = payment - Total_payment
            Pround = round(Fpayment, 3)

            if payment >= Total_payment:
                print(f"Your Bill number {BillNum} that amounted to {Total_payment} pesos has been succesfully paid")
                print(f"Your change is {Pround} pesos")
                print("Thank you for using DX kiosk")
                break
                isrepeat = False 

            else:

                print(f"Sorry, your payment amount is not enough, please pay an amount of {Total_payment} pesos")
                continue
    else: 
        print("Thank you for using the system")

    return 


def lagetec(electrical):
    print("Welcome!")
    AccNum = input("Enter your account number:  ")
    AccName = input("Enter the account name:  ")
    BillNum = input("Enter your bill number:  ")
    BillAmount = eval(input("Enter the bill amount:  "))
    warning = input(f"This transaction will charge you an additional 1% of the amount, do you want to proceed?(yes/no):  ")
    Ppayment = BillAmount * 0.01
    Total_payment = Ppayment + BillAmount
    Tpayment = round(Total_payment,3)

    isrepeat = True
    
    if warning.lower() == "yes": 

        while isrepeat == True:
            
            print(f"Your total amount to pay is {Tpayment}")
            payment = eval(input("Payment amount: "))
            Fpayment = payment - Total_payment
            Pround = round(Fpayment, 3)

            if payment >= Total_payment:
                print(f"Your Bill number {BillNum} that amounted to {Total_payment} pesos has been succesfully paid")
                print(f"Your change is {Pround} pesos")
                print("Thank you for using DX kiosk")
                break
                isrepeat = False 

            else:

                print(f"Sorry, your payment amount is not enough, please pay an amount of {Total_payment} pesos")
                continue
    else: 
        print("Thank you for using the system")

    return 

def batelec(electrical):
    print("Welcome!")
    AccNum = input("Enter your account number:  ")
    AccName = input("Enter the account name:  ")
    BillNum = input("Enter your bill number:  ")
    BillAmount = eval(input("Enter the bill amount:  "))
    warning = input(f"This transaction will charge you an additional 1% of the amount, do you want to proceed?(yes/no):  ")
    Ppayment = BillAmount * 0.01
    Total_payment = Ppayment + BillAmount
    Tpayment = round(Total_payment,3)

    isrepeat = True
    
    if warning.lower() == "yes": 

        while isrepeat == True:
            
            print(f"Your total amount to pay is {Tpayment}")
            payment = eval(input("Payment amount: "))
            Fpayment = payment - Total_payment
            Pround = round(Fpayment, 3)

            if payment >= Total_payment:
                print(f"Your Bill number {BillNum} that amounted to {Total_payment} pesos has been succesfully paid")
                print(f"Your change is {Pround} pesos")
                print("Thank you for using DX kiosk")
                break
                isrepeat = False 

            else:

                print(f"Sorry, your payment amount is not enough, please pay an amount of {Total_payment} pesos")
                continue
    else: 
        print("Thank you for using the system")

    return 


def meralco(electrical):
    print("Welcome!")
    AccNum = input("Enter your account number:  ")
    AccName = input("Enter the account name:  ")
    BillNum = input("Enter your bill number:  ")
    BillAmount = eval(input("Enter the bill amount:  "))
    warning = input(f"This transaction will charge you an additional 1% of the amount, do you want to proceed?(yes/no):  ")
    Ppayment = BillAmount * 0.01
    Total_payment = Ppayment + BillAmount
    Tpayment = round(Total_payment,3)

    isrepeat = True
    
    if warning.lower() == "yes": 

        while isrepeat == True:
            
            print(f"Your total amount to pay is {Tpayment}")
            payment = eval(input("Payment amount: "))
            Fpayment = payment - Total_payment
            Pround = round(Fpayment, 3)

            if payment >= Total_payment:
                print(f"Your Bill number {BillNum} that amounted to {Total_payment} pesos has been succesfully paid")
                print(f"Your change is {Pround} pesos")
                print("Thank you for using DX kiosk")
                break
                isrepeat = False 

            else:
                print(f"Sorry, your payment amount is not enough, please pay an amount of {Total_payment} pesos")
                continue
    else: 
        print("Thank you for using the system")

    return 

def angeles(water):
    print("Welcome!")
    AccNum = input("Enter your account number:  ")
    AccName = input("Enter the account name:  ")
    BillNum = input("Enter your bill number:  ")
    BillAmount = eval(input("Enter the bill amount:  "))
    warning = input(f"This transaction will charge you an additional 1% of the amount, do you want to proceed?(yes/no):  ")
    Ppayment = BillAmount * 0.01
    Total_payment = Ppayment + BillAmount
    Tpayment = round(Total_payment,3)

    isrepeat = True
    
    if warning.lower() == "yes": 

        while isrepeat == True:
            
            print(f"Your total amount to pay is {Tpayment}")
            payment = eval(input("Payment amount: "))
            Fpayment = payment - Total_payment
            Pround = round(Fpayment, 3)

            if payment >= Total_payment:
                print(f"Your Bill number {BillNum} that amounted to {Total_payment} pesos has been succesfully paid")
                print(f"Your change is {Pround} pesos")
                print("Thank you for using DX kiosk")
                break
                isrepeat = False 

            else:

                print(f"Sorry, your payment amount is not enough, please pay an amount of {Total_payment} pesos")
                continue
    return 

def bocaue(water):
    print("Welcome!")
    AccNum = input("Enter your account number:  ")
    AccName = input("Enter the account name:  ")
    BillNum = input("Enter your bill number:  ")
    BillAmount = eval(input("Enter the bill amount:  "))
    warning = input(f"This transaction will charge you an additional 1% of the amount, do you want to proceed?(yes/no):  ")
    Ppayment = BillAmount * 0.01
    Total_payment = Ppayment + BillAmount
    Tpayment = round(Total_payment,3)

    isrepeat = True
    
    if warning.lower() == "yes": 

        while isrepeat == True:
            
            print(f"Your total amount to pay is {Tpayment}")
            payment = eval(input("Payment amount: "))
            Fpayment = payment - Total_payment
            Pround = round(Fpayment, 3)

            if payment >= Total_payment:
                print(f"Your Bill number {BillNum} that amounted to {Total_payment} pesos has been succesfully paid")
                print(f"Your change is {Pround} pesos")
                print("Thank you for using DX kiosk")
                break
                isrepeat = False 

            else:

                print(f"Sorry, your payment amount is not enough, please pay an amount of {Total_payment} pesos")
                continue
    return 

def calamba(water):
    print("Welcome!")
    AccNum = input("Enter your account number:  ")
    AccName = input("Enter the account name:  ")
    BillNum = input("Enter your bill number:  ")
    BillAmount = eval(input("Enter the bill amount:  "))
    warning = input(f"This transaction will charge you an additional 1% of the amount, do you want to proceed?(yes/no):  ")
    Ppayment = BillAmount * 0.01
    Total_payment = Ppayment + BillAmount
    Tpayment = round(Total_payment,3)

    isrepeat = True
    
    if warning.lower() == "yes": 

        while isrepeat == True:
            
            print(f"Your total amount to pay is {Tpayment}")
            payment = eval(input("Payment amount: "))
            Fpayment = payment - Total_payment
            Pround = round(Fpayment, 3)

            if payment >= Total_payment:
                print(f"Your Bill number {BillNum} that amounted to {Total_payment} pesos has been succesfully paid")
                print(f"Your change is {Pround} pesos")
                print("Thank you for using DX kiosk")
                break
                isrepeat = False 

            else:
                print(f"Sorry, your payment amount is not enough, please pay an amount of {Total_payment} pesos")
                continue
    return 

def catanauan(water):
    print("Welcome!")
    AccNum = input("Enter your account number:  ")
    AccName = input("Enter the account name:  ")
    BillNum = input("Enter your bill number:  ")
    BillAmount = eval(input("Enter the bill amount:  "))
    warning = input(f"This transaction will charge you an additional 1% of the amount, do you want to proceed?(yes/no):  ")
    Ppayment = BillAmount * 0.01
    Total_payment = Ppayment + BillAmount
    Tpayment = round(Total_payment,3)

    isrepeat = True
    
    if warning.lower() == "yes": 

        while isrepeat == True:
            
            print(f"Your total amount to pay is {Tpayment}")
            payment = eval(input("Payment amount: "))
            Fpayment = payment - Total_payment
            Pround = round(Fpayment, 3)

            if payment >= Total_payment:
                print(f"Your Bill number {BillNum} that amounted to {Total_payment} pesos has been succesfully paid")
                print(f"Your change is {Pround} pesos")
                print("Thank you for using DX kiosk")
                break
                isrepeat = False 

            else:
                print(f"Sorry, your payment amount is not enough, please pay an amount of {Total_payment} pesos")
                continue
    return 

def gumaca(water):
    print("Welcome!")
    AccNum = input("Enter your account number:  ")
    AccName = input("Enter the account name:  ")
    BillNum = input("Enter your bill number:  ")
    BillAmount = eval(input("Enter the bill amount:  "))
    warning = input(f"This transaction will charge you an additional 1% of the amount, do you want to proceed?(yes/no):  ")
    Ppayment = BillAmount * 0.01
    Total_payment = Ppayment + BillAmount
    Tpayment = round(Total_payment,3)

    isrepeat = True
    
    if warning.lower() == "yes": 

        while isrepeat == True:
            
            print(f"Your total amount to pay is {Tpayment}")
            payment = eval(input("Payment amount: "))
            Fpayment = payment - Total_payment
            Pround = round(Fpayment, 3)

            if payment >= Total_payment:
                print(f"Your Bill number {BillNum} that amounted to {Total_payment} pesos has been succesfully paid")
                print(f"Your change is {Pround} pesos")
                print("Thank you for using DX kiosk")
                break
                isrepeat = False 

            else:
                print(f"Sorry, your payment amount is not enough, please pay an amount of {Total_payment} pesos")
                continue
    return 

def primewater(water):
    print("Welcome!")
    AccNum = input("Enter your account number:  ")
    AccName = input("Enter the account name:  ")
    BillNum = input("Enter your bill number:  ")
    BillAmount = eval(input("Enter the bill amount:  "))
    warning = input(f"This transaction will charge you an additional 1% of the amount, do you want to proceed?(yes/no):  ")
    Ppayment = BillAmount * 0.01
    Total_payment = Ppayment + BillAmount
    Tpayment = round(Total_payment,3)

    isrepeat = True
    
    if warning.lower() == "yes": 

        while isrepeat == True:
            
            print(f"Your total amount to pay is {Tpayment}")
            payment = eval(input("Payment amount: "))
            Fpayment = payment - Total_payment
            Pround = round(Fpayment, 3)

            if payment >= Total_payment:
                print(f"Your Bill number {BillNum} that amounted to {Total_payment} pesos has been succesfully paid")
                print(f"Your change is {Pround} pesos")
                print("Thank you for using DX kiosk")
                break
                isrepeat = False 

            else:

                print(f"Sorry, your payment amount is not enough, please pay an amount of {Total_payment} pesos")
                continue
                return 

def converge(internet):
    print("Welcome to PLDT portal")
    AccNum = input("Enter your account number:  ")
    BillNum = input("Enter your bill number:  ")
    BillAmount = eval(input("Enter the bill amount:  "))
    

    isrepeat = True

    while isrepeat == True:
            
        print(f"Your total amount to pay is {BillAmount}")
        payment = eval(input("Payment amount: "))
        change = payment - BillAmount

        if payment >= BillAmount:
            print(f"Your Bill number {BillNum} that amounted to {BillAmount} pesos has been succesfully paid")
            print(f"Your change is {change} pesos")
            print("Thank you for using DX kiosk")
            break
            isrepeat = False 

        else:

            print(f"Sorry, your payment amount is not enough, please pay an amount of {BillAmount} pesos")
            continue

    return 

def globe(internet):
    print("Welcome to PLDT portal")
    AccNum = input("Enter your account number:  ")
    BillNum = input("Enter your bill number:  ")
    BillAmount = eval(input("Enter the bill amount:  "))
    

    isrepeat = True

    while isrepeat == True:
            
        print(f"Your total amount to pay is {BillAmount}")
        payment = eval(input("Payment amount: "))
        change = payment - BillAmount

        if payment >= BillAmount:
            print(f"Your Bill number {BillNum} that amounted to {BillAmount} pesos has been succesfully paid")
            print(f"Your change is {change} pesos")
            print("Thank you for using DX kiosk")
            break
            isrepeat = False 

        else:

            print(f"Sorry, your payment amount is not enough, please pay an amount of {BillAmount} pesos")
            continue

    return 

def pldt(internet):
    print("Welcome to PLDT portal")
    AccNum = input("Enter your account number:  ")
    BillNum = input("Enter your bill number:  ")
    BillAmount = eval(input("Enter the bill amount:  "))
    

    isrepeat = True

    while isrepeat == True:
            
        print(f"Your total amount to pay is {BillAmount}")
        payment = eval(input("Payment amount: "))
        change = payment - BillAmount

        if payment >= BillAmount:
            print(f"Your Bill number {BillNum} that amounted to {BillAmount} pesos has been succesfully paid")
            print(f"Your change is {change} pesos")
            print("Thank you for using DX kiosk")
            break
            isrepeat = False 

        else:

            print(f"Sorry, your payment amount is not enough, please pay an amount of {BillAmount} pesos")
            continue

    return 

def skyfiber(internet):
    print("Welcome to PLDT portal")
    AccNum = input("Enter your account number:  ")
    BillNum = input("Enter your bill number:  ")
    BillAmount = eval(input("Enter the bill amount:  "))
    

    isrepeat = True

    while isrepeat == True:
            
        print(f"Your total amount to pay is {BillAmount}")
        payment = eval(input("Payment amount: "))
        change = payment - BillAmount

        if payment >= BillAmount:
            print(f"Your Bill number {BillNum} that amounted to {BillAmount} pesos has been succesfully paid")
            print(f"Your change is {change} pesos")
            print("Thank you for using DX kiosk")
            break
            isrepeat = False 

        else:

            print(f"Sorry, your payment amount is not enough, please pay an amount of {BillAmount} pesos")
            continue

    return 

def starlink(internet):
    print("Welcome to PLDT portal")
    AccNum = input("Enter your account number:  ")
    BillNum = input("Enter your bill number:  ")
    BillAmount = eval(input("Enter the bill amount:  "))
    

    isrepeat = True

    while isrepeat == True:
            
        print(f"Your total amount to pay is {BillAmount}")
        payment = eval(input("Payment amount: "))
        change = payment - BillAmount

        if payment >= BillAmount:
            print(f"Your Bill number {BillNum} that amounted to {BillAmount} pesos has been succesfully paid")
            print(f"Your change is {change} pesos")
            print("Thank you for using DX kiosk")
            break
            isrepeat = False 

        else:

            print(f"Sorry, your payment amount is not enough, please pay an amount of {BillAmount} pesos")
            continue

    return 

def ewallet(wallet):
    isrepeat = True
    while isrepeat == True: 

        print("Please select your E-Wallet services: \n 1 - Gcash \n 2 - Maya \n 3 - PayPal \n 4 - ShopeePay \n 5 - Tala app \n 6 - Exit")
        EWallet = eval(input("Please enter the number of your provider:  "))

        if EWallet == 1:
            gcash(0)
    
        elif EWallet == 2:
            maya(0)

        elif EWallet == 3:
            paypal(0)

        elif EWallet == 4:
            shopeepay(0)

        elif EWallet == 5:
            tala(0)

        elif EWallet == 6:
            print("Thank you for using DX Kiosk")
            break
            isrepeat = False
            return
        
        else :
            print("Please enter a valid number")
            continue

def internet(company):
    isrepeat = True
    while isrepeat == True: 

        print("Please select your Internet service provider: \n 1 - Converge \n 2 - Globe \n 3 - PLDT \n 4 - Sky Fiber \n 5  - Starlink \n 6 - Exit")
        Internet_Service_Provider = eval(input("Please enter the number of your Electric service provider:  "))

        if Internet_Service_Provider == 1:
            converge(0)
    
        elif Internet_Service_Provider == 2:
            globe(0)

        elif Internet_Service_Provider == 3:
            pldt(0)

        elif Internet_Service_Provider == 4:
            skyfiber(0)

        elif Internet_Service_Provider == 5:
            starlink(0)

        elif Internet_Service_Provider == 6:
            print("Thank you for using DX Kiosk")
            break
            isrepeat = False
            return
            
        else :
            print("Please enter a valid number")
            continue

def water(company):
    isrepeat = True
    while isrepeat == True: 

        print("Please select your Water service provider: \n 1 - Angeles Water \n 2 - Bocaue Water District \n 3 - Calamba Water District \n 4 - Catanauan Water District \n 5  - Gumaca Water District \n 6 - Prime Water \n 7 - Exit")
        Water_Service_Provider = eval(input("Please enter the number of your Electric service provider:  "))

        if Water_Service_Provider == 1:
            angeles(0)
    
        elif Water_Service_Provider == 2:
            bocaue(0)

        elif Water_Service_Provider == 3:
            calamba(0)

        elif Water_Service_Provider == 4:
            catanauan(0)

        elif Water_Service_Provider == 5:
            gumaca(0)
            
        elif Water_Service_Provider == 6:
           primewater(0)

        elif Water_Service_Provider == 7:
            print("Thank you for using DX Kiosk")
            break
            isrepeat = False
            return
        else :
            print("Please enter a valid number")
            continue

def electric(company):
    isrepeat = True
    while isrepeat == True: 

        print("Please select your Electric service provider: \n 1 - Meralco \n 2 - Quezelco \n 3 - Batelec \n 4 - Laguna Electric \n 5  - Exit")
        Electric_Service_Provider = eval(input("Please enter the number of your Electric service provider:  "))

        if Electric_Service_Provider == 1:
            meralco(0)
    
        elif Electric_Service_Provider == 2:
            quezelco(0)

        elif Electric_Service_Provider == 3:
           batelec(0)

        elif Electric_Service_Provider == 4:
            lagetec(0)

        elif Electric_Service_Provider == 5:
            print("Thank you for using DX Kiosk")
            break
            isrepeat = False
            return
        else :
            print("Please enter a valid number")
            continue

        
def load(telco):
    isrepeat = True
    while isrepeat == True: 

        print("Please select your Service provider: \n 1 - Talk n text \n 2 - Globe \n 3 - TM \n 4 - Smart \n 5 - Dito \n 6 - Sun \n 7 - Exit")
        Service_Provider = eval(input("Please enter the number of your provider:  "))

        if Service_Provider == 1:
            tnt(0)
    
        elif Service_Provider == 2:
            globe(0)

        elif Service_Provider == 3:
            tm(0)

        elif Service_Provider == 4:
            smart(0)

        elif Service_Provider == 5:
            dito(0)

        elif Service_Provider == 6:
            sun(0)

        elif Service_Provider == 7:
            print("Thank you for using DX Kiosk")
            break
            isrepeat = False
            return
        
        else :
            print("Please enter a valid number")
            continue

def main():
    isrepeat = True
    while isrepeat == True: 

        print("Please select what services do you need : \n 1 - E-Wallet \n 2 - Telco Products \n 3 - Electric bills payment \n 4 - Water \n 5 - Internet Provider \n 6 - Exit")
        Service = eval(input("Please enter the number of the services:  "))

        if Service == 1:
            ewallet(0)
    
        elif Service == 2:
            load(0)

        elif Service == 3:
            electric(0)

        elif Service == 4:
            water(0)

        elif Service == 5:
            internet(0)
        
        elif Service == 6:
            print("Thank you for using DX Kiosk")
            break
            isrepeat = False
            return

if __name__ == "__main__":
    main()

        
