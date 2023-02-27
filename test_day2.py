def run_intcode(intcode):
    for i in range(0, len(intcode), 4):
        opcode = intcode[i]
        if opcode == 99:
            return intcode
        elif opcode == 1:
            intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
        elif opcode == 2:
            intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
        else:
            raise ValueError(f'Invalid opcode: {opcode}')
    return intcode

def find_output(intcode, output):
    for noun in range(100):
        for verb in range(100):
            intcode_copy = intcode.copy()
            intcode_copy[1] = noun
            intcode_copy[2] = verb
            result = run_intcode(intcode_copy)
            if result[0] == output:
                return 100 * noun + verb
    return -1

import pytest

def test_run_intcode():
    assert run_intcode([1,0,0,0,99]) == [2,0,0,0,99]
    assert run_intcode([2,3,0,3,99]) == [2,3,0,6,99]

def test_find_output():
    intcode = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 6, 1, 19, 1, 19, 5, 23, 1, 23, 9, 27, 1, 27, 6, 31, 1, 31, 10, 35, 1, 35, 9, 39, 1, 39, 13, 43, 2, 10, 43, 47, 1, 9, 47, 51, 1, 51, 6, 55, 1, 55, 13, 59, 1, 59, 10, 63, 2, 63, 13, 67, 1, 67, 9, 71, 2, 71, 10, 75, 1, 75, 5, 79, 1, 79, 9, 83, 2, 10, 83, 87, 1, 5, 87, 91, 1, 91, 6, 95, 1, 95, 13, 99, 1, 10, 99, 103, 2, 103, 13, 107, 1, 107, 5, 111, 2, 111, 9, 115, 1, 5, 115, 119, 2, 10, 119, 123, 1, 6, 123, 127, 1, 127, 5, 131, 1, 131, 9, 135, 1, 135, 10, 139, 1, 13, 139, 143, 1, 143, 10, 147, 1]
