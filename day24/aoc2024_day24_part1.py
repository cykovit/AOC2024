from enum import Enum
from typing import Dict, List

class GateType(Enum):
    AND = 'AND'
    XOR = 'XOR'
    OR = 'OR'

class Gate:
    def __init__(self, input_wire_1: str, input_wire_2: str, operation: GateType, output_wire: str):
        self.input_wire_1 = input_wire_1
        self.input_wire_2 = input_wire_2
        self.operation = operation
        self.output_wire = output_wire

def parse_gate(description: str) -> Gate:
    input_wire_1, operation, input_wire_2, output_wire = description.replace("->", "").split()
    return Gate(input_wire_1, input_wire_2, GateType(operation), output_wire)

def sim_circuit(wire_values: Dict[str, bool], gates: List[Gate]) -> int:
    while gates:
        current_gate = gates.pop(0)

        if current_gate.input_wire_1 in wire_values and current_gate.input_wire_2 in wire_values:
            if current_gate.operation == GateType.AND:
                wire_values[current_gate.output_wire] = wire_values[current_gate.input_wire_1] & wire_values[current_gate.input_wire_2]
            elif current_gate.operation == GateType.XOR:
                wire_values[current_gate.output_wire] = wire_values[current_gate.input_wire_1] ^ wire_values[current_gate.input_wire_2]
            elif current_gate.operation == GateType.OR:
                wire_values[current_gate.output_wire] = wire_values[current_gate.input_wire_1] | wire_values[current_gate.input_wire_2]
        else:
            gates.append(current_gate)

    output_signals = sorted(
        ((wire, value) for wire, value in wire_values.items() if wire.startswith("z")), reverse=True
    )
    return int("".join("1" if value else "0" for _, value in output_signals), 2)

file_path = "./input_day24.txt"
with open(file_path, "r") as f:
    wiring_data, gate_data = f.read().split("\n\n")

wire_values = {
    wire[:-1]: val == "1" for wire, val in (line.split() for line in wiring_data.splitlines())
}

gates = [parse_gate(line) for line in gate_data.splitlines()]
solve_part1 = sim_circuit(wire_values, gates)

print(solve_part1)
