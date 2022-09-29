"""EX05 - list Utility functions - building list utility functions"""

__author__ = "730622831"

def only_evens(list_of_ints: list[int]) -> list:
    """Given an inputted list of ints, return a new list that only contains the even elements"""
    i = 0
    new_even_list_of_ints = []
    while i < len(list_of_ints):
        if list_of_ints[i] % 2 == 0:
            new_even_list_of_ints.append(list_of_ints[i])
        i += 1
    return new_even_list_of_ints

only_evens([1, 3, 4, 2, 1, 100])


def concat(list_one: list[int], list_two: list[int]) -> list:
    """Given two lists of ints, return a new list composed of the first list followed by the second list."""
    i = 0
    combined_list = []
    while i < len(list_one):
        combined_list.append(list_one[i])
        i = i + 1
    i = 0
    while i < len(list_two):
        combined_list.append(list_two[i])
        i = i + 1
    return combined_list


def sub(list_of_ints: list[int], start_index: int, end_index: int) -> list:
    """Given a list of ints, a start index, and an end index, return a list which is a subset of the given list, between the specified start index and the end index (i.e., doesn't include start and end indexes)."""
    i = 0
    portion_list_of_ints = []
    if start_index < 0:
        start_index = 0
    if end_index > len(list_of_ints):
        end_index = len(list_of_ints - 1)
    if len(list_of_ints) == 0 or start_index > len(list_of_ints) or end_index <= 0:
        return portion_list_of_ints
    while i < len(list_of_ints):
        if i > start_index and i < end_index:
            portion_list_of_ints.append(list_of_ints[i])
        i = i + 1
    return portion_list_of_ints