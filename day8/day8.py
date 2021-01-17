# --- Day 8: Matchsticks ---
# Space on the sleigh is limited this year, and so Santa will be bringing his list as a digital copy. He needs to know how much space it will take up when stored.
#
# It is common in many programming languages to provide a way to escape special characters in strings.
# For example, C, JavaScript, Perl, Python, and even PHP handle special characters in very similar ways.
#
# However, it is important to realize the difference between the number of characters in the code representation of the string literal and the number of characters in the in-memory string itself.
#
# For example:
#
# "" is 2 characters of code (the two double quotes), but the string contains zero characters.
# "abc" is 5 characters of code, but 3 characters in the string data.
# "aaa\"aaa" is 10 characters of code, but the string itself contains six "a" characters and a single, escaped quote character, for a total of 7 characters in the string data.
# "\x27" is 6 characters of code, but the string itself contains just one - an apostrophe ('), escaped using hexadecimal notation.
# Santa's list is a file that contains many double-quoted string literals, one on each line.
# The only escape sequences used are \\ (which represents a single backslash), \" (which represents a lone double-quote character),
# and \x plus two hexadecimal characters (which represents a single character with that ASCII code).
#
# Disregarding the whitespace in the file, what is the number of characters of code for string literals minus the
# number of characters in memory for the values of the strings in total for the entire file?
#
# For example, given the four strings above, the total number of characters of string code (2 + 5 + 10 + 6 = 23) minus the total number
# of characters in memory for string values (0 + 3 + 7 + 1 = 11) is 23 - 11 = 12.
#
# To begin, get your puzzle input.
#

# so far, so simple, just parse a given string and return the size of the string that would be generated
# going to write an interpreted_length function as a starter for 10


def interpreted_length(s: str) -> int:
    """
    interpret an escaped string to remove the length
    """
    # so the string must start and end with a quote
    if not s.startswith('"') or not s.endswith('"'):
        raise ValueError(f"Call this a string ? [{s}]")

    # chop out the bit to parse
    s = s[1:-1]

    # run through the string counting the printable characters
    output_char_count = 0
    idx = 0
    while idx < len(s):
        # is this a backslash ?
        if "\\" == s[idx]:
            # handle the next character
            idx += 1
            if "x" == s[idx]:
                idx += 2
        # and whatever happened, this is worth one character
        output_char_count += 1
        idx += 1

    # and we're done
    return output_char_count


def encoded_length(s: str) -> int:
    """
    return the length of code that would be required to encode the input string
    """
    # so we will need to add quotes around the outside
    output_char_count = 2

    for this_char in s:
        if this_char in '\\"':
            output_char_count += 2
        else:
            output_char_count += 1

    return output_char_count


def part1(filename: str) -> int:
    """
    return the difference between the source and interpreted string lengths
    """
    raw_length = 0
    cooked_length = 0

    with open(filename, "r") as f:
        for this_line in f:
            this_line = this_line.strip()
            if "" != this_line:
                raw_length += len(this_line)
                cooked_length += interpreted_length(this_line)

    return raw_length - cooked_length


def part2(filename: str) -> int:
    """
    return the difference between the source and encoded string lengths
    """
    raw_length = 0
    encoded_total = 0

    with open(filename, "r") as f:
        for this_line in f:
            this_line = this_line.strip()
            if "" != this_line:
                raw_length += len(this_line)
                encoded_total += encoded_length(this_line)

    return encoded_total - raw_length


def main():
    """
    get the file in and for each string calculate the lengths
    """
    filename = "input.txt"
    p1 = part1(filename)
    print(f"part1: {p1}")
    p2 = part2(filename)
    print(f"part2: {p2}")


if __name__ == "__main__":
    main()