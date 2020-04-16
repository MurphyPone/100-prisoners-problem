import numpy as np 
from random import randint 
from copy import deepcopy

def create_shuffled_boxes():
    ordered = np.arange(100)
    np.random.shuffle(ordered)
    return list(ordered)

def create_players():
    return [False] * 100

# def player_search(player, boxes, index, searched=0):
#     if(searched >= 50):
#         current = boxes[randint(0,len(boxes))]
#         if(current == index):
#             player = True
#             return 
#         else: 
#             boxes.pop(index)
#             traverse()


boxes = create_shuffled_boxes()
players = create_players()

for p in range(len(players)):   # 100 players
    curr_box = randint(0, len(boxes)-1)
    curr_bill = boxes[curr_box]
    for b in range(50):         # each player gets 50 chances
        if(curr_bill == p):     # bill matches player index
            players[p] = True
        else:                   # bill does not match
            boxes.pop(curr_box)         # remove box from circulation
            curr_box = boxes[curr_bill]  # new bill = bill in the box


""" 
for each player:
    pick a random box
    do 49 times:
        if the bill in box matches player #
            player = true
        else 
            remove that box 
            pick new random box
"""

print(players)
