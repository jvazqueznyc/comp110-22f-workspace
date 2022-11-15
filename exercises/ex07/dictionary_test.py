"""EX07 - Dictionary Functions - Some practice with some dictionary functions. 3x unit test functions for each function (invert, favorite_color, count)."""

__author__ = "730622831"


# Import functions from EX07 Dictionary.
from exercises.dictionary import invert, favorite_color, count


def test_invert_edge_empty() -> None:
    """only_evens - 1st unit test function - edge case - empty input list results in empty return list."""
    test_input_dict: dict[str, str] = {}
    assert invert(test_input_dict) == {}


def test_invert_use_1() -> None:
    """only_evens - 1st unit test function - edge case - empty input list results in empty return list."""
    test_input_dict: dict[str, str] = {}
    assert invert(test_input_dict) == {}


def test_invert_use_2() -> None:
    """only_evens - 1st unit test function - edge case - empty input list results in empty return list."""
    test_input_dict: dict[str, str] = {}
    assert invert(test_input_dict) == {}


def test_favorite_color_edge_empty() -> None:
    """only_evens - 1st unit test function - edge case - empty input list results in empty return list."""
    test_input_dict: dict[str, str] = {}
    assert favorite_color(test_input_dict) == {}


def test_favorite_color_use_1() -> None:
    """only_evens - 1st unit test function - edge case - empty input list results in empty return list."""
    test_input_dict: dict[str, str] = {}
    assert favorite_color(test_input_dict) == {}


def test_favorite_color_use_2() -> None:
    """only_evens - 1st unit test function - edge case - empty input list results in empty return list."""
    test_input_dict: dict[str, str] = {}
    assert favorite_color(test_input_dict) == {}


def test_count_edge_empty() -> None:
    """only_evens - 1st unit test function - edge case - empty input list results in empty return list."""
    test_input_dict: dict[str, str] = {}
    assert count(test_input_dict) == {}


def test_count_use_1() -> None:
    """only_evens - 1st unit test function - edge case - empty input list results in empty return list."""
    test_input_dict: dict[str, str] = {}
    assert count(test_input_dict) == {}


def test_count_use_2() -> None:
    """only_evens - 1st unit test function - edge case - empty input list results in empty return list."""
    test_input_dict: dict[str, str] = {}
    assert count(test_input_dict) == {}


# def test_invert_use_
# """"""
# # KeyError test. See assignment instructions
# def test_invert_use_
# """"""

# def test_favorite_color_edge_
# """"""
# def test_favorite_color_use_
# """"""
# def test_favorite_color_use_
# """"""

# def count_edge_
# """"""
# def count_use_
# """"""
# def count_use_
# """"""

# # The command to run your tests is python -m pytest exercises/ex07.