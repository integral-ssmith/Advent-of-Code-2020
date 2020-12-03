import os
import numpy as np


def process_list_part_1(arr):
    # get the number of entries
    num_of_entries = np.array(np.char.split(arr[:, 0], '-').tolist(), dtype=int)
    min_of_entries = num_of_entries[:, 0]
    max_of_entries = num_of_entries[:, 1]
    # get the entries and passwords
    entries = np.char.rstrip(arr[:, 1], ':')
    passwords = arr[:, 2]
    # get the counts
    counts = np.array([password.count(entry) for password, entry in zip(passwords, entries)])
    # test the range for password validity
    bool_valid = np.logical_and(counts >= min_of_entries, counts <= max_of_entries)
    return bool_valid


def process_list_part_2(arr):
    # get the number of entries
    pos_of_entries = np.array(np.char.split(arr[:, 0], '-').tolist(), dtype=int)
    pos_1 = pos_of_entries[:, 0] - 1
    pos_2 = pos_of_entries[:, 1] - 1
    # get the entries and passwords
    entries = np.char.rstrip(arr[:, 1], ':')
    passwords = arr[:, 2]
    # check if the entry is in one of the positions in the password
    bool_valid = np.array([(password[p1] == entry) ^ (password[p2] == entry)
                           for password, entry, p1, p2 in zip(passwords, entries, pos_1, pos_2)])
    return bool_valid


if __name__ == '__main__':
    # PART 1
    # sample data
    sample_data = np.array([['1-3', 'a:', 'abcde'], ['1-3', 'b:', 'cdefg'], ['2-9', 'c:', 'ccccccccc']])
    sample_answer = np.array([True, False, True])
    calculated_sample_answer = process_list_part_1(sample_data)
    assert np.all(calculated_sample_answer == sample_answer)
    # test data
    test_data = np.loadtxt(r'data/day_2_input.txt', dtype=str)
    calculated_answer = process_list_part_1(test_data)
    print('Part 1: %i of %i passwords are valid' % (np.sum(calculated_answer), len(calculated_answer)))

    # PART 2
    # sample data
    sample_answer = np.array([True, False, False])
    calculated_sample_answer = process_list_part_2(sample_data)
    assert np.all(calculated_sample_answer == sample_answer)
    # test data
    calculated_answer = process_list_part_2(test_data)
    print('Part 2: %i of %i passwords are valid' % (np.sum(calculated_answer), len(calculated_answer)))
