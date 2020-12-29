# --- Day 1: Not Quite Lisp ---
# Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and he's fresh out!
# To save Christmas, he needs you to collect fifty stars by December 25th.
#
# Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the Advent calendar;
# the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
#
# Here's an easy puzzle to warm you up.
#
# Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing.
# He starts on the ground floor (floor 0) and then follows the instructions one character at a time.
#
# An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.
#
# The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.
#
# For example:
#
# (()) and ()() both result in floor 0.
# ((( and (()(()( both result in floor 3.
# ))((((( also results in floor 3.
# ()) and ))( both result in floor -1 (the first basement level).
# ))) and )())()) both result in floor -3.
# To what floor do the instructions take Santa?
#
# To begin, get your puzzle input.


def floor_result(instructions: str, current_floor=0) -> int:
    """
    Return the finishing floor given a starting floor and some instructions.
    ( -> go up a floor
    ) -> go down a floor
    """
    for this_char in instructions.strip():
        if ")" == this_char:
            current_floor -= 1
        elif "(" == this_char:
            current_floor += 1
        else:
            raise RuntimeError(f"No idea what to do with this character -> {this_char}")
    return current_floor


def load_file_to_single_string(filename: str) -> str:
    """
    Load and concatenate each space-trimmed line into a single string
    blank lines are ignored
    """
    result = ""
    with open(filename, "r") as f:
        for this_line in f:
            this_line = this_line.strip()
            if "" != this_line:
                result += this_line
    return result


# main
if __name__ == "__main__":
    filename = "input.txt"
    instructions = load_file_to_single_string(filename)
    part1_answer = floor_result(instructions)
    print(f"Part 1 answer is {part1_answer}")
