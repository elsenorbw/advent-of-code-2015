# testing the part1 code..
import pytest

from day1_part1 import floor_result


def pytest_report_header(config):
    """
    return a header for the report
    """
    return f"flibble: AOC 2015 basic testing"


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
    ],
)
def test_floor_result(test_input, expected):
    """
    Check that the floor result function does what is expected
    """
    actual = floor_result(test_input)
    assert actual == expected
