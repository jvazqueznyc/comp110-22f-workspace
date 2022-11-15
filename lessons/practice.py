"""Write a function called odd_and_even. Given a list of ints, odd_and_even should return a new list containing the elements that are odd and have an even index.
Example Usage:."""

def not_mask(mask: list[bool]) -> list[bool]:
  result: list[bool] = []
  for item in mask:
    result.append(not item)
  return result

mask_a: list[bool] = less_than(col_data["high"], 80)
mask_b: list[bool] = not_mask(mask_a)

values: list[float] = masked(col_data["low"], mask_b)
print(mean(values))