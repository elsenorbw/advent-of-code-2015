#
#  pytest file for confirming functionality
#

import pytest
from day5 import (
    contains_repeated_letter_pair,
    vowel_count,
    contains_forbidden_strings,
    word_is_nice,
    word_is_new_nice,
    contains_repeated_pair,
    contains_repeated_gapped_letter_pair,
)


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("aaa", True),
        ("abcdefeghi", True),
        ("xyx", True),
        ("ab", False),
        ("", False),
        ("a", False),
        ("abcdefghijklmnopqrstuvwxyz", False),
    ],
)
def test_contains_repeated_gapped_letter_pair(test_input, expected):
    actual = contains_repeated_gapped_letter_pair(test_input)
    assert actual == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("xyxy", True),
        ("aabcdefgaa", True),
        ("aaa", False),
        ("", False),
        ("abclardyboybctaxi", True),
    ],
)
def test_contains_repeated_pair(test_input, expected):
    actual = contains_repeated_pair(test_input)
    assert actual == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("qjhvhtzxzqqjkmpb", True),
        ("xxyxx", True),
        ("uurcxstgmygtbstg", False),
        ("ieodomkazucvgmuy", False),
    ],
)
def test_word_is_new_nice(test_input, expected):
    actual = word_is_new_nice(test_input)
    assert actual == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("ugknbfddgicrmopn", True),
        ("aaa", True),
        ("jchzalrnumimnmhp", False),
        ("haegwjzuvuyypxyu", False),
        ("dvszwmarrgswjxmb", False),
    ],
)
def test_word_is_nice(test_input, expected):
    actual = word_is_nice(test_input)
    assert actual == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("abba", True),
        ("dog", False),
        ("", False),
        ("abab", True),
        ("zzzabzzz", True),
        ("zzzcdzzz", True),
        ("aaapqaaa", True),
        ("gggxyggg", True),
        ("dshaudahsdxy", True),
        ("pqdsnajdk", True),
        ("CertainlyNot", False),
    ],
)
def test_contains_forbidden_strings(test_input, expected):
    actual = contains_forbidden_strings(test_input)
    assert actual == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("aa", True),
        ("abab", False),
        ("aabjbdkjsabdjk", True),
        ("afdsisajfioii", True),
        ("abba", True),
        ("", False),
        ("a", False),
    ],
)
def test_contains_repeated_letter_pair(test_input, expected):
    actual = contains_repeated_letter_pair(test_input)
    assert actual == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("aeiou", 5),
        ("styx", 0),
        ("", 0),
        ("a", 1),
        ("e", 1),
        ("i", 1),
        ("o", 1),
        ("u", 1),
        ("zzzzza", 1),
        ("izzzzz", 1),
        ("zzzzazzzz", 1),
    ],
)
def test_vowel_count(test_input, expected):
    actual = vowel_count(test_input)
    assert actual == expected