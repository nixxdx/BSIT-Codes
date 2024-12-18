def cc1():
    print("\n\n\n\n\t\t\t\t\t\t\t\t\t\t*\n\n\n\n\t\t\t\t\t\t\t\t\t*\t*\t*\n\n\n\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\n\n\n\t\t\t\t\t\t\t*\t*\t*\t*\t*\t*\t*\n\n\n\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\n\n\n\t\t\t\t\t\t\t\t\t*\t*\t*\n\n\n\n\t\t\t\t\t\t\t\t\t\t*")

    return

def cc2():
    name = input("What is your name?")
    print("\n\n\n\n\t\t\t\t\t\t\t\t\t\t*\n\n\n\n\t\t\t\t\t\t\t\t\t*\t*\t*\n\n\n\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\n\n\n\t\t\t\t\t\t\t*\t\tHi\t!\t" + name + "\t\t*\n\n\n\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\n\n\n\t\t\t\t\t\t\t\t\t*\t*\t*\n\n\n\n\t\t\t\t\t\t\t\t\t\t*")
    return

def cc3():
    num1 = eval(input("Enter the first number : "))
    num2 = eval(input("Enter the second number :"))

    print("The sum of " , num1 , " and " , num2 , " is " , num1+num2)
    print("The difference of " , num1 , " and " , num2 , " is " , num1-num2)
    print("The product of " , num1 , " and " , num2 , " is " , num1*num2)
    print("The quotient of " , num1 , " and " , num2 , " is " , num1/num2)
    print(num1 , " exponent by " , 2 , " is " , num1**num2)
    print("The remainder of " , num1 , " and " , num2 , " is " , num1%num2)
    print("The floor division of " , num1 , " and " , num2 , " is " , num1//num2)
    return

def cc4():
    name = input("Enter your name: ")
    money = eval(input("Enter amount to deposit: "))

    onek = money//1000
    k = money % 1000
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
    o = f%1
    print(one,"- 1")
    return

def cc5():
    prelim = eval(input("Enter your grade in Prelim here: "))
    midterm = eval(input("Enter your grade in Midtermhere: "))
    semifinal = eval(input("Enter your grade in Semi-final here: "))
    final = eval(input("Enter your grade in Final here: "))
    quiz = eval(input("Enter your grade in Quiz here: "))
    project = eval(input("Enter your grade in Project here: "))

    fg = round((prelim * 0.15) + (midterm * 0.15) + (semifinal * 0.15) + (final * 0.15) + (quiz * 0.25) + (project * 0.15), 2)

    if fg >= 75 :
            print(f"Congratulations! You passed the course, your final grade is {fg}")
    else :
            print(f"Sorry, you failed, your final grade is {fg}")
    return

def cc6():
    name = input("Enter your name: ")
    age = eval(input("Enter your age: "))

    if age >= 1 and age <=8 :
            print(f"Hello {name}, you are {age} years old and you are classified as a toddler")
    elif age >= 9 and age <=14 :
            print(f"Hello {name}, you are {age} years old and you are classified as a pre-teen ")
    elif age >= 15 and age <= 18:
            print(f"Hello {name}, you are {age} years old and you are classified as teenager ")
    elif age >= 19 and age <= 27 :
            print(f"Hello {name}, you are {age} years old and you are classified as in your early adulthood ")
    elif age >= 28 and age <= 44 :
            print(f"Hello {name}, you are {age} years old and you are classified as a middle aged")
    elif age >= 45 and age <= 59 :
            print(f"Hello {name}, you are {age} years old and you are classified as in your post adulthood")
    elif age >= 60 and age <= 120 :
            print(f"Hello {name}, you are {age} years old and you are classified as a senior")
    else :
            print("Age invalid")
    return

def cc7():
    name = input("Please enter your name: ")
    grocery = input(f"Hi {name}, did you purchase a grocery today? (yes/no): ")

    if grocery.lower() == "yes" :
        disc = 4000
        product = input("What product did you purchase today: ")
        untaxedp = eval(input("What is the price of the product that you purchase: "))
        vat = untaxedp * 0.123
        taxedp = untaxedp + vat

        #Senior Citizen DISCOUNT
        age = eval(input("How old are you: "))
        if age >= 60 and age <= 150 :
            scdisc = untaxedp * 0.123
            scdiscount = taxedp - scdisc
            print("Your  total bill is" , round(scdiscount, 2))
            scpayment = eval(input("Payment: "))
            scchange = scpayment - scdiscount

            if scpayment >= scdiscount :
                print("Your change will be" , round(scchange, 2), ", thank you, come again")

            else : 
                print("Sorry, your payment is not enough, please pay" , scdiscount)

        elif age >= 1 and age <= 59 : 
            #4k Discount
            if untaxedp >= 4000 :
                discp = untaxedp * 0.038
                discprice = untaxedp - discp
                print("Your discounted total is" , round(discprice, 2))
                dppayment = eval(input("Payment: "))
                dchange = dppayment - discprice

                if dppayment >= discprice :
                    print("Your change will be" , round(dchange, 2), ", thank you, come again")

                else : 
                    print("Sorry, your payment is not enough, please pay" , discprice)
            #No Discount
            else :
                print("You are not eligible for any discount, your total bill is" , round(taxedp, 2))
                ndpayment= eval(input("Payment: "))
                ndchange = ndpayment - taxedp

                if ndpayment >= taxedp:
                    print("Your change will be" , round(ndchange, 2), ", thank you, come again")

                else : 
                    print("Sorry, your payment is not enough, please pay" , round(taxedp,2))
        else :
            print("Sorry, your age is invalid, please enter a valid age and try again")
    elif grocery.lower() == "no" :
        print("Thank you for coming, hope you visit again: ")
        
    else :
        print("Sorry, your answer is invalid, please answer (yes/no) and try again")
    return

def cc8():

    sum = 0
    odd = 0
    even = 0

    for numbers in range(1,11):
        num = eval(input("Please enter a number: "))
        sum += num

        if num % 2 == 0 :
            even += num
        else: 
            odd += num
        
    print(f"The sum of all the given numbers is {sum}\nThe sum of all the Even numbers is {even}\nThe sum of all the Odd number is {odd}")
    return

def cc9():
    for v in range(1, 6):
        for w in range(1, v + 1):
            print(" ", end=" ")
        for x in range(6, v, -1):
            print("*", end=" ")
        print()
    return

def cc10():
    for a in range(6, 0, -1):
        for b in range(1, a + 1):
            print(" ", end=" ")
        for c in range(6, a, -1):
            print("*", end=" ")
        for d in range(6 , a , -1):
            print("*", end=" ")
        print()

    for a in range(1, 6):
        for b in range(1, a + 1):
            print(" ", end=" ")
        for c in range(6, a, -1):
            print("^", end=" ")
        for d in range(6 , a , -1):
            print("^", end=" ")
        print()
    return

def cc11():
    for a in range(7, 0, -1):
        for b in range(1, a+1):
            print(" ", end=" ")
        for c in range(6, a, -1):
            print("*", end=" ")
        for d in range(7, a, -1):
            print("*", end=" ")
        print()


    for a in range(0,8):
        for b in range(1, a+1):
            print(" ", end=" ")
        for c in range(6, a, -1):
            print("*", end=" ")
        for d in range(7, a, -1):
            print("*", end=" ")
        print()
    return

def cc12():
    for i in range(6, 0, -1):
        for j in range(1, i + 1):
            print(" ", end=" ")
        for k in range(6, i, -1):
            print("*", end=" ")
        for l in range(6, i, -1):
            print("*", end=" ")
        print()

    for m in range(1,5):
        for n in range(1, i+2):
            print("    ", end=" ")
        for o in range(1, i+2):
            print("*", end=" ")
        print()
    return

def cc13():
    sum = 0
    isrepeat = True

    while isrepeat == True :
        number = eval(input("Please enter a number (Put '0' to stop): "))
        sum+=number
        if number == 0 :
            isrepeat = False
            print(f"The sum of all given number is {sum}")
    return

def cc14():
    
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

def activity1():
    print("Hello World!")
    return

def activity2():

    name = input("Please enter your name: ")
    age = input("Enter your age number: ")
    email = input("Enter your email: ")

    print()
    print("Hi! " + name + " Welcome!! :) \n" + "Your age is " + age + " right? \n" + "Your email address is: " + email)
    print("Your name consist of" + len(name) + "characters")

    num1 = eval(input("Please input a number: "))
    num2 = eval(input("Please input a number: "))

    print()
    print(num1 + "+" + num2 + "=" + num1 + num2) 
    return

def activity3():

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    address = input("Enter your address: ")

    print(f"Hi {name}, from {address} and {age} yrs  old")
    return

def activity4():

    f = eval(input("Enter the Fahrenheit you want to convert: "))
    c = (f-32)* 5 / 9

    print(f"{f} degree fahrenheit converted to celsius is {round(c,2)}")

    cel = eval(input("Enter the Celcius: "))
    fah = (c*9/5) + 32

    print(f"{cel} degree celcius converted to fahrenheit is {round(fah)}")
    return

def activity5():

    x = 10 
    print(x)

    x += x + 10
    print(x)

    x += x + 10 
    print(x)

    x *= 10
    print(x)

    x -= 600
    print(x)

    x /= 10 
    print(x)
    return

def activity6(): 

    password = "Hello World"

    mypassword = input("Enter password (Put 'Hello Word' to get access): ")

    if password == mypassword:
        print("Welcome to conditional statements")

    elif mypassword == "Hello Code":
        print("You are Granted permission!") 

    elif mypassword == "Hello Love":
        print("You are Granted permission using other password!")

    else:
        print("Invalid password\nAccess Denied")
    return

def activity7():
    name = input("Enter your name: ")
    isEnrolled = input("Are you enrolled in DLL (yes/no): ")
    if isEnrolled.lower() == "yes":
        print(f"Hi {name}, welcome to DLL scholarship application")
        
        age = int(input("Enter your age: "))
        if age >= 18 and age <= 35 :
            print("Your age is qualified with the age requirement")

            grade = eval(input("Enter your GWA here: "))
            if grade >= 85 and age <= 99:
                print("Your grade is qualified in DLL scholarship application")

                is4ps = input("Are you a 4ps beneficiary?(yes/no)")
                if is4ps.lower() == "yes":
                    print("Congratulations! You are qualified to be a scholar")
                elif is4ps.lower() == "no":
                    print("Sorry, you are not eligible to recieve a scholarship")
            else:
                print("Sorry your grades is not enough to be a scholar, better luck next time.")
    elif isEnrolled.lower() == "no":
        print("You must be a student of Dalubhasaan ng Lungsod ng Lucena to be able to apply for scholarship")
    else:
        print("You have entered an Invalid answer.")
    return

def activity8():

    sum = 0
    odd = 0 
    even = 0

    for x in range(1,11):
        num = eval(input(f"Input# {x}: "))
        sum += num 
        if num % 2 == 0:
            even += num
        else:
            odd += num
    print(f"The sum of all numbers are: {sum}")
    print(f"The sum of all even numbers are: {even}")
    print(f"The sum of all odd numbers are: {odd}")
    return

def activity9():

    num = eval(input("Enter any number: "))
    factorial = 1 

    for x in range(num,0,-1):
        factorial *= x
    print(f"The factorial of {num} is {factorial}")
    return

def activity10():

    for x in range(1,11):
        print(x,end=" ")
    for y in range(1,11):
        print("*",end=" ")
    print()
    return

def activity11():

    for x in range(1,11):
        for y in range(1,x+1):
            print(" ",end=" ")
        for z in range(11,x,-1):
            print("*",end=" ")
        print()
    return

def activity12():

    for x in range(7,0,-1):
        for y in range(1,x+1):
            print(" ",end=" ")
        for z in range(6,x,-1):
            print("*",end=" ")
        for q in range(7,x,-1):
            print("*",end=" ")
        print()
    for a in range(1,6):
        for b in range(0,a + 1):
            print(" ",end=" ")
        for c in range(5,a,-1):
            print("*",end=" ")
        for d in range(6,a,-1):
            print("*",end=" ")
        print()
    return

def activity13():

    num = eval(input("Enter the column number:  "))
    for x in range(1,11):
        for y in range(1,num+1):
            print(f"{x*y}={x+y}",end="\t")
        print()
    return

def activity14():
        
    import os
    repeat = True
    nt = 0
    while repeat == True:
        var = input("Do you wish to add more triangles? (yes/no) ")

        if var.lower() == "no":
                os.system('cls')
                print("LOOP HAS BEEN STOPPED")
                repeat = False
                break
                
        elif var.lower() == "yes":
            os.system('cls')
            nt += 1
            for x in range(1,7):
                for z in range(1,nt+1):
                    for y in range(1, x+1):
                            print("*", end=" ")
                    for a in range(7, x, -1):
                            print(" ",end=" ")
                    print(end=" ")
                print()
            continue
        else:
            print("Invalid Input")
    return

def activity15():

    isRepeat = True

    while isRepeat == True:
        name = input("Enter a name (type 'stop' to break the loop):  ")
        print(f"Hi {name}")
        #stopping point
        if name.lower() == "stop":
            print("Loop Terminated")
            break
            isRepeat = False
    return

def activity16():

    repeat = True 
    sum = 0
    while repeat == True:
        num = eval(input("Enter any number (type '0' to stop) --->  "))

        if num == 0:
            print("LOOP STOPPED")
            print(f"The sum of all the numbers given is {sum}")
            break
            tuloy = False 
        else:
            sum += num 
            continue
    return

def activity17():

    def greet_Someone():
        print("Hi , hoped your having a delightful Tuesday afternoon.")

    def greet_Person(name):
        print(f"Hi {name}, hoped your having a delightful Tuesday afternoon.")

    def right_Triangle():
        for x in range(1, 6):
            for y in range(1, x+1):
                print("*", end=" ")
            for z in range(6, x, -1):
                print(" ",end= " ")
            print()

    def get_info(name, age):
        print(f"Hi {name}, with age {age} yrs old.")

    def factorial(number):
        #factorial of 4 - 4 x 3 x 2 x 1 
        fact = 1 
        for x in range(number, 0, -1):
            fact *= x
        print(f"The factorial of {number} is {fact}")
    return

def activity18():
    
    def factorial(number):
        """THIS FUNCTION IS FOR CALCULATING FACTORIAL, JUST PUT THE NUMBER INSIDE THE PARENTHESIS"""
        fact = 1
        for x in range(number, 0, -1):
            fact *= x
            print(x)
        return fact
    return

def activity19():
    
    from Activity_18 import factorial  

    print(f"the factorial of 7 is {factorial(7)}")
    return

def activity20():
    fruits = ["Banana","Apple","Orange"]
    print(fruits)
    print(f"My favourite fruit is {fruits[2]}")
    fruits.append("Grapes")
    print(fruits)
    fruits.insert
    return

def codechallenges():
     
    isrepeat = True
    
    while isrepeat == True:
        print(" PLEASE SELECT FROM THE OPTIONS BELOW \n Put the number of your choice.\n 1 -\tDiamond asterisk\n 2 -\tYour name inside a diamond\n 3 -\tOperators\n 4 -\tBank Deposit\n 5 -\tGrade Calculator\n 6 -\tAge Classification\n 7 -\tGrocery\n 8 -\tAddition of Numbers\n 9 -\tTop Right triangle\n 10 -\tDiamond\n 11 -\tPerfect Diamond\n 12 -\tArrow\n 13 -\tAddition using while loop\n 14 -\tBank Simulator\n 15 -\tExit")
        choice = eval(input("Please enter your choice: "))

        if choice == 1:
            cc1()
        elif choice == 2:
            cc2()
        elif choice == 3:
            cc3()
        elif choice == 4:
            cc4()
        elif choice == 5:
            cc5()
        elif choice == 6:
            cc6()
        elif choice == 7:
            cc7()
        elif choice == 8:
            cc8()
        elif choice == 9:
            cc9()
        elif choice == 10:
            cc10()
        elif choice == 11:
            cc11()
        elif choice == 12:
            cc12()
        elif choice == 13:
            cc13()
        elif choice == 14:
            cc14()
        elif choice == 15:
            print("You have exited from Code Challenges!")
            isrepeat = False
            break
            return
        else:
            print("Your have entered an invalid answer, please select between the choices")
            continue
        return

def activities():

    isrepeat = True

    while isrepeat == True:
        print(" PLEASE SELECT FROM THE OPTIONS BELOW \n Put the number of your choice \n 1 -\tHello Word\n 2 -\t Stringed Information\n 3 -\tFormatted String Formation\n 4 -\tFahrenheit Converter\n 5 -\tAssignment Operators\n 6 -\tPassword\n 7 -\tDLL Scholarship\n 8 -\tAddition using for loop\n 9 -\tFactorial\n 10 -\tStraight Numbers\n 11 -\tTop Right Triangle\n 12 -\tPerfect diamond\n 13 -\tCollumns\n 14 -\tAdd triangle\n 15 -\tName loop\n 16 -\tNumber loo[\n 17 -\tFunction\n 18 -\tCalculating factorial\n 19 -\tImport\n 20 -\tList\n 21 -\tExit")
        choice = eval(input("Please enter your choice: "))

        if choice == 1:
            activity1()
        elif choice == 2:
            activity2()
        elif choice == 3:
            activity3()
        elif choice == 4:
            activity4()
        elif choice == 5:
            activity5()
        elif choice == 6:
            activity6()
        elif choice == 7:
            activity7()
        elif choice == 8:
            activity8()
        elif choice == 9:
            activity9()
        elif choice == 10:
            activity10()
        elif choice == 11:
            activity11()
        elif choice == 12:
            activity12()
        elif choice == 13:
            activity13()
        elif choice == 14:
            activity14()
        elif choice == 15:
            activity15()
        elif choice == 16:
            activity16()
        elif choice == 17:
            activity17()
        elif choice == 18:
            activity18()
        elif choice == 19:
            activity19()
        elif choice == 20:
            activity20()
        elif choice == 21:
            print("You have exited from Activities")
            isrepeat == False
            break
            return
        else:
            print("Your have entered an invalid answer, please select between the choices")
            continue
        
        return

def main():
    repeat = True
   

    while repeat == True:
        print("Welcome, This is the code compilation of Ajenico M. Gracias from BSIT-1B\nWhat code do you want to try?\n Press 1 -\tCode Challenges\n Press 2 -\tActivities\n Press 3 -\tExit")
        
        pick = eval(input("Please enter your choice:  "))

        if pick == 1:
            codechallenges()
        elif pick == 2:
            activities()
        elif pick == 3:
            repeat = False
            break
        else:
            print("Please enter a valid answer")
            continue


if __name__ == "__main__":
    main()