from copy import deepcopy
import numpy as np


def process_data_part_1(a):
    # split the instruction and number
    a_instructions = np.array([i.split(' ')[0] for i in a])
    a_number = np.array([int(i.split(' ')[1]) for i in a])
    # initialize variables
    acc = 0
    executed_list = []
    current_index = 0
    while current_index not in executed_list and len(executed_list) != len(a):
        # add instruction as executed
        executed_list.append(current_index)
        # get the instruction
        current_instruction = a_instructions[current_index]
        current_number = a_number[current_index]
        # execute the instruction
        if current_instruction == 'nop':
            current_index += 1
        elif current_instruction == 'acc':
            current_index += 1
            acc += current_number
        elif current_instruction == 'jmp':
            current_index += current_number
        else:
            raise ValueError('Unknown instruction: %s' % current_instruction)
    return acc


def process_data_part_2(a):
    # split the instruction and number
    a_instructions = np.array([i.split(' ')[0] for i in a])
    a_number = np.array([int(i.split(' ')[1]) for i in a])
    # get the location of nop and jmp instructions, filtering nop with +0 because they create infinite loops
    loc_nop = np.where(np.logical_and(a_instructions == 'nop', a_number != 0))[0]
    loc_jmp = np.where(a_instructions == 'jmp')[0]
    # define the target termination index
    index_termination = len(a_instructions)
    # test changing nop to jmp
    nop_change_index = None
    if np.any(loc_nop):
        for index_change in loc_nop:
            a_instructions_copy = deepcopy(a_instructions)
            a_instructions_copy[index_change] = 'jmp'
            if get_termination_index(a_instructions_copy, a_number) == index_termination:
                nop_change_index = index_change
                break
    # test changing jmp to nop
    jmp_change_index = None
    if nop_change_index is None:
        for index_change in loc_jmp:
            a_instructions_copy = deepcopy(a_instructions)
            a_instructions_copy[index_change] = 'nop'
            if get_termination_index(a_instructions_copy, a_number) == index_termination:
                jmp_change_index = index_change
                break
    # change the instruction
    a_instructions_fixed = deepcopy(a_instructions)
    if nop_change_index is not None:
        a_instructions_fixed[nop_change_index] = 'jmp'
    else:
        a_instructions_fixed[jmp_change_index] = 'nop'
    # get the accumulator count
    acc = 0
    executed_list = []
    current_index = 0
    while current_index not in executed_list and len(executed_list) != len(a) and current_index != index_termination:
        # add instruction as executed
        executed_list.append(current_index)
        # get the instruction
        current_instruction = a_instructions_fixed[current_index]
        current_number = a_number[current_index]
        # execute the instruction
        if current_instruction == 'nop':
            current_index += 1
        elif current_instruction == 'acc':
            current_index += 1
            acc += current_number
        elif current_instruction == 'jmp':
            current_index += current_number
        else:
            raise ValueError('Unknown instruction: %s' % current_instruction)
    return acc


def get_termination_index(a_instructions, a_number):
    executed_list = []
    current_index = 0
    while current_index not in executed_list and len(executed_list) != len(a_instructions) and \
            0 <= current_index < len(a_instructions):
        # add instruction as executed
        executed_list.append(current_index)
        # get the instruction
        current_instruction = a_instructions[current_index]
        current_number = a_number[current_index]
        # execute the instruction
        if current_instruction in ['nop', 'acc']:
            current_index += 1
        elif current_instruction == 'jmp':
            current_index += current_number
        else:
            raise ValueError('Unknown instruction: %s' % current_instruction)
    return current_index


if __name__ == '__main__':
    # PART 1
    # sample data
    sample_data = np.array([
        'nop +0',
        'acc +1',
        'jmp +4',
        'acc +3',
        'jmp -3',
        'acc -99',
        'acc +1',
        'jmp -4',
        'acc +6'
    ])
    sample_answer = 5
    calculated_sample_answer = process_data_part_1(sample_data)
    assert sample_answer == calculated_sample_answer
    # test data
    test_data = np.loadtxt(r'data/day_8_input.txt', dtype=str, delimiter='\n')
    calculated_answer = process_data_part_1(test_data)
    print('Part 1: %i' % calculated_answer)

    # PART 2
    # sample data
    sample_data = np.array([
        'nop +0',
        'acc +1',
        'jmp +4',
        'acc +3',
        'jmp -3',
        'acc -99',
        'acc +1',
        'jmp -4',
        'acc +6'
    ])
    sample_answer = 8
    calculated_sample_answer = process_data_part_2(sample_data)
    assert sample_answer == calculated_sample_answer
    # test data
    calculated_answer = process_data_part_2(test_data)
    print('Part 2: %i' % calculated_answer)
