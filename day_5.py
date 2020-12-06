import math
import numpy as np


def process_data_part_1(a):
    seat_ids = np.zeros(len(a), dtype=int)
    for i, i_a in enumerate(a):
        # pull the string values
        row_characters = i_a[0:7]
        col_characters = i_a[7:]
        # get the row
        row_min = 0
        row_max = 127
        for j_r in row_characters[:-1]:
            mid_point = (row_min + row_max) / 2
            if j_r == 'F':
                row_max = math.floor(mid_point)
            else:
                row_min = math.ceil(mid_point)
        if row_characters[-1] == 'F':
            row = row_min
        else:
            row = row_max
        # get the column
        col_min = 0
        col_max = 7
        for j_c in col_characters[:-1]:
            mid_point = (col_min + col_max) / 2
            if j_c == 'L':
                col_max = math.floor(mid_point)
            else:
                col_min = math.ceil(mid_point)
        if col_characters[-1] == 'L':
            col = col_min
        else:
            col = col_max
        seat_ids[i] = row * 8 + col
    return seat_ids


def process_data_part_2(a):
    seat_ids = process_data_part_1(a)
    all_ids = (np.arange(0, 128)[:, np.newaxis] * 8 + np.arange(0, 8)[np.newaxis, :]).flatten()
    return np.setdiff1d(all_ids, seat_ids)


if __name__ == '__main__':
    # PART 1
    # sample data
    sample_data = np.array(['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL'])
    sample_answer = np.array([567, 119, 820])
    calculated_sample_answer = process_data_part_1(sample_data)
    assert np.all(sample_answer == calculated_sample_answer)
    # test data
    test_data = np.loadtxt(r'data/day_5_input.txt', dtype=str)
    calculated_test_answer = process_data_part_1(test_data)
    print('Part 1: the highest passport ID is %i' % (np.amax(calculated_test_answer)))

    # PART 2
    unfilled_ids = process_data_part_2(test_data)
    unfilled_ids_not_at_f_or_b = unfilled_ids[np.where(np.ediff1d(unfilled_ids) != 1)[0][1:]]
    print('Part 2: the unfilled seat ids are %s' % (str(list(unfilled_ids_not_at_f_or_b))))
