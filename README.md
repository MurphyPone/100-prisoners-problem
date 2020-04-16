# 100-prisoners-problem
visualization for the 100 prisoners problem

# [Problem summary](https://youtu.be/C5-I0bAuEUE):

Given 100 individuals with 100 marked bills randomly placed within 100 boxes, what is the probability and best strategy such that if each person is able to search 50/100 boxes, they all find their own bill?

The trivial solution is that each player has (50/100) = 50% chance to find their bill.

The odds that they all find their bills together is (1/2)^100 = 7.88E-31... bleak.

The optimal strategy requires each player to pick a box B(_x_) at random, read the number _y_ on the bill within, then go to the next box B(_y_), building a chain of boxes.