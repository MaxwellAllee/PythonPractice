secret_number = 9
guessCount = 0 
guessNumbers = 3
while guessCount < guessNumbers:
    guess = int(input('Guess: '))
    guessCount += 1
    if guess == secret_number:
        print("you won!!")
        break
else: 
    print("close but no cigar!")