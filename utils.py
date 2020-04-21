import numpy as np 
from random import randint 

# Creates shuffled boxes
def create_shuffled_boxes():
    ordered = np.arange(100)
    np.random.shuffle(ordered)
    return list(ordered)

# Initializes 100 players who haven't found there bill 
def create_players():
    return [False] * 100

# Checks if everryone found their dollar
def check_win(players):
    found = 0
    result = True
    for player in players:
        if player == False:
            result = False
        else: 
            found = found + 1
    # print(result, f", {found}%")
    return result

# Simulates one player searching 50 boxes
def player_search(players, boxes, i):
    visited = 0
    dollar = boxes[i]                               # Get the dollar from the players # box
    while visited < 49 and not players[i]:
        if dollar == i:                             # if the players dollar is in the box
            players[i] = True                       #   set the current player = true
            # print(f"player[{i}]: found after {visited+1} boxes")
            return 
        else: 
            dollar = boxes[dollar]                  #   go to the box of the dollar value
            visited = visited + 1
    # print(f"player[{i}]: did not find after {visited+1} boxes")

def single_cycle(players, boxes):
    for i in range(100):
        player_search(players, boxes, i)
    
    return check_win(players)
