sum = 0
isrepeat = True

while isrepeat == True :
    number = eval(input("Please enter a number (Put '0' to stop): "))
    sum+=number
    if number == 0 :
        isrepeat = False
        print(f"The sum of all given number is {sum}")