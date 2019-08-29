'''
Task 3.3 Custom filter

Implement custom_filter function, which will behave like the original Python filter() function.

Add docstring.
'''


def my_filter(my_function, some_list):

    """
    This function does some iteration with itch element in sorted list
    :param my_function: function what need to do something with list
    :type my_function: function what we would use to sorted list
    :param some_list: list what we need to sort
    :type some_list: list
    :return: some_result: list with manipulation by my_function if condition is OK
    :rtype: list
    """

    some_result = []
    for i in some_list:
        if i > 10:
            some_result.append(my_function(i))
    return some_result


some_list = [1, 23, 2, 6, 89, 95, 64, 11, 5]
# we need to create number list
print(my_filter(lambda x: x * 2, some_list))