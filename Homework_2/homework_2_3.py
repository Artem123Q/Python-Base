'''
Task 2.3 - Find the odd int

Given an array, find the int that appears an odd number of times.
There will always be only one integer that appears an odd number of times.

Examples:

list: [1, 2, 3, 1, 3, 2, 1]
output: 1
'''

task_list = [12, 2, 3, 12, 3, 2, 12]
filter_list = []

for i in task_list:
    task_list.count(i)
    if i % 2 != 0:
        print('There is only one odd number: ', task_list[i], '\nit was counted', i, 'times')
        break


    #if task_list.count(i):
        #print(task_list[0])

