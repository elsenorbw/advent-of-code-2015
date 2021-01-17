import pytest

from day7 import mask_to_bits, LogicNode, LogicBoard


def test_LogicBoard():
    """
    Run the given example in the logic board
    """
    board = LogicBoard()
    instructions = [
        "123 -> x",
        "456 -> y",
        "x AND y -> d",
        "x OR y -> e",
        "x LSHIFT 2 -> f",
        "y RSHIFT 2 -> g",
        "NOT x -> h",
        "NOT y -> i",
    ]
    for this_instruction in instructions:
        board.add_one_instruction(this_instruction)

    expected_results = [
        ("d", 72),
        ("e", 507),
        ("f", 492),
        ("g", 114),
        ("h", 65412),
        ("i", 65079),
        ("x", 123),
        ("y", 456),
    ]

    for node_name, expected_val in expected_results:
        assert board.provide_for(node_name) == expected_val


@pytest.mark.parametrize(
    "input_a, input_b, expected_value",
    [(456, 2, 114), (4, 1, 2), (4, 2, 1), (4, 3, 0)],
)
def test_LogicNode_RSHIFT(input_a, input_b, expected_value):
    node = LogicNode("test_node")
    node.configure(LogicNode.RSHIFT, input_a, input_b)
    actual = node.provide()
    assert actual == expected_value


@pytest.mark.parametrize(
    "input_a, input_b, expected_value",
    [(123, 2, 492), (1, 1, 2), (2, 1, 4), (1, 17, 0)],
)
def test_LogicNode_LSHIFT(input_a, input_b, expected_value):
    node = LogicNode("test_node")
    node.configure(LogicNode.LSHIFT, input_a, input_b)
    actual = node.provide()
    assert actual == expected_value


@pytest.mark.parametrize(
    "input_a, input_b, expected_value",
    [(1, 1, 1), (1, 0, 1), (2, 2, 2), (1, 2, 3), (1, 3, 3), (7, 2, 7), (4, 2, 6)],
)
def test_LogicNode_OR(input_a, input_b, expected_value):
    node = LogicNode("test_node")
    node.configure(LogicNode.OR, input_a, input_b)
    actual = node.provide()
    assert actual == expected_value


@pytest.mark.parametrize(
    "input_a, input_b, expected_value",
    [(1, 1, 1), (1, 0, 0), (2, 2, 2), (1, 2, 0), (1, 3, 1), (7, 2, 2)],
)
def test_LogicNode_AND(input_a, input_b, expected_value):
    node = LogicNode("test_node")
    node.configure(LogicNode.AND, input_a, input_b)
    actual = node.provide()
    assert actual == expected_value


@pytest.mark.parametrize(
    "input_a, input_b, expected_value",
    [(0, None, 65535), (65535, None, 0), (123, None, 65412), (456, None, 65079)],
)
def test_LogicNode_NOT(input_a, input_b, expected_value):
    node = LogicNode("test_node")
    node.configure(LogicNode.NOT, input_a, input_b)
    actual = node.provide()
    assert actual == expected_value


@pytest.mark.parametrize(
    "input_a, input_b, expected_value",
    [(123, None, 123), (456, None, 456), (789, None, 789)],
)
def test_LogicNode_NOP(input_a, input_b, expected_value):
    node = LogicNode("test_node")
    node.configure(LogicNode.NOP, input_a, input_b)
    actual = node.provide()
    assert actual == expected_value


@pytest.mark.parametrize(
    "input_val, expected", [(0, 0), (65535, 65535), (65536, 0), (456, 456)]
)
def test_mask_to_bits(input_val, expected):
    actual = mask_to_bits(16, input_val)
    assert actual == expected