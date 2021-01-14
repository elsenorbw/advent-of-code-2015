import pytest
from day6 import LightGrid, range_split


@pytest.mark.parametrize(
    "input, expected_output",
    [("123,456", (123, 456)), ("1,2", (1, 2)), ("1234567,89", (1234567, 89))],
)
def test_range_split(input, expected_output):
    actual = range_split(input)
    assert actual == expected_output


@pytest.mark.parametrize(
    "grid_to_light, grid_to_turn_off, grid_to_toggle, expected_light_count",
    [
        ((0, 0, 1, 1), None, None, 4),
        (None, None, (0, 0, 1, 1), 4),
        ((0, 0, 1, 1), None, (-2, -2, 2, 2), 21),
        ((0, 0, 1, 1), (0, 0, 0, 1), None, 2),
    ],
)
def test_LightGrid(
    grid_to_light, grid_to_turn_off, grid_to_toggle, expected_light_count
):
    """
    check that the basic functionality for setting and unsetting grids works
    """
    lg = LightGrid()
    if grid_to_light is not None:
        lg.turn_on(*grid_to_light)
    if grid_to_turn_off is not None:
        lg.turn_off(*grid_to_turn_off)
    if grid_to_toggle is not None:
        lg.toggle(*grid_to_toggle)

    actual = lg.lit_count()
    assert actual == expected_light_count


def test_LightGrid_off_without_on():
    """
    Bug: trying to turn off a light that wasn't on raises an error, it should pass silently
    """
    lg = LightGrid()
    lg.turn_off(0, 0, 1, 1)
    assert 0 == lg.lit_count()
