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

    if opcode == 0:  ## adv: division, result stored in register A
        denominator = 2 ** combo_op(operand)
        registers["A"] //= denominator
        instruction_pointer += 2

    elif opcode == 1:  ## bxl: bitwise XOR with literal operand, result stored in register B
        registers["B"] ^= literal_op(operand)
        instruction_pointer += 2

    elif opcode == 2:  ## bst: modulo 8 of combo operand, result stored in register B
        registers["B"] = combo_op(operand) % 8
        instruction_pointer += 2

    elif opcode == 3:  ## jnz: jump to literal operand if register A is not 0
        if registers["A"] != 0:
            instruction_pointer = literal_op(operand)
        else:
            instruction_pointer += 2

    elif opcode == 4:  ## bxc: bitwise XOR of register B and C, result stored in register B
        registers["B"] ^= registers["C"]
        instruction_pointer += 2

    elif opcode == 5:  ## out: modulo 8 of combo operand, output result
        output = combo_op(operand) % 8
        instruction_pointer += 2

    elif opcode == 6:  ## bdv: division, result stored in register B
        denominator = 2 ** combo_op(operand)
        registers["B"] = registers["A"] // denominator
        instruction_pointer += 2

    elif opcode == 7:  ## cdv: division, result stored in register C
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

solve_part1 = ",".join(map(str, sim(registers["A"])))
print(solve_part1)
