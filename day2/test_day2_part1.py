import pytest

from day2_part1 import parse_dimension_string, calculate_paper_required


@pytest.mark.parametrize(
    "test_input,expected", [("1x2x4", [1, 2, 4]), ("123x456x789", [123, 456, 789])]
)
def test_parse_dimension_string(test_input, expected):
    actual = parse_dimension_string(test_input)
    assert actual == expected


@pytest.mark.parametrize(
    "test_input,exception_type",
    [("abcx123x456", ValueError), ("1x2x3x4", ValueError), ("", ValueError)],
)
def test_parse_dimension_string_throws(test_input, exception_type):
    """
    All these tests should throw
    """
    with pytest.raises(exception_type):
        actual = parse_dimension_string(test_input)


@pytest.mark.parametrize("test_input,expected", [((2, 3, 4), 58), ((1, 1, 10), 43)])
def test_calculate_paper_required(test_input, expected):
    actual = calculate_paper_required(*test_input)
    assert actual == expected
