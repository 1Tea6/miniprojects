import time
from PNGS import simulator

print("welcome to pseudorandom number guessing game")

game = simulator(min=1, max=100, max_guesses=10)

print("there is a random number that is within 1 to 100")
print("if you get it right, you will win")

while game.guesses_left() > 0 and not game.won:
    print(f"Guesses remaining:  {game.guesses_left()}")
    user_input = input("Enter your guess between 1 and 100: ").strip()
    if not user_input.isdigit():
        print("put a number my guy")
        continue

    guess = int(user_input)
    if guess < game.min or guess > game.max:
        print("my guy between 1 and 100 not more not less")
        continue

    print("checking temperature..")
    time.sleep(0.4)
    feedback = game.check_guess(guess)
    print(feedback + "\n")

    if game.won:
        print(f"congrts, u got the right number in  {game.guesses_taken} guesses! ")
