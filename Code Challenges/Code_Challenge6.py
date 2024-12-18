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