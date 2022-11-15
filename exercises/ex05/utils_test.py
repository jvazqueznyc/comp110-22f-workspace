"""EX05 - list Utility functions -  writing unit tests for our list utility functions."""

__author__ = "730622831"


from exercises.ex05.utils import only_evens, sub, concat


# only_evens tests


def test_only_evens_empty() -> None:
    """only_evens - 1st unit test function - edge case - empty input list results in empty return list."""
    test_list: list[float] = []
    assert only_evens(test_list) == []


def test_only_evens_no_even_values() -> None:
    """Only_evens - 2nd unit test function - use case - input list with only odd values returns empty list."""
    test_list: list[float] = [1, 3, 5, 7, 9]
    assert only_evens(test_list) == []


def test_only_evens_mixed_values() -> None:
    """Only_evens 3rd unit test functions - use case - input list with both odd and even values returns only even values (excluding start and end indexes)."""
    test_list: list[float] = [1, 2, 3, 4, 5, 6, 7, 8]
    assert only_evens(test_list) == [2, 4, 6, 8]


# concat unit tests


def test_concat_empty() -> None:
    """Concat - 1st unit test functions - edge case - Given two empty lists, an empty list is returned."""
    test_list: list[float] = []
    test_list_2: list[float] = []
    assert concat(test_list, test_list_2) == []


def test_concat_single_int() -> None:
    """Concat - 2nd unit test functions - one list of a single interger and a second list of intergers of various amounts of digits are succesfully combined."""
    test_list: list[float] = [1]
    test_list_2: list[float] = [200000000000000000000, 3, 43333333, 5111111111, 6, 70202929493294392923493294329432943294]
    assert concat(test_list, test_list_2) == [1, 200000000000000000000, 3, 43333333, 5111111111, 6, 70202929493294392923493294329432943294]


def test_concat_long() -> None:
    """Concat - 3rd unit test functions - use case - two long lists of many elements are correctly combined."""
    test_list: list[float] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    test_list_2: list[float] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert concat(test_list, test_list_2) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# sub unit tests


def test_sub_name() -> None:
    """Sub - 1st unit test functions - edge case - Given an empty list, return an empty list."""
    test_list: list[float] = []
    start_i = 0
    end_i = 10
    assert sub(test_list, start_i, end_i) == []


def test_sub_name2() -> None:
    """Sub - 2nd unit test functions - Given a start index that is less than 0, return a list that used 0 as the start index."""
    test_list: list[float] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start_i = -10
    end_i = 7
    assert sub(test_list, start_i, end_i) == [1, 2, 3, 4, 5, 6]


def test_sub_name3() -> None:
    """Sub - 3rd unit test functions - Given a very long list, return a very long list that doesn't include start and end indexes."""
    test_list: list[float] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    start_i = 0
    end_i = 20
    assert sub(test_list, start_i, end_i) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# the command to run your tests in new terminal is: python -m pytest exercises/ex05/utils_test.py