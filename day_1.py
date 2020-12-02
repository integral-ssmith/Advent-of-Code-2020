import os
import numpy as np


def get_pair_adding_to_2020(arr):
    arr_1 = 2020 - arr
    bool_pair = arr_1[:, np.newaxis] == arr[np.newaxis, :]
    index_pair = np.where(np.logical_and(bool_pair, np.logical_not(np.identity(len(arr)))))[0]
    assert len(index_pair) == 2
    return arr[[index_pair[0], index_pair[1]]]


def get_triplet_adding_to_2020(arr):
    arr_1 = 2020 - arr
    arr_sum = arr[:, np.newaxis] + arr[np.newaxis, :]
    bool_compare = arr_sum[:, :, np.newaxis] == arr_1[np.newaxis, np.newaxis, :]
    index_triplet = np.unique(np.where(
        np.logical_and(bool_compare,
                       np.repeat(np.logical_not(np.identity(len(arr)))[:, :, np.newaxis], len(arr), axis=2))
    )[0])
    assert len(index_triplet) == 3
    return arr[[index_triplet[0], index_triplet[1], index_triplet[2]]]


if __name__ == '__main__':
    # PART 1
    # sample data
    sample_data = np.array([1721, 979, 366, 299, 675, 1456])
    sample_pair = np.array([1721, 299])
    sample_answer = 514579
    # test sample data
    calculated_sample_pair = get_pair_adding_to_2020(sample_data)
    calculated_sample_answer = calculated_sample_pair[0] * calculated_sample_pair[1]
    assert np.all([i in calculated_sample_pair for i in sample_pair])
    assert calculated_sample_answer == sample_answer
    # load in test data
    test_data = np.loadtxt(r'data/day_1_input.txt').astype(int)
    # calculate test result
    calculated_test_pair = get_pair_adding_to_2020(test_data)
    calculated_test_answer = calculated_test_pair[0] * calculated_test_pair[1]
    # output test result
    print('The pair of points that sum to 2020 are: %i, %i' % tuple(calculated_test_pair))
    print('Their product is: %i' % calculated_test_answer)

    # PART 2
    # sample data
    sample_triplet = np.array([979, 366, 675])
    sample_answer = 241861950
    # test sample data
    calculated_sample_triplet = get_triplet_adding_to_2020(sample_data)
    calculated_sample_answer = calculated_sample_triplet[0] * calculated_sample_triplet[1] * \
                               calculated_sample_triplet[2]
    assert np.all([i in calculated_sample_triplet for i in sample_triplet])
    assert calculated_sample_answer == sample_answer
    # calculate test result
    calculated_test_triplet = get_triplet_adding_to_2020(test_data)
    calculated_test_answer = calculated_test_triplet[0] * calculated_test_triplet[1] * \
                             calculated_test_triplet[2]
    # output test result
    print('The triplet of points that sum to 2020 are: %i, %i, %i' % tuple(calculated_test_triplet))
    print('Their product is: %i' % calculated_test_answer)
