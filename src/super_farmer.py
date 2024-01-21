import random
from enum import Enum


class Animal(Enum):
    RABBIT = 'Rabbit'
    SHEEP = 'Sheep'
    PIG = 'Pig'
    COW = 'Cow'
    HORSE = 'Hors'
    FOX = 'Fox'
    WOLF = 'Wolf'


blue_dice = 1 * [Animal.COW] + \
            1 * [Animal.WOLF] + \
            3 * [Animal.SHEEP] + \
            1 * [Animal.PIG] + \
            6 * [Animal.RABBIT]

orange_dice = 1 * [Animal.HORSE] + \
              1 * [Animal.FOX] + \
              2 * [Animal.SHEEP] + \
              2 * [Animal.PIG] + \
              6 * [Animal.RABBIT]


def roll_both_dice():
    blue_result = random.choice(blue_dice)
    orange_result = random.choice(orange_dice)
    return blue_result, orange_result


print(roll_both_dice())
