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
my_choice=int(input("What so you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissor.\n"))
if my_choice==0:
    print("\nYou chose Rock: ")
    print(rock)
if my_choice==1:
    print("\nYou chose Paper: ")
    print(paper)
if my_choice==2:
    print("\nYou chose Scissor: ")
    print(scissors)

computer_choice=random.randint(0,2)
if computer_choice==0:
    print("\nComputer chose Rock: ")
    print(rock)
if computer_choice==1:
    print("\nComputer chose Paper: ")
    print(paper)
if computer_choice==2:
    print("\nComputer chose Scissor: ")
    print(scissors)

if my_choice==0:
    if computer_choice==0:
        print("Tie!! Try again.")
    elif computer_choice==1:
        print("You lost.")
    else:
        print("You won.")
if my_choice==1:
    if computer_choice==1:
        print("Tie!! Try again.")
    elif computer_choice==0:
        print("You won.")
    else:
        print("You lost.")
if my_choice==2:
    if computer_choice==2:
        print("Tie!! Try again.")
    elif computer_choice==0:
        print("You lost.")
    else:
        print("You won.")

from time import sleep
sleep(10)#to wait 10 seconds before closing
