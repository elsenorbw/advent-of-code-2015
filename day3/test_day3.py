import pytest

from day3_part1 import DeliveryMap
from day3_part2 import RoboDeliveryMap


@pytest.mark.parametrize(
    "test_input,expected", [("<<<", 4), ("^>v<", 4), (">", 2), ("^v^v^v^v^v", 2)]
)
def test_delivery_map(test_input, expected):
    """
    confirm that the correct number of presents are recorded
    """
    dm = DeliveryMap()
    dm.apply_moves(test_input)
    actual = dm.houses_visited()
    assert actual == expected


@pytest.mark.parametrize(
    "test_input,expected", [("<<<", 3), ("^>v<", 3), (">", 2), ("^v^v^v^v^v", 11)]
)
def test_robo_delivery_map(test_input, expected):
    """
    confirm that the correct number of presents are recorded
    """
    rdm = RoboDeliveryMap()
    rdm.apply_moves(test_input)
    actual = rdm.houses_visited()
    assert actual == expected
