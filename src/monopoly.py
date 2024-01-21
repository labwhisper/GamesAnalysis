import numpy as np

position_dict = ["Start", "[b] Molo w Brzeźnie", "Kasa Społeczna 2", "[b] Latarnia Morska Nowy Port", "Parking 200zł",
                 "PKM Osowa",
                 "[L] Piecki-Migowo Morena", "Szansa 7", "[L] Oliwa", "[L] Wrzeszcz", "Więzienie",
                 "[M] ECS", "[T] Radio Gdańsk", "[M] Centrum Hewelianum", "[M] Politechnika Gdańska",
                 "PKM Niedźwiednik",
                 "[O] Garnizon", "Kasa społeczna 17", "[O] Hala Targowa", "[O] Forum Gdańsk", "Bezpłatny Parking",
                 "[R] Park Oruński", "Szansa 22", "[R] Park Reagana", "[R] Park Oliwski", "PKM Jasień",
                 "[Y] Muzeum II Wojny Światowej", "[Y] Gdański Teatr Szekspirowski", "[T] trójmiasto.pl",
                 "[Y] Narodowe Muzeum Morskie",
                 "Idź do więzienia",
                 "[G] Brama Wyżynna", "[G] Brama Złota", "Kasa Społeczna 33", "[G] Brama Zielona", "PKM Strzyża",
                 "Szansa 36", "[B] Ratusz Głównego Miasta", "Sprzątanie po psie 100zł", "[B] Żuraw"]

group_brown = [1, 3]
group_light_blue_group = [6, 8, 9]
group_magenta = [11, 13, 14]
group_orange = [16, 18, 19]
group_red = [21, 23, 24]
group_yellow = [26, 27, 29]
group_green = [31, 32, 34]
group_blue = [37, 39]

start = 0
pkm_osowa = 5
jail = 10
ecs = 11
oliva_park = 24
go_to_jail = 30
crane = 39
closest_pkm = -20
closest_media = -100

media_list = [12, 28]
pkm_list = [5, 15, 25, 35]
chest_list = [2, 17, 33]
chance_list = [7, 22, 36]

p_chance_move = 10 / 16
p_chest_move = 2 / 16


def find_closest_pkm(position: int):
    if position < 5:
        return 5
    elif position < 15:
        return 15
    elif position < 25:
        return 25
    elif position < 35:
        return 35
    else:
        return 5


def find_closest_media(position: int):
    if position < 12:
        return 12
    elif position < 28:
        return 28
    else:
        return 12


chance_move_list = [start, start, -3, crane, -20, pkm_osowa, ecs, -20, jail, -100]
chest_move_list = [start, jail]


def move_on_chance(position: int):
    movement_on_chance = np.random.randint(0, 16)

    if movement_on_chance >= 10:
        return position

    movement = np.random.randint(0, 10)
    movement_value = chance_move_list[movement]

    # print("MOVE VALUE: " + str(movement_value))
    if movement_value >= 0:
        return movement_value
    elif movement_value == closest_pkm:
        return find_closest_pkm(position)
    elif movement_value == closest_media:
        return find_closest_media(position)
    elif movement_value == -3:
        return position - 3
    else:
        return position


def move_on_chest(position: int):
    movement_on_chance = np.random.randint(0, 16)
    if movement_on_chance < 2:
        movement = np.random.randint(0, 2)
        return chance_move_list[movement]
    else:
        return position


def rzuc_kostka_wiele_razy(ile_razy: int):
    kostka = np.random.randint(1, 7, ile_razy)
    return kostka.sum(0)


def next_position(position):
    dice_result = rzuc_kostka_wiele_razy(2)
    # print("rzut kostkami:" + str(dice_result))
    # print("pozycja poczatkowa:" + str(position))
    new_position = (position + dice_result) % 40
    # print("pozycja po dodaniu kostek:" + str(new_position))

    if new_position == go_to_jail:
        # print("do wiezienia:" + str(jail))
        return jail
    elif new_position in chance_list:
        # print("szansa:" + str(new_position))
        return move_on_chance(new_position)
    elif new_position in chest_list:
        # print("kasa spoleczna:" + str(new_position))
        return move_on_chest(new_position)
    else:
        # print("zwykly rzut" + str(new_position))
        return new_position


ilosc_rzutow = 1000000
next = start
positions = []
for x in range(ilosc_rzutow):
    next = next_position(next)
    positions.append(next)
unique, counts = np.unique(positions, return_counts=True)
values = dict(sorted(zip(unique, counts), key=lambda k: k[1], reverse=True))
# values = dict(sorted(values.items(), key=lambda k: k[1], reverse=True))
groups = {}
for key in values:
    group_key = position_dict[key][0:3]
    if group_key not in groups:
        groups[group_key] = 0
    groups[group_key] += values[key]
    print(position_dict[key] + " : " + str(values[key]))
sorted_groups = dict(sorted(groups.items(), key=lambda k: k[1], reverse=True))
for group in sorted_groups:
    print(group + " : " + str(groups[group]))
# print(values)
# unique, counts = np.unique(pole, return_counts=True)
# values = dict(zip(unique, counts))
# print(values)
