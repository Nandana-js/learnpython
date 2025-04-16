import random
print("Hello there! Welcome to the number guessing game")
def play_game():
    num_gs = random.randint(1,20)
    attempts = 0
    print("I'm thinking of a number between 1 and 20")
    
    while True:
        try:
            guess = int(input("take a guess: "))
            attempts += 1;

            if guess<num_gs:
                print("your number is too low")
            elif guess > num_gs:
                print("your number is too high")
            else:
                print(f"Hurray! you made it in {attempts} tries...")
                break
        except ValueError:
            print("Invalid input")

def main():
    while True:
        play_game()
        again = input("Do you want to play the game again(yes/no): ").lower()
        if again != "yes":
            print("Thank you for your interest in playing..")
            break
main()