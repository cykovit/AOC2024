import os
from enum import Enum
from typing import List, Dict, Optional

class GateType(Enum):
    AND = 'AND'
    XOR = 'XOR'
    OR = 'OR'

class LogicGate:
    def __init__(self, input_wire_1: str, input_wire_2: str, gate_type: GateType, output_wire: str):
        self.input_wire_1 = input_wire_1
        self.input_wire_2 = input_wire_2
        self.gate_type = gate_type
        self.output_wire = output_wire

    def from_line(line: str) -> "LogicGate":
        inputs, output = line.replace('->', '').split()[:-1], line.split()[-1]
        return LogicGate(inputs[0], inputs[2], GateType(inputs[1]), output)

    def contains(self, wire: str) -> bool:
        return wire in (self.input_wire_1, self.input_wire_2)

    def alt_input(self, known_wire: str) -> str:
        return self.input_wire_1 if known_wire == self.input_wire_2 else self.input_wire_2

def find_gate_by_wire(gates: List[LogicGate], gate_type: GateType, wire_id: str) -> Optional[LogicGate]:
    return next((gate for gate in gates if gate.gate_type == gate_type and gate.contains(wire_id)), None)

def id_swapped_wires(gates: List[LogicGate]) -> str:
    swapped_wires = []
    carry_wire, bit_index = find_gate_by_wire(gates, GateType.AND, 'x00').output_wire, 0

    while len(swapped_wires) < 8:
        bit_index += 1
        x_wire, z_wire = f"x{bit_index:02}", f"z{bit_index:02}"

        temp_1 = find_gate_by_wire(gates, GateType.XOR, x_wire).output_wire
        temp_2 = find_gate_by_wire(gates, GateType.AND, carry_wire).output_wire
        temp_3 = find_gate_by_wire(gates, GateType.AND, x_wire).output_wire
        xor_gate = find_gate_by_wire(gates, GateType.XOR, carry_wire)
        or_gate = find_gate_by_wire(gates, GateType.OR, temp_2) or find_gate_by_wire(gates, GateType.OR, temp_3)
        temp_1_expected = xor_gate.alt_input(carry_wire)
        carry_wire = or_gate.output_wire

        if temp_1 != temp_1_expected:
            swapped_wires.append(temp_1)
        if xor_gate.output_wire != z_wire:
            swapped_wires.append(xor_gate.output_wire)
        if not or_gate.contains(temp_2):
            swapped_wires.append(temp_2)
        if not or_gate.contains(temp_3):
            swapped_wires.append(temp_3)
        if carry_wire in (temp_1_expected, z_wire):
            swapped_wires.append(carry_wire)
            carry_wire = swapped_wires[-2]

    return ",".join(sorted(swapped_wires))

file_path = "./input_day24.txt"
with open(file_path, "r") as f:
    _, circuit_blueprint = f.read().split("\n\n")

gates = [LogicGate.from_line(line) for line in circuit_blueprint.splitlines()]
solve_part2 = id_swapped_wires(gates)
print(solve_part2)
