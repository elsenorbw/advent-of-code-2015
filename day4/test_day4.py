#
#  tests for the function that we're using in day4
#

import pytest
from day4 import hash_for_key, find_lowest_matching_hash_for_key


@pytest.mark.parametrize(
    "test_value, expected",
    [
        ("abcd123", "79CFEB94595DE33B3326C06AB1C7DBDA"),
        ("CaptainFlibbleSaysHello", "7B9B056E4BFCC87CF81A3BA68D464357"),
        ("1234567890", "E807F1FCF82D132F9BB018CA6738A19F"),
    ],
)
def test_hash_for_key(test_value, expected):
    """
    check that the function returns the result expected
    """
    actual = hash_for_key(test_value)
    assert actual.casefold() == expected.casefold()


@pytest.mark.parametrize(
    "test_value,expected", [("abcdef", 609043), ("pqrstuv", 1048970)]
)
def test_find_lowest_matching_hash_for_key(test_value, expected):
    """
    it's testing buddy... you know.. for safety ?
    """
    actual = find_lowest_matching_hash_for_key(test_value)
    assert actual == expected
