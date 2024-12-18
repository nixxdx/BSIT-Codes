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