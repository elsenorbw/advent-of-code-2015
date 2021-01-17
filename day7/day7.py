# --- Day 7: Some Assembly Required ---
# This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates!
# Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.
#
# Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535).
# A signal is provided to each wire by a gate, another wire, or some specific value.
# Each wire can only get a signal from one source, but can provide its signal to multiple destinations.
# A gate provides no signal until all of its inputs have a signal.
#
# The included instructions booklet describes how to connect the parts together:
# x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.
#
# For example:
#
# 123 -> x means that the signal 123 is provided to wire x.
# x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
# p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
# NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
# Other possible gates include OR (bitwise OR) and RSHIFT (right-shift).
# If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.
#
# For example, here is a simple circuit:
#
# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i
# After it is run, these are the signals on the wires:
#
# d: 72
# e: 507
# f: 492
# g: 114
# h: 65412
# i: 65079
# x: 123
# y: 456
# In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

# so we need a collection of logic gate objects
# each one has 1 or 2 inputs
# each input is either another gate or a 16-bit integer value..
# executing a provide() function call on a logic gate should yield its output value
# node types are :
#   NOP pass-through - provide() yields the single input value
#   AND - the binary AND for two inputs
#   OR - binary OR
#   NOT - the bitwise complement (remember we're in 16-bit land here)
#   LSHIFT - Left shift value1 by value2 places
#   RSHIFT - right shift value1 by value2 places
#
# so as we go through loading the instructions, we need to be creating and attaching the nodes
# this means that sometimes we will need to attach a node as an input before we know what the hell it is
# so all nodes will start blank in the master node list, when we come to configure node ABC, we will add it to the list if missing
# if not missing that just means that it's already an input to something else..
# in either case, we then configure that node to have the appropriate types and inputs
#

# --- Part Two ---
# Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a).
# What new signal is ultimately provided to wire a?

from typing import Union, Optional


def mask_to_bits(num_bits: int, the_value: int) -> int:
    """
    Return the lowest num_bits bits of the value
    """
    mask = (1 << num_bits) - 1
    result = the_value & mask
    return result


class LogicNode:
    UNKNOWN = 42
    NOP = 1001
    AND = 1002
    OR = 1003
    NOT = 1004
    LSHIFT = 1005
    RSHIFT = 1006

    @staticmethod
    def _op_nop(a: int, b: Optional[int]) -> int:
        """
        no operation, just return what we have on input a
        """
        return a

    @staticmethod
    def _op_not(a: int, b: Optional[int]) -> int:
        """
        not operation, just return a bitwise complement of the input value
        """
        return ~a

    @staticmethod
    def _op_and(a: int, b: int) -> int:
        """
        and operation
        """
        return a & b

    @staticmethod
    def _op_or(a: int, b: int) -> int:
        """
        and operation
        """
        return a | b

    @staticmethod
    def _op_lshift(a: int, b: int) -> int:
        """
        left shift a by b places
        """
        return a << b

    @staticmethod
    def _op_rshift(a: int, b: int) -> int:
        """
        right shift a by b places
        """
        return a >> b

    @staticmethod
    def _resolve_value(v, depth: int) -> int:
        if v is None:
            return 0
        if isinstance(v, int):
            return v
        else:
            # assume it's a LogicNode..
            return v.provide(depth + 1)

    def clear_answer(self):
        """
        removed any cached values to allow for re-calculation
        """
        self.node_value = None

    def __init__(self, node_id: str):
        """
        configure the node as dumb / unknown
        """
        self.id = node_id
        self.node_type = LogicNode.UNKNOWN
        self.value1 = None
        self.value2 = None
        self.node_value = None

    def operator_name(self) -> str:
        """
        Return a string deescribing the current operator
        """
        op_strings = {
            LogicNode.UNKNOWN: "Not Configured",
            LogicNode.NOP: "Pass-through",
            LogicNode.AND: "Bitwise AND",
            LogicNode.OR: "Bitwise OR",
            LogicNode.NOT: "Bitwise NOT",
            LogicNode.LSHIFT: "Left Shift",
            LogicNode.RSHIFT: "Right Shift",
        }
        result = f"WTF!?!->{self.node_type}"
        if self.node_type in op_strings:
            result = op_strings[self.node_type]
        return result

    def configure(self, node_type, value1, value2=None):
        """
        Allow ourselves to be configured to do something useful
        """
        self.node_type = node_type
        self.value1 = value1
        self.value2 = value2

    def __str__(self) -> str:
        """
        Return a nice string representation of the node
        """
        s = f"<LogicNode ({self.id}) {self.operator_name()} {self.value1}, {self.value2}>"
        return s

    def provide(self, depth=1) -> int:
        """
        Provide the output of this logic node
        """
        # if we've done this work before then we can remember..
        if self.node_value is not None:
            return self.node_value

        a = LogicNode._resolve_value(self.value1, depth)
        b = LogicNode._resolve_value(self.value2, depth)

        logic_operations = {
            LogicNode.NOP: LogicNode._op_nop,
            LogicNode.AND: LogicNode._op_and,
            LogicNode.OR: LogicNode._op_or,
            LogicNode.NOT: LogicNode._op_not,
            LogicNode.LSHIFT: LogicNode._op_lshift,
            LogicNode.RSHIFT: LogicNode._op_rshift,
        }

        # get the operation
        if self.node_type not in logic_operations:
            raise RuntimeError(
                f"Attempting to provide() on a node ({self.id}) of type {self.node_type} - not supported"
            )
        the_operation = logic_operations[self.node_type]

        # call the operation providing the two values
        result = the_operation(a, b)

        # ensure that we're within 16 bits..
        result = mask_to_bits(16, result)

        # store for next time..
        self.node_value = result

        # return the value
        return result


class LogicBoard:
    def __init__(self):
        """
        Initialise an empty board
        """
        self.nodes = dict()

    def add_one_instruction(self, instruction: str):
        """
        Add one instruction to the board
        instructions look like one of:
            123 -> x
            x AND y -> d
            x LSHIFT 2 -> f
            NOT x -> h
        """
        # so in this case we are creating the node on the rhs of ->
        # we need to understand the lhs, numerics are constants but strings are other node references
        # we need to wire up this node appropriately to those source nodes
        # initial thought, split the lhs on spaces, 1 item is a NOP, 2 items are a NOT, 3 items need to identify the middle one for the operation
        # sounds good, let's try
        sides = instruction.split("->")
        if len(sides) != 2:
            raise ValueError(
                f"Cannot perform the initial split on this instruction: {instruction}"
            )
        lhs = sides[0].strip()
        target_node_name = sides[1].strip()
        # ok, we have the lhs.. let's split it and trim it and lose any double spaces
        components = [x.strip() for x in lhs.split(" ") if x.strip() != ""]

        # right, we can use some sneaky logic here to do things just once..
        # step 1 - identify the operation node and the a/b nodes
        if 1 == len(components):
            # NOP
            action = "NOP"
            a = components[0]
            b = None
        elif 2 == len(components):
            # NOT x
            action = components[0]
            a = components[1]
            b = None
        else:
            # anything else a OP b
            action = components[1]
            a = components[0]
            b = components[2]

        # step 2, turn the a and b widgets into either nodes or integer values
        if a is not None:
            if a[0] in "0123456789":
                # it's an int
                a = int(a)
            else:
                # we need to find / create a node..
                if a not in self.nodes:
                    self.nodes[a] = LogicNode(a)
                a = self.nodes[a]
        if b is not None:
            if b[0] in "0123456789":
                b = int(b)
            else:
                if b not in self.nodes:
                    self.nodes[b] = LogicNode(b)
                b = self.nodes[b]
        # ok, so now we have an action and two either nodes or ints..
        # print(f"ins: {instruction}, a={a}, b={b}, op={action}")
        # we need to add this node if necessary
        if target_node_name not in self.nodes:
            self.nodes[target_node_name] = LogicNode(target_node_name)
        target_node = self.nodes[target_node_name]

        # and configure it
        op_values = {
            "NOP": LogicNode.NOP,
            "OR": LogicNode.OR,
            "NOT": LogicNode.NOT,
            "AND": LogicNode.AND,
            "LSHIFT": LogicNode.LSHIFT,
            "RSHIFT": LogicNode.RSHIFT,
        }
        target_node.configure(op_values[action], a, b)
        print(f"ins: {instruction}")

    def load_from_file(self, filename: str):
        """
        Read a file full of wiring instructions and add them to the current board
        """
        with open(filename, "r") as f:
            for this_line in f:
                this_line = this_line.strip()
                if "" != this_line:
                    # this must be an instruction, let's run it..
                    self.add_one_instruction(this_line)

    def recalculate(self):
        """
        remove any cached answers for logic nodes on the board
        """
        for this_node in self.nodes.values():
            this_node.clear_answer()

    def provide_for(self, node_name: str):
        """
        return the value for requested node
        """
        return self.nodes[node_name].provide()

    def print_values(self):
        """
        output all the current values for each node
        """
        print(f"Summary of values")
        for this_node in sorted(self.nodes.keys()):
            print(f"{this_node}: {self.nodes[this_node].provide()}")


def main():
    filename = "input.txt"
    board = LogicBoard()
    board.load_from_file(filename)
    board.print_values()
    part1 = board.provide_for("a")
    print(f"part 1, wire a has a value of {part1}")

    # part 2
    command = f"{part1} -> b"
    board.add_one_instruction(command)
    board.recalculate()
    part2 = board.provide_for("a")
    print(f"part 2, wire a now has a value of {part2}")


if __name__ == "__main__":
    main()