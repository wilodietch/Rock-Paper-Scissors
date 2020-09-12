import random
# Project Planning
# 2 players: player vs. computer
# Ask player their choice
# Computer makes choice
# Outputting and comparing who won
# players either choose: rock, paper or scissor
# rock beats scissor
# paper beats rock
# scissor beats paper

print ("Welcome to Rock, Paper, Scissors Showdown")

choices = ["rock", "paper", "scissors"]

player_choice = input("Choose rock, paper, or scissors: \n")

while player_choice not in choices:
    player_choice = input("Not valid. Please choose rock, paper, or scissors \n")

print(f"Player choice: {player_choice}")

