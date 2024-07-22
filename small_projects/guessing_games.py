#Write a program that simulates a guessing game. The program should generate a random number between 1 and 100, and then repeatedly ask 
#the user to guess the number. If the user's guess is too high, it should print "Too high, try again." If the guess is too low, it 
#should print "Too low, try again." If the guess is correct, it should print "Congratulations, you guessed it!" and terminate the program.

from random import randint
num = randint(1, 100)
print('Guess a number between 1 and 100')

while True:
    guess = int(input())
    if guess == num:
        print('Congratulations, you guessed it!')
        break
    elif guess < num:
               print('Too low, try again.')
    elif guess > num:
               print('Too high, try again.')


#Write a program that generates a random number between 1 and 10, then asks the user to guess the number. The program should give the 
#user three attempts to guess correctly. If the user guesses correctly within three attempts, it should print "Congratulations, you 
#guessed it!" Otherwise, it should print "Sorry, you didn't guess it. The correct number was [the correct number]."

from random import randint
num = randint(1, 10)

attempts = 0

print('Guess a number between 1 and 10. ')
while attempts < 3:
    guess = int(input())
    attempts += 1
    if guess == num:
        print("Congratulations, you guessed it!")
        break
    else:
        print("Incorrect guess. Try again.")
else:
    print(f"Sorry, you didn't guess it. The correct number was {num}.")