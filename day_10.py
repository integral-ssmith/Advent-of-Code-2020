import numpy as np
import networkx as nx


def process_data_part_1(a):
    diffs, counts = np.unique(np.ediff1d(np.sort(np.append(a, [0, np.amax(a) + 3]))), return_counts=True)
    return counts[diffs == 1][0] * counts[diffs == 3][0]


def process_subdata_part_2(a_sorted):
    # generate the network
    charger_network = nx.DiGraph()
    for val in a_sorted:
        # add node
        if val not in list(charger_network.nodes):
            charger_network.add_node(val)
        # get forward connections
        other_vals = a_sorted[np.logical_and(a_sorted > val, a_sorted <= val + 3)]
        if len(other_vals) != 0:
            for other_val in other_vals:
                if other_val not in list(charger_network.nodes):
                    charger_network.add_node(other_val)
                charger_network.add_edge(val, other_val)
    # get the number of paths between the start and end
    paths = nx.all_simple_paths(charger_network, a_sorted[0], a_sorted[-1])
    return len(list(paths))


def process_data_part_2(a):
    # get the sorted vals
    sorted_vals = np.sort(np.append(a, [0, np.amax(a) + 3]))
    # find the locations of the 3 jolt jumps (only one path between)
    min_jumps = np.ediff1d(sorted_vals)
    loc_max_jump = np.where(min_jumps == 3)[0]
    # break into segments and multiply the result
    count = 1
    for i in range(len(loc_max_jump)):
        if i == 0:
            val_subset = sorted_vals[:loc_max_jump[i] + 1]
            count = count * process_subdata_part_2(val_subset)
        if i == len(loc_max_jump) - 1:
            val_subset = sorted_vals[loc_max_jump[i] + 1:]
        else:
            val_subset = sorted_vals[loc_max_jump[i] + 1:loc_max_jump[i + 1] + 1]
        if len(val_subset) > 2:
            count = count * process_subdata_part_2(val_subset)
    return count


if __name__ == '__main__':
    # PART 1
    # sample data
    sample_data = np.array([
        28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34,
        10, 3
    ])
    sample_answer = 220
    calculated_sample_answer = process_data_part_1(sample_data)
    assert sample_answer == calculated_sample_answer
    # test data
    test_data = np.loadtxt(r'data/day_10_input.txt', dtype=np.uint64)
    calculated_answer = process_data_part_1(test_data)
    print('Part 1: %i' % calculated_answer)

    # PART 2
    # sample data
    sample_answer = 19208
    calculated_sample_answer = process_data_part_2(sample_data)
    assert sample_answer == calculated_sample_answer
    # test data
    calculated_answer = process_data_part_2(test_data)
    print('Part 2: %i' % calculated_answer)
