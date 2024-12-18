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