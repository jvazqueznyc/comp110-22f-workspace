"""EX07 - Dictionary Functions - Some practice with some dictionary functions. This is where you will implement your function skeletons and implementations below."""

__author__ = "730622831"


invert_dict_input: dict[str, str] = {"UNC": "Tarheels", "Duke": "Blue Devils", "USC": "Trojans", "UMiami": "Hurricanes"}


def invert(inv_dict_parameter: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of [str, str], invert should return a dict[str, str] that inverts the keys and the values."""
    inverted_dict_output: dict[str, str] = {}
    for key in inv_dict_parameter:
        if inv_dict_parameter[key] in inverted_dict_output:
            raise KeyError(f"Duplicate key found: {inv_dict_parameter[key]}")
        print(inv_dict_parameter[key])
        inverted_dict_output[inv_dict_parameter[key]] = key  # inv_dict_parameter[key] returns values of inv_dict_parameter dictionary. the values of the old dict are now the keys of our new dict.; at the end of equation '= key' gives us the keys of inv_dict_parameter. Our og dict keys are now the values of our new dict.

    return inverted_dict_output


fav_colors_input_dict: dict[str, str] = {1: "red", 2: "red", 3: "red", 4: "orange", 5: "orange", 6: "yellow", 7: "green", 8: "green", 9: "green", 10: "blue", 11: "blue", 12: "indigo", 13: "violet"}


def favorite_color(fav_colors_parameter: dict[str, str]) -> str:
    """Given a dictionary of [str, str], favorite_colors returns a str which is the color that appears most frequently in dictionary. If there is a tie, returns the color that first appeared in dictionry."""
    new_dict_color_totals: dict[str, int] = {}
    for key in fav_colors_parameter:
        # if color being assigned from old dictionary already appears in new dictionary as a key, then increase value of that key in new dict by 1. If not, initialize it to 1.
        if fav_colors_parameter[key] in new_dict_color_totals:
            new_dict_color_totals[fav_colors_parameter[key]] += 1
        else:
            new_dict_color_totals[fav_colors_parameter[key]] = 1
    # print(new_dict_color_totals)
    # See instructions to see how to check the correctness of function.
    list_of_new_dict_values: list[int] = []
    for key in new_dict_color_totals:
        list_of_new_dict_values.append(new_dict_color_totals[key])
    # print(list_of_new_dict_values)
    max_value_new_dict_color_totals = max(list_of_new_dict_values)
    # print(max_value_new_dict_color_totals)
    for key in new_dict_color_totals:
        if new_dict_color_totals[key] == max_value_new_dict_color_totals:
            # print(key)
            return key

# print(favorite_color(fav_colors_input_dict))  # To test favorite_color function.


count_input_list: list[str] = ["A", "A", "A", "A", "B", "B", "B", "C", "D", "D", "A", "A", "B", "D", "C", "B"]


def count(count_parameter_list: list[str]) -> dict[str, int]:
    """Given a list of strings, function produces a dictionary [str, int] where each key is a unique element in the given list and each associated value is the count of the number of times that value appeared in the input list. In other words, a dictionary of the counts of each of the items in the input list."""
    new_dict: dict[str, int] = {}
    for index in count_input_list:
        if index in new_dict:
            new_dict[index] += 1
        else:
            if index not in new_dict:
                new_dict[index] = 1
    return new_dict


print(count(count_input_list))