import random
player = input("Choose rock, paper, or scissors. ")

#make a list of hand_signs
hand_signs = ["rock", "paper", "scissors"]

random.choice(hand_signs)
 
computer_choice = (random.choice(hand_signs))

#conditions
if player == computer_choice:
    print("It's a tie!")

if player == "rock" and computer_choice == "paper":
  print("computer chose paper, you lose.")
if player == "rock" and computer_choice == "scissors":
  print("computer chose scissors, you win!")

if player == "scissors" and computer_choice == "rock":
  print("computer chose rock, you lose.")
if player == "scissors" and computer_choice == "paper":
    print("computer chose paper, you win!")

if player == "paper" and computer_choice == "rock":
    print("computer chose rock, you win!")
if player == "paper" and computer_choice == "scissors":
    print("computer chose scissors, you lose.")
