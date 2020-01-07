##Basic Calculator
##
##Num_1 = input("Enter a number: ")
##Num_2 = input("Enter another number: ")
##
##result= Num_1 + Num_2
##print(result)


## Python automatically converts anything in the input function into a String
## So you must do the following

Num_1 = input("Enter a number: ")
Num_2 = input("Enter another number: ")

result= float(Num_1) + int(Num_2)

print(result) ## The output will be float
