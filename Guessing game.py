secret_word  = "Bacon"
guess        = ""
guessCount   = 0
guessLimit   = 3
outOfGuesses = False

while guess != secret_word and not (outOfGuesses):
    if guessCount < guessLimit:
        guess = input("Enter a word: ")
        guessCount += 1
    else:
        outOfGuesses = True
    
if outOfGuesses:
    print("Wrong word!")
else:
    print("You Win!")
