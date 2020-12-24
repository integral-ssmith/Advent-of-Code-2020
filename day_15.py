from copy import deepcopy
import numpy as np


def process_data_part_1(a):
    num_history = deepcopy(a)
    i = len(num_history)
    while i < 2020:
        last_num = num_history[-1]
        if not np.any(np.array(num_history[:-1]) == last_num):
            # first time spoken
            num_history = np.append(num_history, [0])
        else:
            # get number of turns since last spoken
            idx_last_spoken = np.where(np.array(num_history[:-1]) == last_num)[0][-1]
            num_history = np.append(num_history, [i - idx_last_spoken - 1])
        i += 1
    return num_history[-1]


def process_data_part_2(arr_in, max_index):
    # strorage for the current and last index of each number
    num_current = {}
    num_previous = {}
    # initialize with the starting numbers
    for i in range(len(arr_in)):
        num = arr_in[i]
        num_current[num] = i + 1
    # loop through the remainder up until the max index
    for i in range(len(arr_in), max_index):
        # get the new number
        if num in num_previous:
            # if the last number occurred before get the difference in index between the occurences
            num = num_current[num] - num_previous[num]
        else:
            # new number is 0 if no previous occurences of last number
            num = 0
        # assign the index for the new number
        if num in num_current:
            # assign to previously occurred as well
            num_previous[num] = num_current[num]
            num_current[num] = i + 1
        else:
            # first occurrence, just assign to current
            num_current[num] = i + 1
    # num_history = np.zeros(30000000, dtype=np.int64)
    # i_start = len(a)
    # num_history[:i_start] = a
    # prev_used = []
    # prev_used_idx = []
    # for i, val in enumerate(a):
    #     if val not in prev_used:
    #         prev_used.append(val)
    #         prev_used_idx.append(i)
    #     else:
    #         prev_used_idx[prev_used.index(val)] = i
    # for i in range(i_start, 30000000):
    #     last_val = num_history[i - 1]
    #     if last_val in prev_used:
    #         num_history[i] = i - prev_used_idx[prev_used.index(last_val)] - 1
    #         prev_used_idx[prev_used.index(last_val)] = i
    #     else:
    #         prev_used.append(last_val)
    #         prev_used_idx.append(i)
    #         # 0 already default for value
    # return num_history[-1]
    return num


if __name__ == '__main__':
    # PART 1
    # sample data
    for nums, sample_answer in zip([[0, 3, 6], [1, 3, 2], [2, 1, 3], [1, 2, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]],
                                   [436, 1, 10, 27, 78, 438, 1836]):
        sample_data = np.array(nums)
        calculated_sample_answer = process_data_part_1(sample_data)
        assert sample_answer == calculated_sample_answer
    # test data
    test_data = np.loadtxt(r'data/day_15_input.txt', dtype=int, delimiter=',')
    calculated_answer = process_data_part_1(test_data)
    print('Part 1: %i' % calculated_answer)

    # PART 2
    # sample data
    for nums, sample_answer in zip([[0, 3, 6], [1, 3, 2], [2, 1, 3], [1, 2, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]],
                                   [175594, 2578, 3544142, 261214, 6895259, 18, 362]):
        sample_data = np.array(nums)
        calculated_sample_answer = process_data_part_2(sample_data, 30000000)
        assert sample_answer == calculated_sample_answer
    # test data
    calculated_answer = process_data_part_2(test_data.astype(np.int64), 30000000)
    print('Part 2: %i' % calculated_answer)
