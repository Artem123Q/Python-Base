class Character:
    """
    Class describes character
    """
    def __init__(self, name):

        self.name = name
        self._hp = 100
        self._damage = 5
        self.move

    def is_dead(self):

        """
        Function to check if char is dead
        """

        if self._hp <= 0:
            return True

    def on_combat(self, enemy):

        """
        Function to describe fighting
        """

        self._hp -= enemy.attack()
        is_dead = self.is_dead()

        if is_dead:
            return is_dead

        print(f'Char hp: {self._hp}')
        enemy.take_damage(self._damage)

    def move(self):
        """
        Function to describe movement of character
        """
        move_to = input('choose your move:\n')
        move_choice = {'w': 'forward', 'a': 'left', 's': 'down', 'd': 'right'}

        if move_to in move_choice:
            return print(f'You move {move_choice.get(move_to)}')

    def hill(self):
        """
        Function to describe characters hill
        """
        self._hp += 5
        return print(f'You have a hill + 5 hp{self._hp}')


class Orc(Character):

    """
    Class to describe Orc race
    """

    def __init__(self, name):

        super().__init__(name)  # call to Character().__init__

        self._hp *= 1.5
        self._damage *= 1.2


class Wizard(Character):

     """
     Class to describe wizard rase
     """

     def __init__(self, name):

         super().__init__(name)

         self._hp *= 1.1
         self._damade *= 1.6

# races to be checked within a game loop
RACES = {'orc': Orc, 'wizard' : Wizard}

