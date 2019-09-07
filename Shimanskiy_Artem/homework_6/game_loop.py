import characters
import enemies
import random
from time import sleep


char_race = input('Your race: ')
char_name = input('Your name: ')

# Check if char_race exists
if char_race in characters.RACES:

    # Create main_char instance
    main_char = characters.RACES[char_race](char_name)

while True:

    # Randomly picked enemy

    move_char = main_char.move()

    x = random.randint(0, 1)

    if x != 0:
        hill_me = main_char.hill()
    else:
        pass

    current_enemy = random.choice(enemies.ENEMIES_TYPES)()
    is_dead = main_char.on_combat(current_enemy)

    if is_dead:
        print('Game over')
        break

    sleep(2)
        



    
    



