# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

# [1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
# [1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
# [] --> []
# You can assume that all values are integers. Do not mutate the input array.

def invert_1(lst):
    my_lst = []
    for el in lst:
        el * -1
        my_lst += el
    return my_lst

def invert_2(lst):
    my_lst = []
        for el in list:
        my_lst.append(el* -1)
    return my_lst

def invert_3(lst):
    return [el * -1 for el in lst]