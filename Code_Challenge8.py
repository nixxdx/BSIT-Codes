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