import random

def get_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == 's' and computer == 'w') or \
         (user == 'g' and computer == 's') or \
         (user == 'w' and computer == 'g'):
        return "user"
    else:
        return "computer"

print("Welcome to Snake-Water-Gun Game!")
print("Choices: 's' for Snake, 'w' for Water, 'g' for Gun")

user_score = 0
computer_score = 0
rounds = int(input("Enter number of rounds: "))

for i in range(rounds):
    print(f"\nRound {i+1}")
    user_choice = input("Enter your choice (s/w/g): ").lower()
    if user_choice not in ['s', 'w', 'g']:
        print("Invalid choice! Try again.")
        continue

    computer_choice = random.choice(['s', 'w', 'g'])
    print(f"Computer chose: {computer_choice}")

    winner = get_winner(user_choice, computer_choice)

    if winner == "user":
        print("You win this round!")
        user_score += 1
    elif winner == "computer":
        print("Computer wins this round!")
        computer_score += 1
    else:
        print("This round is a draw!")

print("\nFinal Scores:")
print(f"You: {user_score} | Computer: {computer_score}")

if user_score > computer_score:
    print(" Congratulations, you win the game!")
elif user_score < computer_score:
    print(" Sorry, computer wins the game!")
else:
    print(" It's a draw!")
