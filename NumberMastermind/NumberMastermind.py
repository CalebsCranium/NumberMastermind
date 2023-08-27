import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Number Mastermind, a deductive logic game.
          By Caleb Cooper

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:      That means:
Close             One digit is correct but in the wrong position.
Match            One digit is correct and in the right position.
No Match         No digit is correct.

For example, if the secret number was 248 and your guess was 843, the clues would be Match Close.'''.format(NUM_DIGITS))

    # Main Game Loop
    while True:
        # This stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it right.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looking until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}:'.format(numGuesses))
                guess = input('>')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # They're correct, so we break out of this loop
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses')
                print('The answer was {}.'.format(secretNum))

        # Ask the player if they want to play again
        print("Do you want to play again? (yes or no)")
        if not input('> ').lower().startswith('y'):
            break
        print('Thanks for playing!')

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with the close, match, and no match clues for a guess and
    secret number pair."""
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append('Match')
        elif guess[i] in secretNum:
            # A correct digit is in the incorrect place.
            clues.append('Close')
    if len(clues) == 0:
        return 'No Match'  # There are no correct digits at all.
    else:
        # Sort the clues into alphabetical order so their original order
        # does not give information away
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
