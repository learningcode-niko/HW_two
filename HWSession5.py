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

