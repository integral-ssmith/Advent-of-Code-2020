import numpy as np


def process_data_part_1(a):
    arr = np.array([[char for char in row] for row in a])
    encountered = ''
    i = 0
    j = 0
    i_max, j_max = arr.shape
    while i < i_max - 1:
        i += 1
        j += 3
        if j >= j_max:
            j -= j_max
        encountered += arr[i, j]
    num_trees = encountered.count('#')
    return num_trees


def process_data_part_2(a, num_right, num_down):
    arr = np.array([[char for char in row] for row in a])
    encountered = ''
    i = 0
    j = 0
    i_max, j_max = arr.shape
    while i < i_max - 1:
        i += num_down
        j += num_right
        if j >= j_max:
            j -= j_max
        encountered += arr[i, j]
    num_trees = encountered.count('#')
    return num_trees


if __name__ == '__main__':
    # PART 1
    # sample data
    sample_data = np.array([
        '..##.......',
        '#...#...#..',
        '.#....#..#.',
        '..#.#...#.#',
        '.#...##..#.',
        '..#.##.....',
        '.#.#.#....#',
        '.#........#',
        '#.##...#...',
        '#...##....#',
        '.#..#...#.#'])
    sample_answer = 7
    calculated_sample_answer = process_data_part_1(sample_data)
    assert sample_answer == calculated_sample_answer
    # test data
    test_data = np.loadtxt(r'data/day_3_input.txt', dtype=str, comments=None)
    calculated_answer = process_data_part_1(test_data)
    print('Part 1: %i trees encountered' % calculated_answer)

    # PART 2
    # sample data
    direction_pairs = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    sample_answer = 336
    calculated_sample_answer = np.prod(np.array([process_data_part_2(sample_data, *instructions)
                                                for instructions in direction_pairs], dtype='int64'))
    assert sample_answer == calculated_sample_answer
    # test data
    calculated_answer = np.prod(np.array([process_data_part_2(test_data, *instructions)
                                         for instructions in direction_pairs], dtype='int64'))
    print('Part 2: the product of the trees encountered is %i' % calculated_answer)
