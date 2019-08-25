'''
Task 2.2 - Reverse String

Reverse a string

Examples:

input: "Hello"
output: "olleH"
'''
string = input('Enter some word: \n')
revers_string = ''
count = 0

for i in string:
    count += 1
    result = len(string) - count
    revers_string += string[result]
    print(revers_string)
