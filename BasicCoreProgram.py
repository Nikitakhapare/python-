'''
@Author: Nikita
@Date: 2022-04-03 19: 14: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-03 19:14:00
@Title: coin flip Program to calculate percentage of Haid vs Tail
'''

import random

def flipCoin():
    """
        Description:
            Function to calculate percentage of haid vs tail
        Parameter:
            No parameter
        Return:
            returning the percentage of Head vs Tail
    """
    no_of_flip=int(input("How Many times You want to flip coin "))
    tail=0
    tailPecentage=0
    for i in range(no_of_flip):
        coinFlip=random.randint(0,1)

        if coinFlip<0.5:
            tail+=1
            tailPecentage=(tail/no_of_flip)*100

        else:
            headPercentage=100-tailPecentage

    return print("Percentage of head ", headPercentage, "vs Tail is ",tailPecentage)

flipCoin()

