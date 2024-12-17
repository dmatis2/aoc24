with open('17.in') as f:
    regs, program = f.read().strip().split('\n\n')
    r_a, r_b, r_c = list(map(int, [n.split(': ')[1] for n in regs.split('\n')]))
    program = list(map(int, program.split(': ')[1].split(',')))

def run(a):
    b, c = 0, 0
    eip = 0
    length = len(program)
    to_print = []

    def get_combo_operand(operand):
        if 0 <= operand <= 3:
            return operand
        if operand == 4:
            return a
        if operand == 5:
            return b
        if operand == 6:
            return c
        return None

    while eip < length:
        if program[eip] == 0:
            # adv
            numerator = a
            operand = get_combo_operand(program[eip + 1])
            if operand is None:
                raise ValueError('Invalid operand')
            a = numerator // (2 ** operand)
            eip += 2
        elif program[eip] == 1:
            # bxl
            b = b ^ program[eip + 1]
            eip += 2
        elif program[eip] == 2:
            # bst
            operand = get_combo_operand(program[eip + 1])
            if operand is None:
                raise ValueError('Invalid operand')
            b = operand % 8
            eip += 2
        elif program[eip] == 3:
            # jnz
            if a != 0:
                eip = program[eip + 1]
            else:
                eip += 2
        elif program[eip] == 4:
            # bxc
            b = b ^ c
            eip += 2
        elif program[eip] == 5:
            # out
            operand = get_combo_operand(program[eip + 1])
            if operand is None:
                raise ValueError('Invalid operand')
            to_print.append(operand % 8)
            eip += 2
        elif program[eip] == 6:
            # bdv
            numerator = a
            operand = get_combo_operand(program[eip + 1])
            if operand is None:
                raise ValueError('Invalid operand')
            b = numerator // (2 ** operand)
            eip += 2
        elif program[eip] == 7:
            # cdv
            numerator = a
            operand = get_combo_operand(program[eip + 1])
            if operand is None:
                raise ValueError('Invalid operand')
            c = numerator // (2 ** operand)
            eip += 2
    return to_print

print(','.join(map(str, run(r_a))))

# totally hardcoded, but it works for me! Merry XMAS!
def bruteforce(expected):
    for a in range(2672651662 * 10 ** 5, 10 ** 16):
        if run(a) == expected:
            return a
        
    
print(bruteforce(program))