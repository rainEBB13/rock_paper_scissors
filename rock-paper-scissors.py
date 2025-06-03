import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Lists
rock_paper_scissors = [rock,paper,scissors]

# User choice
user_choice = int(input("Choose rock, paper, or scissors: (0,1,2)\n"))

# Computer choice
computer_choice = random.randint(0,2)

# Game logic
if user_choice == computer_choice:
    print(rock_paper_scissors[user_choice])
    print(rock_paper_scissors[computer_choice])
    print("Draw")
else:
    if user_choice == 0 and computer_choice == 1:
        print(rock_paper_scissors[user_choice])
        print(f"The computer chose {computer_choice}")
        print(rock_paper_scissors[computer_choice])
        print("Lose")
    elif user_choice == 0 and computer_choice == 2:
        print(rock_paper_scissors[user_choice])
        print(f"The computer chose {computer_choice}")
        print(rock_paper_scissors[computer_choice])
        print("Win")
    elif user_choice == 1 and computer_choice == 0:
        print(rock_paper_scissors[user_choice])
        print(f"The computer chose {computer_choice}")
        print(rock_paper_scissors[computer_choice])
        print(computer_choice)
        print("Win")
    elif user_choice == 1 and computer_choice == 2:
        print(rock_paper_scissors[user_choice])
        print(f"The computer chose {computer_choice}")
        print(rock_paper_scissors[computer_choice])
        print(computer_choice)
        print("Lose")
    elif user_choice == 2 and computer_choice == 0:
        print(rock_paper_scissors[user_choice])
        print(f"The computer chose {computer_choice}")
        print(rock_paper_scissors[computer_choice])
        print(computer_choice)
        print("Lose")
    elif user_choice == 2 and computer_choice == 1:
        print(rock_paper_scissors[user_choice])
        print(f"The computer chose {computer_choice}")
        print(rock_paper_scissors[computer_choice])
        print(computer_choice)
        print("Win")