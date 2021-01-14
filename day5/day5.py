# --- Day 5: Doesn't He Have Intern-Elves For This? ---
# Santa needs help figuring out which strings in his text file are naughty or nice.
#
# A nice string is one with all of the following properties:
#
# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
# For example:
#
# ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
# aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
# jchzalrnumimnmhp is naughty because it has no double letter.
# haegwjzuvuyypxyu is naughty because it contains the string xy.
# dvszwmarrgswjxmb is naughty because it contains only one vowel.
# How many strings are nice?
#
# To begin, get your puzzle input.
from typing import List


def contains_repeated_letter_pair(s: str) -> bool:
    """
    if there is a pair of repeated letters in the provided word then True else False
    """
    # An array of where this character matches the previous one..
    matches = [s[i] == s[i - 1] for i in range(1, len(s))]

    result = any(matches)

    return result


def contains_repeated_gapped_letter_pair(s: str) -> bool:
    """
    if there is a pair of repeated letters with any other character inbetween them in the provided word then True else False
    """
    # An array of where this character matches the previous one..
    matches = [s[i] == s[i - 2] for i in range(2, len(s))]

    result = any(matches)

    return result


def contains_repeated_pair(s: str) -> bool:
    """
    True if there is a repeated, non-overlapping pair of characters in the string
    """
    repeated = [s[idx : idx + 2] in s[idx + 2 :] for idx in range(len(s))]
    result = any(repeated)
    return result


def vowel_count(s: str) -> int:
    """
    count the number of vowels (aeiou) in the string
    """
    # an array of true false for each character position
    vowels = [c in "aeiou" for c in s]
    result = sum(vowels)

    return result


def contains_forbidden_strings(s: str) -> bool:
    """
    True if any of the forbidden strings are in the provided value
    """

    forbidden_strings = ["ab", "cd", "pq", "xy"]
    forbidden_found = [forbidden in s for forbidden in forbidden_strings]
    result = any(forbidden_found)

    return result


def word_is_nice(s: str) -> bool:
    """
    True if:
      - contains at least 3 vowels
      - at least one repeated character
      - does not contain the forbidden words
    """
    result = True

    if 3 > vowel_count(s):
        result = False
    elif not contains_repeated_letter_pair(s):
        result = False
    elif contains_forbidden_strings(s):
        result = False

    return result


def word_is_new_nice(s: str) -> bool:
    """
    True if:
    - contains one repeated pair of characters (no overlaps)
    - contains one letter which is repeated with any other character in between
    """
    result = True

    if not contains_repeated_pair(s):
        result = False
    elif not contains_repeated_gapped_letter_pair(s):
        result = False

    return result


def load_words_from_file(filename: str) -> List[str]:
    """
    Load each line as a separate word, trimmed output only
    """
    result = []

    with open(filename, "r") as f:
        for this_line in f:
            this_line = this_line.strip()
            if "" != this_line:
                result.append(this_line)

    return result


def count_nice_strings(word_list: List[str], eval_function=word_is_nice) -> int:
    """
    return how many of these strings match the "nice" criteria
    """
    result = 0

    for this_word in word_list:
        if eval_function(this_word):
            result += 1

    return result


def main():
    """
    The main function
    """
    filename = "input.txt"
    all_words = load_words_from_file(filename)
    print(f"All Words: {all_words}")
    part1 = count_nice_strings(all_words)
    print(f"Part 1 answer - your list contains {part1} nice words")
    part2 = count_nice_strings(all_words, eval_function=word_is_new_nice)
    print(f"Part 2 answer - your list contains {part2} new-nice words")


if __name__ == "__main__":
    # actual code
    main()