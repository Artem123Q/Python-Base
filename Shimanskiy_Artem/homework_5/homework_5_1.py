'''
Task 5.1

One common problem when prompting for numerical input occurs when people provide text instead of numbers.
When you try to convert the input to an int, you`ll get a ValueError.
Write a program that prompts for two numbers.
Add them together and print the result.
Catch the ValueError if either input value is not a number, and print a friendly error message.
Test your program by entering two numbers and then by entering some text instead of a number.
'''


def summ():
    """
    This function summon 2 value we input
    :return: Return the sum of two numbers
    :rtype: int
    """
    try:
         first_value = int(input('Enter 1  number :\n'))
         second_value = int(input('Enter 2  number :\n'))
    except ValueError:
         print('number means NUMBER!!!')
    else:
        result = first_value + second_value
    return result


print(summ())

if __name__ == "__main__":
    with open('file_test', 'w')as f:
        write_in_file = f.write(f'{summ()}\n')
