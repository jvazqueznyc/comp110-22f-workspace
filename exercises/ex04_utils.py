"""EX04 - Utils - Recreating three commonly used functions to gain an understanding of the code behind them."""

__author__ = "730622831"


def all(our_list_of_ints: list[int], our_int_variable: int) -> bool:
    """Given a list of intergers and a single interger, checks to see if every individual interger in list equals the single interger."""
    index_counter_variable = 0
    if len(our_list_of_ints) == 0:
        return False
    while index_counter_variable < len(our_list_of_ints):
        if our_list_of_ints[index_counter_variable] != our_int_variable:
            return False
        else:
            index_counter_variable = index_counter_variable + 1
    return True


def max(max_list_of_ints: list[int]) -> int:
    """Given a list of ints, returns the largest int in list."""
    if len(max_list_of_ints) == 0:
        raise ValueError("max() arg is an empty List")
    max_list_index_counter = 0
    max_item = max_list_of_ints[0]
    while max_list_index_counter < len(max_list_of_ints):
        if max_item < max_list_of_ints[max_list_index_counter]:
            max_item = max_list_of_ints[max_list_index_counter]
        max_list_index_counter = max_list_index_counter + 1
    return max_item


def max_dict(max_dict_w_ints: list[int]) -> int:
    """Given a dict with int values, return the largest int in list."""
    if len(max_dict_w_ints) == 0:
        raise ValueError("max_dict() parameter is an empty dictionary. Add pairs to dictionary and try again.")
    max_pair = ""
    for key in max_dict_w_ints:

    max_list_index_counter = 0
    max_item = max_dict_w_ints[0]
    while max_list_index_counter < len(max_dict_w_ints):
        if max_item < max_dict_w_ints[max_list_index_counter]:
            max_item = max_dict_w_ints[max_list_index_counter]
        max_list_index_counter = max_list_index_counter + 1
    return max_item


def is_equal(list_ints_1: list[int], list_ints_2: list[int]) -> bool:
    """Given two lists of ints, checks to see if every integer at every index is the same in both lists."""
    index_counter_both_lists = 0
    if len(list_ints_1) != len(list_ints_2):
        return False
    while index_counter_both_lists < len(list_ints_1):
        if list_ints_1[index_counter_both_lists] == list_ints_2[index_counter_both_lists]:
            index_counter_both_lists = index_counter_both_lists + 1
        else:
            return False
    return True