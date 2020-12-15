import numpy as np


def process_data_part_1(a):
    # get first available time
    first_available = int(a[0])
    # filter to running busses
    bus_opts = a[1:]
    bus_opts = bus_opts[bus_opts != 'x']
    bus_opts = bus_opts.astype(int)
    # get closest interval after first available time for each bus
    int_multiplier = np.ceil(first_available / bus_opts)
    time_between = np.multiply(bus_opts, int_multiplier) - first_available
    id_bus = np.argmin(time_between)
    bus_t = time_between[id_bus]
    bus_id = bus_opts[id_bus]
    return bus_t * bus_id


def process_data_part_2(a):
    # get the bus ids and time interval addition
    bus_opts = a[1:]
    bus_time_adds = np.arange(len(bus_opts))
    # filter not running busses
    bus_time_adds = bus_time_adds[bus_opts != 'x'].astype(np.int64)
    bus_opts = bus_opts[bus_opts != 'x'].astype(np.int64)
    # get the first time that fulfils the criteria
    t = bus_opts[0] + bus_time_adds[0]
    step = t
    for bus_opt, bus_time_add in zip(bus_opts, bus_time_adds):
        while True:
            if np.mod(t + bus_time_add, bus_opt) == 0:
                break
            t += step
        step = np.lcm(step, bus_opt)
    return t


if __name__ == '__main__':
    # PART 1
    # sample data
    sample_data = np.array(['939', '7', '13', 'x', 'x', '59', 'x', '31', '19'])
    sample_answer = 295
    calculated_sample_answer = process_data_part_1(sample_data)
    assert sample_answer == calculated_sample_answer
    # test data
    test_data = np.loadtxt(r'data/day_13_input.txt', dtype=str, comments=None)
    test_data = np.array([test_data[0], *test_data[1].split(',')])
    calculated_answer = process_data_part_1(test_data)
    print('Part 1: %i' % calculated_answer)

    # PART 2
    # sample data
    sample_answer = 1068781
    calculated_sample_answer = process_data_part_2(sample_data)
    assert sample_answer == calculated_sample_answer
    # test data
    calculated_answer = process_data_part_2(test_data)
    print('Part 2: %i' % calculated_answer)
