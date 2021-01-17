import pytest

from day8 import interpreted_length, encoded_length


@pytest.mark.parametrize(
    "input, expected",
    [
        ('""', 6),
        ('"abc"', 9),
        ('"aaa\\"aaa"', 16),
    ],
)
def test_encoded_length(input, expected):
    actual = encoded_length(input)
    assert actual == expected


@pytest.mark.parametrize(
    "input, expected", [('""', 0), ('"abc"', 3), ('"aaa\\"aaa"', 7)]
)
def test_interpreted_length(input, expected):
    actual = interpreted_length(input)
    assert actual == expected