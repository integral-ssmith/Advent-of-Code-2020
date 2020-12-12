import numpy as np


def process_data_part_1(a, preamble=25):
    # loop through value stream
    for i in range(preamble, len(a)):
        # get the preamble
        a_preamble = a[i-preamble:i]
        # get the value
        a_val = a[i]
        # get the valid values
        valid_vals = a_preamble[:, np.newaxis] + a_preamble[np.newaxis, :]
        valid_vals = valid_vals.astype(float)
        valid_vals[np.identity(len(a_preamble), dtype=bool)] = np.nan
        valid_vals = valid_vals.flatten()
        valid_vals = valid_vals[np.logical_not(np.isnan(valid_vals))].astype(np.uint64)
        # check for invalid value
        if a_val not in valid_vals:
            return a_val
    return


def process_data_part_2(a, preamble=25):
    # get the invalid number
    invalid_num = process_data_part_1(a, preamble=preamble)
    # loop by number of contiguous numbers and find set
    for num_contig in range(2, len(a)):
        # get the moving contiguous sum
        moving_sum = [np.sum(a[i:i+num_contig]) for i in range(0, len(a) - num_contig)]
        # verify it hasn't gone too high
        if np.all(moving_sum > invalid_num):
            return
        # check for a match location
        bool_loc = moving_sum == invalid_num
        if np.any(bool_loc):
            # get the location
            loc = np.where(bool_loc)[0][0]
            # return the result
            nums = a[loc:loc+num_contig]
            return np.amin(nums) + np.amax(nums)
    return


if __name__ == '__main__':
    # PART 1
    # sample data
    sample_data = np.array([
        35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576
    ])
    sample_answer = 127
    calculated_sample_answer = process_data_part_1(sample_data, preamble=5)
    assert sample_answer == calculated_sample_answer
    # test data
    test_data = np.loadtxt(r'data/day_9_input.txt', dtype=np.uint64)
    calculated_answer = process_data_part_1(test_data)
    print('Part 1: %i' % calculated_answer)

    # PART 2
    # sample data
    sample_answer = 62
    calculated_sample_answer = process_data_part_2(sample_data, preamble=5)
    assert sample_answer == calculated_sample_answer
    # test data
    calculated_answer = process_data_part_2(test_data)
    print('Part 2: %i' % calculated_answer)
