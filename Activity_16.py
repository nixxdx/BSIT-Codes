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