from utils import *

runs = 5000
wins = 0

for i in range(runs):
    players = create_players()
    boxes = create_shuffled_boxes()

    if single_cycle(players, boxes):
        wins = wins + 1

print(f"{(float(wins)/runs) * 100}%")
