import random


secret = random.randint(1, 50)
attempts = 5

    
while attempts > 0:
    guess = int(input("Guess the number between 1 and 50: "))
    if guess == secret:
        print("Congratulations! You guessed the correct number.")
        break
    if guess < secret: 
        print("Too Low! Try again.")
    if guess > secret:
        print("Too High! Try again.")
    attempts -= 1
      

