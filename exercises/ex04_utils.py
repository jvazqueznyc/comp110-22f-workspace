"""EX04 - Utils - Recreating three commonly used functions to gain an understanding of the code behind them."""

__author__ = "730622831"

from ast import Return
from re import L


def all(our_list_of_ints: list[int], our_int_variable: int) -> bool:
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
    if len(max_list_of_ints) == 0:
        raise ValueError("max() arg is an empty List")
    max_list_index_counter = 0
    max_item = max_list_of_ints[0]
    while max_list_index_counter < len(max_list_of_ints):
        if max_item < max_list_of_ints[max_list_index_counter]:
            max_item = max_list_of_ints[max_list_index_counter]
        max_list_index_counter = max_list_index_counter + 1
    return max_item


def is_equal(list_ints_1: list[int], list_ints_2: list[int]) -> bool:
    index_counter_both_lists = 0
    if len(list_ints_1) != len(list_ints_2):
        return False
    while index_counter_both_lists < len(list_ints_1):
        if list_ints_1[index_counter_both_lists] == list_ints_2[index_counter_both_lists]:
            index_counter_both_lists = index_counter_both_lists + 1
        else:
            return False
    return True

