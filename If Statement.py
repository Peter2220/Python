is_male = True
is_tall = False

##if is_male or is_tall:   ## or
##    print("You are a male or tall or both")
##    print("                               ")
##else:
##    print("You are neither male or tall")
##



if is_male and is_tall:   ## and
    print("You are a male or tall or both")
    print("                              ")
elif is_male and not(is_tall):
    print("You are a short male|")
elif not(is_male) and is_tall:
    print("You are a male but are tall|")
else:
    print("You are neither male or tall")


## Comparison operators 
def max_num(num1, num2, num3):
    if num1 != num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(1,3,9))
