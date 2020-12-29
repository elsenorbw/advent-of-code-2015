# testing the part1 code..
import pytest

from day1_part2 import when_do_we_enter_the_basement


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (")", 1),
        ("()())", 5),
        ("(((", None),
        ("(()(()(", None),
    ],
)
def test_when_do_we_enter_the_basement(test_input, expected):
    """
    Check that the basement_entry function does what is expected
    """
    actual = when_do_we_enter_the_basement(test_input)
    assert actual == expected
