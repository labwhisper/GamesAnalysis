import math
import random
from enum import Enum


class Animal(Enum):
    RABBIT = 'Rabbit'
    SHEEP = 'Sheep'
    PIG = 'Pig'
    COW = 'Cow'
    HORSE = 'Horse'
    FOX = 'Fox'
    WOLF = 'Wolf'
    SMALL_DOG = 'Small dog'
    BIG_DOG = 'Big dog'


animal_value = {
    Animal.RABBIT: 1,
    Animal.SHEEP: 6,
    Animal.SMALL_DOG: 6,
    Animal.PIG: 12,
    Animal.COW: 36,
    Animal.HORSE: 72,
    Animal.BIG_DOG: 36,
}

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

user_animals = []


def has_enough_animals(animal, quantity):
    return user_animals.count(animal) >= quantity


def remove_animals(animal, quantity):
    for _ in range(quantity):
        user_animals.remove(animal)


def add_animals(animal, quantity):
    user_animals.extend([animal] * quantity)


def calculate_exchange_quantity(animal_to_give, give_quantity, animal_to_receive):
    receive_ = animal_value[animal_to_give] * give_quantity / animal_value[animal_to_receive]
    print(f"RECEIVE: {receive_}")
    return math.floor(receive_)


def exchange_animals(animal_to_give, give_quantity, animal_to_receive):
    print(f"Trying to give {give_quantity} {animal_to_give.value} to get {animal_to_receive.value}.")
    required_quantity = calculate_exchange_quantity(animal_to_give, give_quantity, animal_to_receive)
    if required_quantity is not None and required_quantity >= 1:
        # if has_enough_animals(animal_to_give, give_quantity):
        print(f"Exchanging {give_quantity} {animal_to_give.value} to {required_quantity} {animal_to_receive.value}.")
        # remove_animals(animal_to_give, give_quantity)
        # add_animals(animal_to_receive, required_quantity)
    # else:
    #     print(f"Not enough {animal_to_give.value} to exchange.")
    else:
        print(f"Cannot exchange {give_quantity} {animal_to_give.value} for {animal_to_receive.value}.")


def roll_both_dice():
    blue_result = random.choice(blue_dice)
    orange_result = random.choice(orange_dice)
    return blue_result, orange_result


print("Roll | Blue / Orange")
for i in range(100):
    blue_roll, orange_roll = roll_both_dice()
    print(f"{i + 1:4} | {blue_roll.value}/{orange_roll.value}")

print(exchange_animals(Animal.PIG, 5, Animal.HORSE))
