import deck_game
import random
from time import sleep

d = deck_game.Desk()
a = ['x', 'o']
choice_paws = random.choice(a)
print(f'You play: {choice_paws}')

d.print_desk()

while d.count_check():

    while True:

        yor_turn = input('Press \'m\' to move: or press \'e\' to eat paws:')

        if yor_turn == 'm':

            d.new_index()
            d.make_coordinate()
            d.checker_moove()
            break

        elif yor_turn == 'e':

            d.new_index()
            d.make_coordinate()
            d.fight_vs_bot()
            break
        else:

            continue

    d.print_desk()


    if d.bot_fight_checker() == True:

        d.bot_fight()
        d.print_desk()

    else:
        d.bot_moove()
        d.print_desk()
    sleep(2)


