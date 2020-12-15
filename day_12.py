import numpy as np


def compute_direction(d, a):
    d = d + a
    while d >= 360:
        d -= 360
    while d < 0:
        d += 360
    return d


def process_data_part_1(a):
    # east = 0, north = 90, etc..
    direction = 0
    position_x = 0
    position_y = 0
    # process the instructions
    for instr in a:
        if instr.startswith('N'):
            position_y += int(instr[1:])
        elif instr.startswith('S'):
            position_y -= int(instr[1:])
        elif instr.startswith('E'):
            position_x += int(instr[1:])
        elif instr.startswith('W'):
            position_x -= int(instr[1:])
        elif instr.startswith('L'):
            direction = compute_direction(direction, int(instr[1:]))
        elif instr.startswith('R'):
            direction = compute_direction(direction, -1 * int(instr[1:]))
        elif instr.startswith('F'):
            position_x += int(round(int(instr[1:]) * np.cos(np.deg2rad(direction)), 0))
            position_y += int(round(int(instr[1:]) * np.sin(np.deg2rad(direction)), 0))
        else:
            raise ValueError('Unknown direction')
    return abs(position_x) + abs(position_y)


def process_data_part_2(a):
    # east = 0, north = 90, etc..
    position_x_s = 0
    position_y_s = 0
    position_x_wp_r = 10
    position_y_wp_r = 1
    # process the instructions
    for instr in a:
        if instr.startswith('N'):
            position_y_wp_r += int(instr[1:])
        elif instr.startswith('S'):
            position_y_wp_r -= int(instr[1:])
        elif instr.startswith('E'):
            position_x_wp_r += int(instr[1:])
        elif instr.startswith('W'):
            position_x_wp_r -= int(instr[1:])
        elif instr.startswith('L'):
            position_x_wp_r_old = position_x_wp_r
            position_y_wp_r_old = position_y_wp_r
            deg_change = int(instr[1:])
            if deg_change == 90:
                position_x_wp_r = -1 * position_y_wp_r_old
                position_y_wp_r = position_x_wp_r_old
            elif deg_change == 180:
                position_x_wp_r = -1 * position_x_wp_r_old
                position_y_wp_r = -1 * position_y_wp_r_old
            elif deg_change == 270:
                position_x_wp_r = position_y_wp_r_old
                position_y_wp_r = -1 * position_x_wp_r_old
            else:
                raise ValueError('Not implemented')
        elif instr.startswith('R'):
            position_x_wp_r_old = position_x_wp_r
            position_y_wp_r_old = position_y_wp_r
            deg_change = int(instr[1:])
            if deg_change == 90:
                position_x_wp_r = position_y_wp_r_old
                position_y_wp_r = -1 * position_x_wp_r_old
            elif deg_change == 180:
                position_x_wp_r = -1 * position_x_wp_r_old
                position_y_wp_r = -1 * position_y_wp_r_old
            elif deg_change == 270:
                position_x_wp_r = -1 * position_y_wp_r_old
                position_y_wp_r = position_x_wp_r_old
            else:
                raise ValueError('Not implemented')
        elif instr.startswith('F'):
            num_times = int(instr[1:])
            position_x_s += num_times * position_x_wp_r
            position_y_s += num_times * position_y_wp_r
        else:
            raise ValueError('Unknown direction')
    return abs(position_x_s) + abs(position_y_s)


if __name__ == '__main__':
    # PART 1
    # sample data
    sample_data = np.array(['F10', 'N3', 'F7', 'R90', 'F11'])
    sample_answer = 25
    calculated_sample_answer = process_data_part_1(sample_data)
    assert sample_answer == calculated_sample_answer
    # test data
    test_data = np.loadtxt(r'data/day_12_input.txt', dtype=str, comments=None)
    calculated_answer = process_data_part_1(test_data)
    print('Part 1: %i' % calculated_answer)

    # PART 2
    # sample data
    sample_answer = 286
    calculated_sample_answer = process_data_part_2(sample_data)
    assert sample_answer == calculated_sample_answer
    # test data
    calculated_answer = process_data_part_2(test_data)
    print('Part 2: %i' % calculated_answer)
