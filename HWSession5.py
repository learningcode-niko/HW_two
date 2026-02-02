gross = int(input("What is your gross income: "))
kids = int(input("How many kids do you have: "))
try:
    print("Congratulations")
except ValueError:
    print("That is not a valid number")
    print("Nice Try")
except NameError:
    print("You are misspelling something")
except:
    print("I did not see that coming")
else:
    print("Thanks for playing fair")
if gross < 1000:
    print("Net Income =", gross * (0.9+0.01*kids))
elif gross < 2000:
    print("Net Income =", gross * (0.88+0.01*kids))
elif gross < 4000:
    print("Net Income =", gross * (0.86+0.005*kids))
else:
    print("Net Income =", gross * (0.82+0.005*kids))