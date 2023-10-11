import random

print("rock...paper...scissor")


user=input("please return your choice?")

number=random.randint(1,3)

player = ""

if number == 1:
    player = "rock"
    print("player choice rock")
elif number == 2:
    player = "paper"
    print("player chose paper")
elif number == 3:
    player = "scissor"
    print("player chose scissor")

if player == "rock" and user == "paper":
    print("user win")
elif player == "rock" and user == "scissor":
    print("player win")
elif player == "paper" and user == "rock":
     print("player win")
elif player=="paper" and user == "scissor":
     print("user win")
elif player == "scissor" and user == "paper":
     print("player win")
elif player == "scissor" and user == "rock":
     print("user win")