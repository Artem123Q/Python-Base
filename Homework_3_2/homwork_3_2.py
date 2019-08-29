'''
Task 3.2 Custom map

Implement custom_map function, which will behave like the original Python map() function.

Add docstring.
'''


def my_map(my_function, some_list):

    """
    This function does some iteration with itch element in some_list
    :param my_function: function what need to do something with list
    :type my_function: function what can work with list type
    :param some_list: list where we need to do iteration
    :type some_list: list
    :return: some_result: list with manipulation by my_function
    :rtype: list
    """

    some_result = []
    for i in some_list:
        some_result.append(my_function(i))
    return some_result


some_list = list(input('enter some list: \n'))
print(my_map(lambda x: x * 2, some_list)) # We need only function what works with list
