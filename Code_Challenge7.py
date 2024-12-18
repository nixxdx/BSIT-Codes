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