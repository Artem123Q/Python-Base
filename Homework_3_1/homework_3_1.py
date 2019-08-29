'''
Task 3.1 Array difference

Implement a difference function, which subtracts one list from another and returns the result.

It should remove all values (all of its occurrences) from list a, which are present in list b.

Add docstring.

Examples:

call: array_diff([1, 2], [1])
return: [2]

call: array_diff([1, 2, 2, 2, 3], [2])
return: [1,3]
'''


def array_difference(list_1, list_2):
    """
    This function removes all matches from list_1 which are present in list_2.

    :param list_1: list where I wont to delete some objects
    :type: list
    :param list_2: list where present object which should be delete from list_1.
    :type: list
    :return: list_3: list which do not have elements in list_2.
    :type: list
    """
    list_3 = []
    for i in list_1:
        list_3.append(i)

        for j in list_2:
            if j == i:
                list_3.remove(j)

    return list_3


list_1 = list(input('Enter some list 1: \n'))
list_2 = list(input('Enter some list 2: \n'))
filter_list = array_difference(list_1, list_2)
print(filter_list)
