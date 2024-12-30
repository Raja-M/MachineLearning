# import random
# from random import choices
#
#
# def get_choices():
#     player_choice = input("Enter a choice (rock, paper, scissors):  ")
#     options = ["rock", "paper", "scissor"]
#     computer_choice = random.choice(options)
#     choices = {"player": player_choice, "computer": computer_choice}
#     return choices
#
# def check_win(player, computer):
#     print(f"You chose {player} ,computer chose {computer}")
#     if player==computer:
#         return "It's a tie!"
#     elif player == 'rock':
#         if computer == 'scissors':
#             return "Rock smashes scissors! You win!"
#         else:
#             return "Paper covers rock! You lose."
#     elif player == 'paper':
#         if computer == 'rock':
#             return "Paper covers rock! You win!"
#         else:
#             return "Scissors cuts paper! You lose."
#     elif player == 'scissors':
#         if computer == 'paper':
#             return "Scissors cuts paper! You win!"
#         else:
#             return "Rock smashes scissors! You lose."
# choices = get_choices()
# result = check_win(choices['player'], choices['computer'])
# print(result)
from src.FunctionStatements import hello

# dog = {"name": "roger", "age": 8, "color": "green" }
# dog["favorite food"] = "Meat"
# del dog['color']
# dogCopy = dog.copy()
# print(dog)

# set1 = {"roger","syd", "roger"}
# set2 = {"roger"}
#
# print(list(set1))

# def hello(name, age):
# #     print('Hello'+ name + ", you are "+ str(age)+" years old!")
# # hello(" Simbu",2)

# def change(value):
#     value["name"] = "Syd"
# val = {"name": "Aaradhya"}
# change(val)
# print(val)

def hello(name):
    if not name:
        return
    print('Hello'+ name + "!")
hello(False)
