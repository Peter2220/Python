## Print two words in seperate lines (new line):  \n

print("Sergio\nRamos")

## Escape the  "   using  \

print("Sergio\"Ramos")

## .upper()  isupper()      .lower()    islower()   

print("Sergio Ramos".lower())

print("Sergio Ramos".islower()) ##False

print("Sergio Ramos".lower().islower())  ##True


##Printing the length of a string
random_phrase = "Hi Amigo!"
print(len(phrase)) ## 9

##Printing any character using the index
print(phrase[0])   ## H

##Return the index of any character in a string
print(phrase.index("H"))  ## 0

##Return the index of the first encountered character in a string
print(phrase.index("i"))  ## 1

##Replacing a word/string with another one
print(phrase.replace("Amigo", "Amiga"))
