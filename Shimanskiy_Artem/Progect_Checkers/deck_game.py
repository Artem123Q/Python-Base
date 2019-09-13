import random

class Desk:

    def __init__(self):

        self._play_x = 'x'
        self._play_o = 'o'
        self.desk = [['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
                          [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
                          ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
                          ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
                          [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o']]

    def print_desk(self):

        """
        Function create play-desk
        """

        syms = [' A ', ' B ', ' C ', ' D ', ' E ', ' F ', ' G ', ' H ']
        number_syms = ['1', '2', '3', '4', '5', '6', '7', '8']
        print('    A B C D E F G H')

        for j, i in enumerate(self.desk):
            print(f'{number_syms[j]}  ' + '|' + '|'.join(i) + '|' + f'  {number_syms[j]}')

        print('    A B C D E F G H')

    def count_check(self):

        """
        Function to count the number of itch paws
        """

        self.count_play_x = []
        self.count_play_o = []

        for k in range(len(self.desk)):
            for l in range(8):

                if self.desk[k][l] == 'x':
                    self.count_play_x.append(l)

                elif self.desk[k][l] == 'o':
                    self.count_play_o.append(l)

        if len(self.count_play_x) != 0 and len(self.count_play_o) != 0:
            return True


    def new_index(self):

        """
        Function for converting desk's indexes in new indexes (letter and number)
        """

        #index_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        #new_index_list = [0, 1, 2, 3, 4, 5, 6, 7]
        self.dict_letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        self.dict_number = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}

        #y = dict_letters[user_coordinate[0]]
        #x = dict_number[user_coordinate[1]]

        #self.d_ind = dict(zip(index_list, new_index_list))
        #self.d_ind =

        self.j = self.dict_letters[input('enter letter : ')]
        self.i = self.dict_number[input('enter number : ')]


    def make_coordinate(self):

        """
        Function to create coordinate from input and add them to the list
        """

        desk = self.desk

        self.gap = []
        self.x = []
        self.o = []

        for i in range(len(desk)):
            for j in range(len(desk[i])):

                if desk[i][j] == 'x':
                    self.x.append([i, j])

                elif desk[i][j] == 'o':
                    self.o.append([i, j])

                else:
                    self.gap.append([i, j])

        self.pkus_play_x = [[i + 1, j + 1] for l, j in self.x] #lists for mooving x
        self.pkus_2 = [[l + 1, j - 1] for l, j in self.x]
        self.pkus_3 = [[l - 1, j + 1] for l, j in self.x]
        self.pkus_4 = [[l - 1, j - 1] for l, j in self.x]

        self.pkus_play_o1 = [[l + 1, j + 1] for l, j in self.o]#lists for mooving o
        self.pkus_play_o2 = [[l + 1, j - 1] for l, j in self.o]
        self.pkus_play_o3 = [[l - 1, j + 1] for l, j in self.o]
        self.pkus_play_o4 = [[l - 1, j - 1] for l, j in self.o]

        self.pkus_play_o2_1 = [[l + 2, j + 2] for l, j in self.o]#lists for fighting o
        self.pkus_play_o2_2 = [[l + 2, j - 2] for l, j in self.o]
        self.pkus_play_o2_3 = [[l - 2, j + 2] for l, j in self.o]
        self.pkus_play_o2_4 = [[l - 2, j - 2] for l, j in self.o]

        self.pkus_1 =self.pkus_play_x + self.pkus_2 #for possibilities to moove team x
        self.pkus_for_def_fight = self.pkus_play_x + self.pkus_2 + self.pkus_3 + self.pkus_4 #for possibilities to fight vs bot for team x

        self.pkus_play_o = self.pkus_play_o3 + self.pkus_play_o4#for possibilities to moove team x
        self.pkus_for_bot = self.pkus_play_o1 + self.pkus_play_o2 + self.pkus_play_o3 + self.pkus_play_o4#for possibilities to fight vs bot for team o
        self.pkus_play_o2_com = self.pkus_play_o2_1 + self.pkus_play_o2_2 + self.pkus_play_o2_3 + self.pkus_play_o2_4#for possibilities to fight vs bot for team o
        return(self.x, self.o, self.gap, self.pkus_1,self.pkus_for_def_fight,self.pkus_for_bot, self.pkus_play_o)


    def checker_moove(self):

        """
        Function for checking mooving possibilities of Player and move his checkers
        """

        self.ind = []

        for a in range(len(self.pkus_1)):
            for b in range(len(self.gap)):

                if self.pkus_1[a] == self.gap[b]:

                    self.ind.append(self.pkus_1[a])# possible moves

        for x in range(len(self.ind)):

            self.ch_l = self.dict_letters[input('Move to (Letter):')]
            self.ch_n = self.dict_number[input('Move to (Number):')]

            if [self.ch_n, self.ch_l] == self.ind[x]:

                self.desk[self.ch_n][self.ch_l] = self.desk[self.i][self.j]
                self.desk[self.i][self.j] = ' '
                break

    def fight_vs_bot(self):
        """
        Function for checking fighting possibilities vs bot and fight
        """

        self.indy = []
        self.fght = []# possible variants to moove to beat the bot's checker

        for i in range(len(self.pkus_for_def_fight)):
            for j in range(len(self.o)):

                if self.pkus_for_def_fight[i] == self.o[j]:
                    self.indy.append(self.pkus_for_def_fight[i])

        self.indy = sorted(self.indy)
        self.sort_indy = [self.indy[i] for i in range(len(self.indy)) if i == 0 or self.indy[i] != self.indy[i - 1]]

        self.indy_plus_1 = [[l + 1, j + 1] for l, j in self.sort_indy]
        self.indy_plus_2 = [[l + 1, j - 1] for l, j in self.sort_indy]
        self.indy_plus_3 = [[l - 1, j + 1] for l, j in self.sort_indy]
        self.indy_plus_4 = [[l - 1, j - 1] for l, j in self.sort_indy]

        self.indy_common = self.indy_plus_1 + self.indy_plus_2 + self.indy_plus_3 + self.indy_plus_4

        for x in range(len(self.indy_common)):
            for y in range(len(self.gap)):

                if self.indy_common[x] == self.gap[y]:

                    self.fght.append(self.indy_common[x])


        self.ch_l_f = [self.dict_letters.get('Move to (Letter):')]

        self.ch_n_f = self.dict_number[input('Move to (Number):')]

        for x in range(len(self.sort_indy)):

            if [self.ch_n_f - 1, self.ch_l_f - 1] == self.sort_indy[x]:


                self.desk[self.ch_n_f][self.ch_l_f] = self.desk[self.i][self.j]
                self.desk[self.i][self.j] = ' '
                self.desk[self.ch_n_f - 1][self.ch_l_f - 1] = ' '
                break

            elif [self.ch_n_f + 1, self.ch_l_f - 1] == self.sort_indy[x]:

                self.desk[self.ch_n_f][self.ch_l_f] = self.desk[self.i][self.j]
                self.desk[self.i][self.j] = ' '
                self.desk[self.ch_n_f + 1][self.ch_l_f - 1] = ' '
                break

            elif [self.ch_n_f - 1, self.ch_l_f + 1] == self.sort_indy[x]:

                self.desk[self.ch_n_f][self.ch_l_f] = self.desk[self.i][self.j]
                self.desk[self.i][self.j] = ' '
                self.desk[self.ch_n_f - 1][self.ch_l_f + 1] = ' '
                break

            elif [self.ch_n_f + 1, self.ch_l_f + 1] == self.sort_indy[x] :

                self.desk[self.ch_n_f][self.ch_l_f] = self.desk[self.i][self.j]
                self.desk[self.i][self.j] = ' '
                self.desk[self.ch_n_f + 1][self.ch_l_f + 1] = ' '
                break


    def bot_moove(self):

        """
        Function for checking mooving possibilities of Bot and move his checkers
        """

        self.ind_bot = []

        for a in range(len(self.pkus_play_o)):
            for b in range(len(self.gap)):

                if self.pkus_play_o[a] == self.gap[b]:

                    self.ind_bot.append(self.pkus_play_o[a])

        self.i_bot, self.j_bot = random.choice(self.ind_bot)[0], random.choice(self.ind_bot)[1]

        for x in range(len(self.o)):

            if [self.i_bot + 1, self.j_bot - 1] == self.o[x]:

                self.desk[self.i_bot][self.j_bot] = self.desk[self.i_bot + 1][self.j_bot - 1]
                self.desk[self.i_bot + 1][self.j_bot - 1] = ' '
                break

            elif [self.i_bot + 1, self.j_bot + 1] == self.o[x]:

                self.desk[self.i_bot][self.j_bot] = self.desk[self.i_bot + 1][self.j_bot + 1]
                self.desk[self.i_bot + 1][self.j_bot + 1] = ' '
                break

            else:
                print(" You can't moove")


    def bot_fight_checker(self):

        """
        Function checking fight possibility
        """

        for i in range(len(self.pkus_for_bot)):
            for j in range(len(self.x)):
                for k in range(len(self.gap)):
                    for z in range(len(self.pkus_play_o2_com)):

                        if self.pkus_for_bot[i] == self.x[j] and self.pkus_play_o2_com[z] == self.gap[k]:

                            return(True)


    def bot_fight(self):

        """
        Function for beat Player's checker
        """

        self.indy_bot_f = []
        self.fght_bot = []

        for i in range(len(self.pkus_for_bot)):
            for j in range(len(self.x)):

                if self.pkus_for_bot[i] == self.x[j]:

                    self.indy_bot_f.append(self.pkus_for_bot[i])


        self.indy_bot_f = sorted(self.indy_bot_f)
        self.sort_indy_bot_f = [self.indy_bot_f[i] for i in range(len(self.indy_bot_f)) if i == 0 or self.indy_bot_f[i] != self.indy_bot_f[i - 1]]

        self.indy_b_plus_1 = [[l + 1, j + 1] for l, j in self.sort_indy_bot_f]
        self.indy_b_plus_2 = [[l + 1, j - 1] for l, j in self.sort_indy_bot_f]
        self.indy_b_plus_3 = [[l - 1, j + 1] for l, j in self.sort_indy_bot_f]
        self.indy_b_plus_4 = [[l - 1, j - 1] for l, j in self.sort_indy_bot_f]

        self.indy_common_b = self.indy_b_plus_1 + self.indy_b_plus_2 + self.indy_b_plus_3 + self.indy_b_plus_4

        for x in range(len(self.indy_common_b)):
            for y in range(len(self.gap)):

                if self.indy_common_b[x] == self.gap[y]:
                    self.fght_bot.append(self.indy_common_b[x])

        self.i_bot, self.j_bot = random.choice(self.fght_bot)[0], random.choice(self.fght_bot)[1]

        for x in range(len(self.indy_bot_f)):

            if [self.i_bot + 1, self.j_bot + 1] == self.indy_bot_f[x] and self.i_bot != 6 and self.i_bot != 7:

                self.desk[self.i_bot][self.j_bot] = self.desk[self.i_bot + 2][self.j_bot + 2]
                self.desk[self.i_bot + 2][self.j_bot + 2] = ' '
                self.desk[self.i_bot + 1][self.j_bot + 1] = ' '

                break

            elif [self.i_bot + 1, self.j_bot - 1] == self.indy_bot_f[x] and self.i_bot != 0 and self.i_bot != 1:

                self.desk[self.i_bot][self.j_bot] = self.desk[self.i_bot + 2][self.j_bot - 2]
                self.desk[self.i_bot + 2][self.j_bot - 2] = ' '
                self.desk[self.i_bot + 1][self.j_bot - 1] = ' '

                break

            elif [self.i_bot - 1, self.j_bot + 1] == self.indy_bot_f[x]:

                self.desk[self.i_bot][self.j_bot] = self.desk[self.i_bot - 2][self.j_bot + 2]
                self.desk[self.i_bot - 2][self.j_bot + 2] = ' '
                self.desk[self.i_bot - 1][self.j_bot + 1] = ' '

                break

            elif [self.i_bot - 1, self.j_bot - 1] == self.indy_bot_f[x]:

                self.desk[self.i_bot][self.j_bot] = self.desk[self.i_bot - 2][self.j_bot - 2]
                self.desk[self.i_bot - 2][self.j_bot - 2] = ' '
                self.desk[self.i_bot - 1][self.j_bot - 1] = ' '

                break
