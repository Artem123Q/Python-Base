'''
Task 5.2

Edit your previous task: put the results into a file.
Then create a new python script and import your previous program to the new script.
Write a program that reads the file and prints it three times.
Print the contents once by reading in the entire file, once by looping over the file object,
and once by storing the lines in a list and then working with them outside the 'with' block.
'''
'''from homework_5_1 import summ
print(summ())


with open('file_test', 'a') as in_file:
    for i in range(3):
        read_3_times = in_file.write(f'{summ()}\n')
        print(read_3_times)'''

with open('file_test') as read_all:
    file_value = read_all.read()
    print(file_value)
for i in file_value:
    print(i)# loop
list_1 = []
for i in file_value:
    list_1.append(i)


