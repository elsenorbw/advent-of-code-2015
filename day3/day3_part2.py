# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
# Santa is delivering presents to an infinite two-dimensional grid of houses.
#
# He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next.
# Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.
#
# However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once.
# How many houses receive at least one present?
#
# For example:
#
# > delivers presents to 2 houses: one at the starting location, and one to the east.
# ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
# ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
# To begin, get your puzzle input.

# Your puzzle answer was 2565.
#
# The first half of this puzzle is complete! It provides one gold star: *
#
# --- Part Two ---
# The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.
#
# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf,
# who is eggnoggedly reading from the same script as the previous year.
#
# This year, how many houses receive at least one present?
#
# For example:
#
# ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
# ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
# ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.`


class RoboDeliveryMap:
    def __init__(self):
        self.delivered = set([(0, 0)])
        self.santa = (0, 0)
        self.robosanta = (0, 0)
        self.next_move_is_santa = True

    def apply_one_move(self, the_move):
        """
        move according to the character provided
        """
        move_effect = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}
        if the_move not in move_effect:
            raise ValueError(f"Unsure what to do with a move of [{the_move}]")
        x_increment, y_increment = move_effect[the_move]

        # now move the correct individual
        if self.next_move_is_santa:
            x, y = self.santa
            x += x_increment
            y += y_increment
            self.santa = (x, y)
            self.delivered.add((x, y))
        else:
            x, y = self.robosanta
            x += x_increment
            y += y_increment
            self.robosanta = (x, y)
            self.delivered.add((x, y))

        # and toggle the individual
        self.next_move_is_santa = not self.next_move_is_santa

    def apply_moves(self, move_list):
        """
        apply each of the moves in the string provided
        """
        for this_move in move_list.strip():
            self.apply_one_move(this_move)

    def houses_visited(self):
        """
        how many locations have we visited at least once
        """
        return len(self.delivered)


def load_file_to_string(filename: str) -> str:
    """
    return all the lines in the file (excluding blanks), trimmed and concatenated
    """
    file_contents = ""

    with open(filename, "r") as f:
        for this_line in f:
            this_line = this_line.strip()
            if "" != this_line:
                file_contents += this_line

    return file_contents


if __name__ == "__main__":
    filename = "input.txt"
    moves = load_file_to_string(filename)
    dm = RoboDeliveryMap()
    dm.apply_moves(moves)
    part2_result = dm.houses_visited()
    print(f"Part 2 result: {part2_result}")
