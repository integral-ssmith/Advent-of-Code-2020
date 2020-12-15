import numpy as np
import itertools


def process_data_part_1(a):
    # dictionary to store memory data
    memory_data = {}
    # loop through the instructions
    for instruction in a:
        if instruction.startswith('mask = '):
            bit_mask = instruction[7:]
        elif instruction.startswith('mem['):
            # get memory location and write value
            mem_loc = int(instruction[4:].split(']')[0])
            mem_write_val = int(instruction.split(' = ')[-1])
            # initialize/retrieve memory location value
            if mem_loc not in list(memory_data.keys()):
                memory_data[mem_loc] = '0' * 36
            mem_current_val = memory_data[mem_loc]
            # get the bit representation of the write value
            mem_write_val_bit = '{0:036b}'.format(mem_write_val)
            # apply the mask
            mem_write_val_bit_temp = [char for char in mem_write_val_bit]
            for i in range(len(mem_write_val_bit_temp)):
                if bit_mask[i] != 'X':
                    mem_write_val_bit_temp[i] = bit_mask[i]
            mem_write_val_bit = ''.join(mem_write_val_bit_temp)
            # write to memory
            memory_data[mem_loc] = mem_write_val_bit
        else:
            raise ValueError('Unknown instruction')
    return np.sum([int(val, 2) for val in memory_data.values()])


def process_data_part_2(a):
    # dictionary to store memory data
    memory_data = {}
    # loop through the instructions
    for instruction in a:
        if instruction.startswith('mask = '):
            bit_mask = instruction[7:]
        elif instruction.startswith('mem['):
            # get memory location and write value
            mem_loc_base = '{0:036b}'.format(int(instruction[4:].split(']')[0]))
            mem_write_val = int(instruction.split(' = ')[-1])
            # apply the mask to get all memory locations possible with floating bits
            mem_write_val_bit_temp = [char for char in mem_loc_base]
            for i in range(len(mem_write_val_bit_temp)):
                if bit_mask[i] != '0':
                    mem_write_val_bit_temp[i] = bit_mask[i]
            # get a list of the potential combinations dealing with floating bits
            num_floating = np.sum(np.array(mem_write_val_bit_temp) == 'X')
            mem_locs = []
            if num_floating == 0:
                mem_locs.append(''.join(mem_write_val_bit_temp))
            else:
                # get all floating point location combinations
                loc_floating = np.where(np.array(mem_write_val_bit_temp) == 'X')[0]
                loc_combinations = []
                for len_subset in range(len(loc_floating) + 1):
                    for subset in itertools.combinations(loc_floating, len_subset):
                        loc_combinations.append(list(subset))
                # get memory addresses for each subset
                for loc_combination in loc_combinations:
                    for loc_possible in loc_floating:
                        if loc_possible in loc_combination:
                            mem_write_val_bit_temp[loc_possible] = '1'
                        else:
                            mem_write_val_bit_temp[loc_possible] = '0'
                    mem_locs.append(''.join(mem_write_val_bit_temp))
            # write to memory
            for mem_loc in mem_locs:
                memory_data[mem_loc] = mem_write_val
        else:
            raise ValueError('Unknown instruction')
    return np.array(list(memory_data.values()), dtype=np.int64).sum()


if __name__ == '__main__':
    # PART 1
    # sample data
    sample_data = np.array([
        'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
        'mem[8] = 11',
        'mem[7] = 101',
        'mem[8] = 0'
    ])
    sample_answer = 165
    calculated_sample_answer = process_data_part_1(sample_data)
    assert sample_answer == calculated_sample_answer
    # test data
    test_data = np.loadtxt(r'data/day_14_input.txt', dtype=str, comments=None, delimiter='\n')
    calculated_answer = process_data_part_1(test_data)
    print('Part 1: %i' % calculated_answer)

    # PART 2
    # sample data
    sample_data = np.array([
        'mask = 000000000000000000000000000000X1001X',
        'mem[42] = 100',
        'mask = 00000000000000000000000000000000X0XX',
        'mem[26] = 1'
    ])
    sample_answer = 208
    calculated_sample_answer = process_data_part_2(sample_data)
    assert sample_answer == calculated_sample_answer
    # test data
    calculated_answer = process_data_part_2(test_data)
    print('Part 2: %i' % calculated_answer)
