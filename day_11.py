import copy
import numpy as np


def apply_rules_part_1(a_start):
    a_end = copy.deepcopy(a_start)
    len_i, len_j = a_end.shape
    for i in range(len_i):
        for j in range(len_j):
            if not np.isnan(a_start[i, j]):
                count_adj_occupied = 0
                for i_adj in [i - 1, i, i + 1]:
                    for j_adj in [j - 1, j, j + 1]:
                        if i_adj != -1 and i_adj != len_i and j_adj != -1 and j_adj != len_j and \
                                not (i_adj == i and j_adj == j):
                            if a_start[i_adj, j_adj] == 1:
                                count_adj_occupied += 1
                if count_adj_occupied == 0:
                    a_end[i, j] = 1
                elif count_adj_occupied >= 4:
                    a_end[i, j] = 0
    return a_end


def process_data_part_1(a):
    # format array
    val_map = {'L': 0, '#': 1, '.': np.nan}
    a = np.array([[val_map[j] for j in i] for i in a], dtype=float)
    # apply the rules until no changes occur
    bool_changed = True
    a_new = copy.deepcopy(a)
    while bool_changed:
        a_old = copy.deepcopy(a_new)
        a_new = apply_rules_part_1(a_old)
        if np.all(np.logical_or.reduce((a_old == a_new, np.isnan(a_old), np.isnan(a_new))), axis=None):
            bool_changed = False
    return np.nansum(a_new)


def apply_rules_part_2(a_start):
    a_end = copy.deepcopy(a_start)
    len_i, len_j = a_end.shape
    for i in range(len_i):
        for j in range(len_j):
            # if i == 1 and j == 9:
            #     t = 1
            if not np.isnan(a_start[i, j]):
                count_adj_occupied = 0
                # up
                if i != 0:
                    for i_adj in range(i - 1, -1, -1):
                        if not np.isnan(a_start[i_adj, j]):
                            if a_start[i_adj, j] == 1:
                                count_adj_occupied += 1
                            break
                # down
                if i != len_i - 1:
                    for i_adj in range(i + 1, len_i, 1):
                        if not np.isnan(a_start[i_adj, j]):
                            if a_start[i_adj, j] == 1:
                                count_adj_occupied += 1
                            break
                # left
                if j != 0:
                    for j_adj in range(j - 1, -1, -1):
                        if not np.isnan(a_start[i, j_adj]):
                            if a_start[i, j_adj] == 1:
                                count_adj_occupied += 1
                            break
                # right
                if j != len_j - 1:
                    for j_adj in range(j + 1, len_j, 1):
                        if not np.isnan(a_start[i, j_adj]):
                            if a_start[i, j_adj] == 1:
                                count_adj_occupied += 1
                            break
                # up-left
                if i != 0 and j != 0:
                    for i_adj, j_adj in zip(np.arange(i - 1, -1, -1), np.arange(j - 1, -1, -1)):
                        if not np.isnan(a_start[i_adj, j_adj]):
                            if a_start[i_adj, j_adj] == 1:
                                count_adj_occupied += 1
                            break
                # down-left
                if i != len_i - 1 and j != 0:
                    for i_adj, j_adj in zip(np.arange(i + 1, len_i, 1), np.arange(j - 1, -1, -1)):
                        if not np.isnan(a_start[i_adj, j_adj]):
                            if a_start[i_adj, j_adj] == 1:
                                count_adj_occupied += 1
                            break
                # up-right
                if i != 0 and j != len_j - 1:
                    for i_adj, j_adj in zip(np.arange(i - 1, -1, -1), np.arange(j + 1, len_j, 1)):
                        if not np.isnan(a_start[i_adj, j_adj]):
                            if a_start[i_adj, j_adj] == 1:
                                count_adj_occupied += 1
                            break
                # down-right
                if i != len_i - 1 and j != len_j - 1:
                    for i_adj, j_adj in zip(np.arange(i + 1, len_i, 1), np.arange(j + 1, len_j, 1)):
                        if not np.isnan(a_start[i_adj, j_adj]):
                            if a_start[i_adj, j_adj] == 1:
                                count_adj_occupied += 1
                            break
                # count check
                if count_adj_occupied == 0:
                    a_end[i, j] = 1
                elif count_adj_occupied >= 5:
                    a_end[i, j] = 0
    return a_end


def process_data_part_2(a):
    # format array
    val_map = {'L': 0, '#': 1, '.': np.nan}
    a = np.array([[val_map[j] for j in i] for i in a], dtype=float)
    # apply the rules until no changes occur
    bool_changed = True
    a_new = copy.deepcopy(a)
    while bool_changed:
        a_old = copy.deepcopy(a_new)
        a_new = apply_rules_part_2(a_old)
        if np.all(np.logical_or.reduce((a_old == a_new, np.isnan(a_old), np.isnan(a_new))), axis=None):
            bool_changed = False
    return np.nansum(a_new)


if __name__ == '__main__':
    # PART 1
    # sample data
    sample_data = np.loadtxt(r'data/day_11_sample_input.txt', dtype=str, comments=None)
    sample_answer = 37
    calculated_sample_answer = process_data_part_1(sample_data)
    assert sample_answer == calculated_sample_answer
    # test data
    test_data = np.loadtxt(r'data/day_11_input.txt', dtype=str, comments=None)
    calculated_answer = process_data_part_1(test_data)
    print('Part 1: %i' % calculated_answer)

    # PART 2
    # sample data
    sample_answer = 26
    calculated_sample_answer = process_data_part_2(sample_data)
    assert sample_answer == calculated_sample_answer
    # test data
    calculated_answer = process_data_part_2(test_data)
    print('Part 2: %i' % calculated_answer)
