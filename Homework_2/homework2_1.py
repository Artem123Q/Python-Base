'''
Task 2.1 - Exes and Ohs
Check to see if a string has the same amount of 'x's and 'o's. The string can contain any char.
Examples:
input: "ooxx"
output: True
input: "xooxx"
output: False
input: "ooxXm"
output: True
True when no 'x' and 'o' is present
input: "zpzpzpp"
output: True'''

some_word = input('Enter something: ')
check_x = [i for i in some_word if i == 'X' or i == 'x']
check_o = [i for i in some_word if i == 'O' or i == 'o']
if len(check_o) == len(check_x):
    print(True)
elif len(check_o) == 0 and len(check_x) == 0:
    print(True)
else:
    print(False)
