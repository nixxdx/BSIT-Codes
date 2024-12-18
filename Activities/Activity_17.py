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