import random
print('Guessing game')

# initialize the number of guesses to 1
i = 1

# set the result to 'Loser' by default and change it to 'Winner' if the user guesses the number
result = 'Loser'

# generate a random number between 1 and 100
random_number = random.randint(1, 100)


# loop to give the user 10 guesses to guess the number
while i <= 10:
    print(f'You have {11-i} guesses left')
    guess = int(input('Guess a number between 1 and 100: '))
    
    # check if the user guessed the number and break the loop
    if guess == random_number:
       result = 'Winner'
       break
    
    # give hits to the user
    elif guess < random_number:
        print('Try higher')
    elif guess > random_number:
        print('Try lower')
        
    i+=1

# print the result of the game
if result == 'Winner':
    print(f'You are a {result}, you guessed from {i} try')
else:
    print(f'You are a {result}, the number was {random_number}')
    
print('Game Over')