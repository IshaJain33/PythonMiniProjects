import random

def get_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "snake" and computer == "water") or \
         (user == "water" and computer == "gun") or \
         (user == "gun" and computer == "snake"):
        return "user"
    else:
        return "computer"

choices = ["snake", "water", "gun"]

user_score = 0
computer_score = 0

while True:
    print("\nChoose: Snake, Water, or Gun (or type 'exit' to quit)")
    user_choice = input("Your choice: ").lower()

    if user_choice == "exit":
        print("Thanks for playing! Exiting the game...")
        break

    if user_choice not in choices:
        print("Invalid choice! Please enter 'snake', 'water', or 'gun'.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    result = get_winner(user_choice, computer_choice)
    
    if result == "user":
        user_score += 1
        print("You Win this round!")
    elif result == "computer":
        computer_score += 1
        print("Computer Wins this round!")
    else:
        print("It's a Draw!")

    print(f"Score: You - {user_score}, Computer - {computer_score}")

# Final Result
print("\nGame Over!")
if user_score > computer_score:
    print(f"You won the game! Final Score: You - {user_score}, Computer - {computer_score}")
elif user_score < computer_score:
    print(f"Computer won the game! Final Score: You - {user_score}, Computer - {computer_score}")
else:
    print(f"It's a Draw! Final Score: You - {user_score}, Computer - {computer_score}")
