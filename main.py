from random import randint
from art import logo
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
answer = randint(1, 100)
# print(f"Pssst, the correct answer is {answer}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
game_over = False

def guess_logic(attempts):
  global game_over
  for _ in range(attempts):
    if attempts > 0:
      guess = int(input("Make a guess: "))
      if guess == answer:
        print(f"You got it! The answer was {answer}.")
        game_over = True
        return
      elif guess < answer:
        print("Too low.\nGuess Again.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")
      elif guess > answer:
        print("Too high.\nGuess Again.")
        attempts -= 1 
        print(f"You have {attempts} attempts remaining to guess the number.")
  print("You've run out of guesses, you lose.")
  print(f"The number was: {answer}")
  game_over = True
  return
  
if difficulty == "easy":
  guess_logic(10)
else:
  guess_logic(5)
