data = open('input_day17.txt').readlines()
registers = {r: int(data[i].strip().split(": ")[1]) for r, i in zip("ABC", range(3))}
program = [int(d) for d in data[-1].split(": ")[1].split(",")]

def literal_op(operand):
    return operand

def combo_op(operand):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return registers["A"]
    elif operand == 5:
        return registers["B"]
    elif operand == 6:
        return registers["C"]
    elif operand == 7:
        raise Exception("Invalid operand")

def execute(opcode, operand, instruction_pointer):
    output = None

    if opcode == 0: 
        denominator = 2 ** combo_op(operand)
        registers["A"] //= denominator
        instruction_pointer += 2

    elif opcode == 1:  
        registers["B"] ^= literal_op(operand)
        instruction_pointer += 2

    elif opcode == 2: 
        registers["B"] = combo_op(operand) % 8
        instruction_pointer += 2

    elif opcode == 3:  
        if registers["A"] != 0:
            instruction_pointer = literal_op(operand)
        else:
            instruction_pointer += 2

    elif opcode == 4:  
        registers["B"] ^= registers["C"]
        instruction_pointer += 2

    elif opcode == 5:  
        output = combo_op(operand) % 8
        instruction_pointer += 2

    elif opcode == 6:
        denominator = 2 ** combo_op(operand)
        registers["B"] = registers["A"] // denominator
        instruction_pointer += 2

    elif opcode == 7:  
        denominator = 2 ** combo_op(operand)
        registers["C"] = registers["A"] // denominator
        instruction_pointer += 2

    return output, instruction_pointer

def sim(initial_a_value):
    registers["A"] = initial_a_value
    instruction_pointer = 0
    outputs = []

    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]
        output, instruction_pointer = execute(opcode, operand, instruction_pointer)

        if output is not None:
            outputs.append(output)

    return outputs

def flatten(nested_list):
    if not nested_list:
        return []
    if isinstance(nested_list[0], list):
        return flatten(nested_list[0]) + flatten(nested_list[1:])
    return [nested_list[0]] + flatten(nested_list[1:])

def minimum_register(register, index):
    if index == 16:
        return int("".join(map(str, register)))

    possible_registers = []
    for value in range(8): 
        current_register = register[:]
        current_register[index] = value
        candidate_a_value = int("".join(map(str, current_register)), 8)  

        output = sim(candidate_a_value)
        expected_output = [0] * (len(program) - len(output)) + output  

        if expected_output[-(index + 1)] == program[-(index + 1)]:
            possible_registers.append(current_register)

    return [minimum_register(r, index + 1) for r in possible_registers]

solve_part1 = ",".join(map(str, sim(registers["A"])))
minimum_register_a_value = min(flatten(minimum_register([0] * 16, 0)))
solve_part2 = int(str(minimum_register_a_value), 8)

print("Part 1 - Output:", solve_part1)
print("Part 2 - Lowest positive initial value:", solve_part2)
