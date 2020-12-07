import string
import numpy as np


def process_data_part_1(a):
    alphabet = list(string.ascii_lowercase)
    counts = np.zeros(len(a))
    for i, i_a in enumerate(a):
        for j in alphabet:
            if j in i_a:
                counts[i] = counts[i] + 1
    return np.sum(counts)


def process_data_part_2(a):
    alphabet = list(string.ascii_lowercase)
    counts = np.zeros(len(a))
    for i, i_a in enumerate(a):
        i_a_split = i_a.split(' ')
        for j in alphabet:
            if np.all([j in k for k in i_a_split]):
                counts[i] = counts[i] + 1
    return np.sum(counts)


if __name__ == '__main__':
    # PART 1
    # sample data
    sample_data = np.array([
        'abc', 'abc', 'abac', 'aaaa', 'b'
    ])
    sample_answer = 11
    calculated_sample_answer = process_data_part_1(sample_data)
    assert sample_answer == calculated_sample_answer
    # test data
    test_data = []
    with open(r'data/day_6_input.txt', 'rb') as f:
        contents = f.readlines()
        current_line = ''
        for line in contents:
            line = line.decode('utf-8')
            line = line.strip('\r\n')
            if len(line) != 0:
                if len(current_line) != 0:
                    current_line = current_line + line
                else:
                    current_line = line
            else:
                test_data.append(current_line)
                current_line = ''
    if len(current_line) != 0:
        test_data.append(current_line)
    test_data = np.array(test_data)
    calculated_answer = process_data_part_1(test_data)
    print('Part 1: %i' % calculated_answer)

    # PART 2
    # sample data
    sample_data = np.array([
        'abc', 'a b c', 'ab ac', 'a a a a', 'b'
    ])
    sample_answer = 6
    calculated_sample_answer = process_data_part_2(sample_data)
    assert sample_answer == calculated_sample_answer
    # test data
    test_data = []
    with open(r'data/day_6_input.txt', 'rb') as f:
        contents = f.readlines()
        current_line = ''
        for line in contents:
            line = line.decode('utf-8')
            line = line.strip('\r\n')
            if len(line) != 0:
                if len(current_line) != 0:
                    current_line = current_line + ' ' + line
                else:
                    current_line = line
            else:
                test_data.append(current_line)
                current_line = ''
    if len(current_line) != 0:
        test_data.append(current_line)
    test_data = np.array(test_data)
    calculated_answer = process_data_part_2(test_data)
    print('Part 2: %i' % calculated_answer)
