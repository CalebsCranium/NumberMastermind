# NumberMastermind

How this program works:

This program uses string values that contain numeric digits, not integer values. For example, '349' is a different value than 349.
This is done because we are performing string comparison swith the secret number, not math operations. 
Remember that '0' can be a leading digit: the string '013' is different from '13', but the integer 013 is the same as 13. 

#The expected output should look like this:

Number Mastermind, a deductive logic game.
          By Caleb Cooper

I am thinking of a 3-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:      That means:
Close             One digit is correct but in the wrong position.
Match            One digit is correct and in the right position.
No Match         No digit is correct.

For example, if the secret number was 248 and your guess was 843, the clues would be Match Close.
I have thought up a number.
You have 10 guesses to get it right.
Guess #1:
>911 
No Match
Guess #2:
>912
No Match
Guess #3:
>029
Close
Guess #4:
>019
Close
Guess #5:
>038
Close
Guess #6:
>024
Close
Guess #7:
>654
Close Close
Guess #8:
>
Guess #8:
>234
No Match
Guess #9:
>43
Guess #9:
>234
No Match
Guess #10:
>234
No Match
You ran out of guesses
The answer was 506.
Do you want to play again? (yes or no)
>
