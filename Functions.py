## Defining a function

def SayHello(Name, Age):
    print("Hello User!")
    print("Your name is: " + Name + ". " + "And your age is: " + str(Age) + ".")
    print("           ")

## Calling the function
SayHello("Michael", 15)
SayHello("Pence", "30")



##def power_four(Number):
##    Number * Number * Number * Number
##
##print(power_four(3)) ## None 


def power_four(Number):
    return Number * Number * Number * Number ## Any code after the return statement inside a function won't be executed

print(power_four(3))   ## 81


