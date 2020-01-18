word   = input("Please enter a word: ")

new_word = ''

for char in word:
    if char in "AEIOUaeiou":
        if char.islower():
            new_word = new_word + 'm'
        else:
            new_word = new_word + 'M'
    else:
        new_word = new_word + char
print(new_word)
