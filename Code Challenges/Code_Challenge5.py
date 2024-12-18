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