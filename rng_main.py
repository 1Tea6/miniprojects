import time
from simulator import Simulator

print("=" * 55)
print("PSEUDORANDOM NUMBER GUESSING SYSTEM: HOT & COLD")
print("=" * 55)
game = Simulator(low=1, high=100, max_guesses=10)
print(f"I've picked a secret number between {game.low} and {game.high}.")
print(f"You have {game.max_guesses} attempts to crack the code!\n")
while game.guesses_left() > 0 and not game.won:
    print(f"Guesses remaining: {game.guesses_left()}")
    user_input = input(f"Enter your guess ({game.low}-{game.high}): ").strip()
    if not user_input.isdigit():
        print("Please enter a valid positive number!\n")
        continue
    guess = int(user_input)
    if guess < game.low or guess > game.high:
        print(f"Guess must be between {game.low} and {game.high}!\n")
        continue
    print("Checking temperature...", end=" ")
    time.sleep(0.4)
    feedback = game.check_guess(guess)
    print(feedback + "\n")
print("=" * 55)
if game.won:
    print(f"VICTORY! You cracked the secret code in {game.guesses_taken} guess(es)!")
else:
    print("GAME OVER! You ran out of guesses.")
    print(f"The secret pseudorandom number was: {game.secret_number}")
print("=" * 55)
