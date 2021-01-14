# --- Day 6: Probably a Fire Hazard ---
# Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.
#
# Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.
#
# Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0.
# The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs.
# Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square.
# The lights all start turned off.
#
# To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.
#
# For example:
#
# turn on 0,0 through 999,999 would turn on (or leave on) every light.
# toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
# turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
# After following the instructions, how many lights are lit?
#

# --- Part Two ---
# You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.
#
# The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.
#
# The phrase turn on actually means that you should increase the brightness of those lights by 1.
#
# The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.
#
# The phrase toggle actually means that you should increase the brightness of those lights by 2.
#
# What is the total brightness of all lights combined after following Santa's instructions?
#
# For example:
#
# turn on 0,0 through 0,0 would increase the total brightness by 1.
# toggle 0,0 through 999,999 would increase the total brightness by 2000000.

from typing import Tuple, Union


class BrightGrid:
    def __init__(self):
        # all the lights that are currently lit
        self.lights = dict()

    @staticmethod
    def _location_range_for(start_x, start_y, end_x, end_y):
        """
        Generator for every position for the passed field (inclusive)
        """
        for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
            for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
                yield (x, y)

    def light_increase(self, light_location, amount=1):
        """
        This light is now x brighter
        """
        if light_location in self.lights:
            self.lights[light_location] += amount
        else:
            self.lights[light_location] = amount

    def light_decrease(self, light_location, amount=1):
        """
        This light is now x dimmer
        """
        if light_location in self.lights:
            self.lights[light_location] = max(0, self.lights[light_location] - amount)
        # we don't need an else here, non-set lights are automatically assumed to be 0 and so cannot be decreased

    def lit_count(self):
        """
        return how many lights are lit
        """
        return len(self.lights)

    def light_output(self):
        """
        return the total brightness of all bulbs
        """
        return sum(self.lights.values())

    def apply_grid(self, start_x, start_y, end_x, end_y, action, amount):
        for this_location in self._location_range_for(start_x, start_y, end_x, end_y):
            action(this_location, amount)

    def turn_on(self, start_x, start_y, end_x, end_y):
        """
        Turn on each light in the specified locations
        """
        self.apply_grid(start_x, start_y, end_x, end_y, self.light_increase, 1)

    def turn_off(self, start_x, start_y, end_x, end_y):
        """
        Turn off each light in the specified locations
        """
        self.apply_grid(start_x, start_y, end_x, end_y, self.light_decrease, 1)

    def toggle(self, start_x, start_y, end_x, end_y):
        """
        Turn on each light in the specified locations
        """
        self.apply_grid(start_x, start_y, end_x, end_y, self.light_increase, 2)


class LightGrid:
    def __init__(self):
        # all the lights that are currently lit
        self.lights = set()

    @staticmethod
    def _location_range_for(start_x, start_y, end_x, end_y):
        """
        Generator for every position for the passed field (inclusive)
        """
        for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
            for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
                yield (x, y)

    def light_on(self, light_location):
        """
        This light is now on
        """
        self.lights.add(light_location)

    def light_off(self, light_location):
        """
        This light is now off
        """
        if light_location in self.lights:
            self.lights.remove(light_location)

    def light_toggle(self, light_location):
        """
        Change the current state of this..
        """
        if light_location in self.lights:
            self.lights.remove(light_location)
        else:
            self.lights.add(light_location)

    def lit_count(self):
        """
        return how many lights are lit
        """
        return len(self.lights)

    def apply_grid(self, start_x, start_y, end_x, end_y, action):
        for this_location in self._location_range_for(start_x, start_y, end_x, end_y):
            action(this_location)

    def turn_on(self, start_x, start_y, end_x, end_y):
        """
        Turn on each light in the specified locations
        """
        self.apply_grid(start_x, start_y, end_x, end_y, self.light_on)

    def turn_off(self, start_x, start_y, end_x, end_y):
        """
        Turn off each light in the specified locations
        """
        self.apply_grid(start_x, start_y, end_x, end_y, self.light_off)

    def toggle(self, start_x, start_y, end_x, end_y):
        """
        Turn on each light in the specified locations
        """
        self.apply_grid(start_x, start_y, end_x, end_y, self.light_toggle)


def range_split(s: str) -> Tuple[int, int]:
    """
    takes a string 123,456 and return a tuple 123, 456 as ints
    """
    idx = s.find(",")
    a = int(s[:idx])
    b = int(s[idx + 1 :])
    return a, b


def apply_one_line_to_grid(grid: Union[LightGrid, BrightGrid], instruction: str):
    """
    Apply a single instruction to the X-Grid
    instruction must be one of:
    turn on 1,2 through 3,4
    turn off 1,2 through 3,4
    toggle 1,2 through 3,4
    """

    # split the line into the coordinates (which are always the same) and the instruction, which is weird..
    words = instruction.split(" ")
    through = words.index("through")
    range1 = words[through - 1]
    range2 = words[through + 1]
    x1, y1 = range_split(range1)
    x2, y2 = range_split(range2)
    # print(f"words: {words}, -> {range1},{range2} -> {x1}-{y1}-{x2}-{y2}")

    # now figure out which instruction we're dealing with and apply the command
    if instruction.startswith("turn on"):
        grid.turn_on(x1, y1, x2, y2)
    elif instruction.startswith("turn off"):
        grid.turn_off(x1, y1, x2, y2)
    elif instruction.startswith("toggle"):
        grid.toggle(x1, y1, x2, y2)
    else:
        raise ValueError(f"What the hell kind of command is {instruction} ?")


def light_grid_from_file(filename: str) -> LightGrid:
    """
    Return a LightGrid object configured per the instructions in the file
    """
    the_grid = LightGrid()

    with open(filename, "r") as f:
        for this_line in f:
            this_line = this_line.strip()
            if "" != this_line:
                # handle this line
                apply_one_line_to_grid(the_grid, this_line)

    return the_grid


# there must be a smarter way to do this..
def bright_grid_from_file(filename: str) -> BrightGrid:
    """
    Return a BrightGrid object configured per the instructions in the file
    """
    the_grid = BrightGrid()

    with open(filename, "r") as f:
        for this_line in f:
            this_line = this_line.strip()
            if "" != this_line:
                # handle this line
                apply_one_line_to_grid(the_grid, this_line)

    return the_grid


def main():
    print(f"2015 day_6")
    filename = "input.txt"
    grid = light_grid_from_file(filename)
    print(f"part 1: {grid.lit_count()}")
    grid2 = bright_grid_from_file(filename)
    print(f"part 2: {grid2.light_output()}")


if __name__ == "__main__":
    main()