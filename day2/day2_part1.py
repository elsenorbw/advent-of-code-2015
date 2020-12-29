# --- Day 2: I Was Told There Would Be No Math ---
# The elves are running low on wrapping paper, and so they need to submit an order for more.
# They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.
#
# Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier:
# find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l.
# The elves also need a little extra paper for each present: the area of the smallest side.
#
# For example:
#
# A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
# A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
# All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
#
# To begin, get your puzzle input.
from typing import List


def calculate_paper_required(l: int, w: int, h: int) -> int:
    """
    How much paper do we need for a present of length, width, and height specified ?
    There are :
    2 sides of l*w
    2 sides of w*h
    2 sides of l*h
    + slack of 1 x the smallest side
    """
    sides = (l * w, w * h, l * h)
    present_total = sum([2 * x for x in sides])
    slack = min(sides)
    result = present_total + slack
    return result


def parse_dimension_string(s: str) -> List[int]:
    """
    given an input of 123x456x789 return [123, 456, 789]
    if there are not exactly 3 dimensions then we will throw
    non-integer values, we will throw
    """
    dimensions = [int(x) for x in s.split("x")]
    if len(dimensions) != 3:
        raise ValueError(f"We have a weird number of dimensions for this : {s}")
    return dimensions


def calculate_paper_for_all_gifts(filename: str) -> int:
    """
    Given a file of d1xd2xd3 lines, add up the paper required for each one
    """
    paper_for_all_gifts = 0
    with open(filename, "r") as f:
        for this_line in f:
            this_line = this_line.strip()
            if this_line != "":
                # got a line to process
                dimensions = parse_dimension_string(this_line)
                # get the value
                paper_for_this_gift = calculate_paper_required(*dimensions)
                # and update the total
                paper_for_all_gifts += paper_for_this_gift
    return paper_for_all_gifts


if __name__ == "__main__":
    filename = "input.txt"
    part1_answer = calculate_paper_for_all_gifts(filename)
    print(f"Part 1 answer is {part1_answer}")