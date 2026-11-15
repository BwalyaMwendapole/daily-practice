import random
# 1. Event Eligibility Check
print("--- 1. Event Eligibility Check ---")
random_number_1 = random.randrange(1,50+1)
print(random_number_1)

if random_number_1 <= 45:
    print("You are still not eligible to participate for this event")
    print("Wait another year and try again")
    print("Next participant please") 
else:
    print("You are eligible to participate")
    print("Please wait for 5 minutes while we organize someone to attend to you")
    print("thank you for your patience")

# 2. skiing Decision
print("\n--- 2. skiing Decision ---")
random_guess_2 = random.choice(['yes', 'no'])
print(random_guess_2)
statement = "Are you ready to go skiing?"
print(statement)

if random_guess_2 == 'yes':
    print("Then lets get going, time is not with us.")
    print("Make sure to lock your room door.")
else:
    print("How come?")
    print("Is everything okay?")

# 3. Dice Roll
print("\n--- 3. Dice Roll ---")
secret_dice = random.randint(1,6)
print("You rolled:",secret_dice)

# 4. Number Guessing Game
print("\n--- 4. Number Guessing game ---")
Random_number_3 = random.randint(1,50+1)
player_guess_1 = int(input("Enter a number from (1-50): "))

if Random_number_3 == player_guess_1:
    print("congratulations! you win.")
    print("You have been promomted to the next level.")
else:
    print("Sorry, try again")

# 5. Rock, Paper, Scissors
print("\n--- 5. Rock, Paper, Scissors ---")
sys_choices = ["rock", "paper", "scissors"]
computer = random.choice(sys_choices)
player_guess_2 = input("Pick (rock,paper or scissors): ")
print("computer chose ",computer)
print("you chose",player_guess_2)

if player_guess_2 == computer:
    print("Its a tie!")
elif player_guess_2 == "rock" and computer == "scissors":
    print("You wins!")
elif player_guess_2 == "scissors" and computer == "paper":
    print("You wins!")
elif player_guess_2 == "paper" and computer == "rock":
    print("You wins!")
else:
    print("Computer wins!")


    