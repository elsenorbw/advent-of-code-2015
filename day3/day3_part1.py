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


class DeliveryMap:
    def __init__(self):
        self.delivered = set([(0, 0)])
        self.x = 0
        self.y = 0

    def apply_one_move(self, the_move):
        """
        move according to the character provided
        """
        move_effect = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}
        if the_move not in move_effect:
            raise ValueError(f"Unsure what to do with a move of [{the_move}]")
        x_increment, y_increment = move_effect[the_move]
        self.x += x_increment
        self.y += y_increment
        self.delivered.add((self.x, self.y))

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
    dm = DeliveryMap()
    dm.apply_moves(moves)
    part1_result = dm.houses_visited()
    print(f"Part 1 result: {part1_result}")
