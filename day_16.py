import numpy as np


def read_input(file):
    # initialize containers for data
    field_rules = {}
    my_ticket = []
    other_tickets = []
    # initialize looping variables
    current_section = 0
    # read in the file
    with open(file, 'r') as f:
        # loop by line
        lines = f.readlines()
        for line in lines:
            # ensure not blank line
            if line.strip() != '':
                # check for section changes
                if line.strip() == 'your ticket:':
                    current_section = 1
                elif line.strip() == 'nearby tickets:':
                    current_section = 2
                else:
                    # add data based on section
                    if current_section == 0:
                        # field data
                        # split the sections
                        field_data_split = line.split(': ')
                        field = field_data_split[0]
                        valid_range_string = field_data_split[1]
                        # get the valid ranges
                        valid_ranges = []
                        for range_string in valid_range_string.split(' or '):
                            range_string_split = range_string.split('-')
                            valid_ranges.append((int(range_string_split[0]), int(range_string_split[1])))
                        # assign the data
                        field_rules[field] = valid_ranges
                    elif current_section == 1:
                        # my ticket
                        # assign the data
                        my_ticket.append([int(val) for val in line.split(',')])
                    else:
                        # nearby tickets
                        # assign the data
                        other_tickets.append([int(val) for val in line.split(',')])
    # convert the lists to arrays
    return field_rules, np.array(my_ticket[0], dtype=np.int64), np.array(other_tickets, dtype=np.int64)


def process_data_part_1(field_rules, my_ticket, other_tickets):
    # get overall valid ranges for numbers
    valid_ranges = []
    for valid_ranges_set in field_rules.values():
        for vals_pair in valid_ranges_set:
            valid_ranges.append(list(vals_pair))
    valid_ranges = np.array(valid_ranges)
    # sort by the range start
    valid_ranges_sorted = valid_ranges[valid_ranges[:, 0].argsort()]
    # simplify the range set
    valid_ranges_simplified = [list(valid_ranges_sorted[0])]
    for valid_ranges_set in valid_ranges_sorted[1:]:
        # get previous and current range
        prev_min_val = valid_ranges_simplified[-1][0]
        prev_max_val = valid_ranges_simplified[-1][1]
        curr_min_val = valid_ranges_set[0]
        curr_max_val = valid_ranges_set[1]
        if curr_min_val <= prev_max_val + 1:
            # if there is overlap in the range
            if curr_max_val <= prev_max_val:
                # current range fully overlapped by previous range
                continue
            else:
                # extend the range
                valid_ranges_simplified[-1][1] = curr_max_val
        else:
            # no overlap
            valid_ranges_simplified.append(list(valid_ranges_set))
    # check each ticket number value against the possible ranges
    invalid_ticket_locations = np.array([
        np.logical_and.reduce([
            np.logical_not(
                np.logical_and(
                    other_tickets[:, i] >= val_pair[0],
                    other_tickets[:, i] <= val_pair[1]
                )
            ) for val_pair in valid_ranges_simplified
        ]) for i in range(other_tickets.shape[1])
    ]).T
    # get the sum of the invalid ticket numbers
    return np.sum(other_tickets[invalid_ticket_locations])


def discard_invalid_tickets(field_rules, other_tickets):
    # get overall valid ranges for numbers
    valid_ranges = []
    for valid_ranges_set in field_rules.values():
        for vals_pair in valid_ranges_set:
            valid_ranges.append(list(vals_pair))
    valid_ranges = np.array(valid_ranges)
    # sort by the range start
    valid_ranges_sorted = valid_ranges[valid_ranges[:, 0].argsort()]
    # simplify the range set
    valid_ranges_simplified = [list(valid_ranges_sorted[0])]
    for valid_ranges_set in valid_ranges_sorted[1:]:
        # get previous and current range
        prev_min_val = valid_ranges_simplified[-1][0]
        prev_max_val = valid_ranges_simplified[-1][1]
        curr_min_val = valid_ranges_set[0]
        curr_max_val = valid_ranges_set[1]
        if curr_min_val <= prev_max_val + 1:
            # if there is overlap in the range
            if curr_max_val <= prev_max_val:
                # current range fully overlapped by previous range
                continue
            else:
                # extend the range
                valid_ranges_simplified[-1][1] = curr_max_val
        else:
            # no overlap
            valid_ranges_simplified.append(list(valid_ranges_set))
    # check each ticket number value against the possible ranges
    invalid_ticket_locations = np.any(
        np.array([
            np.logical_and.reduce([
                np.logical_not(
                    np.logical_and(
                        other_tickets[:, i] >= val_pair[0],
                        other_tickets[:, i] <= val_pair[1]
                    )
                ) for val_pair in valid_ranges_simplified
            ]) for i in range(other_tickets.shape[1])
        ]).T, axis=1
    )
    return other_tickets[np.logical_not(invalid_ticket_locations)]


def process_data_part_2(field_rules, my_ticket, other_tickets):
    # get the valid tickets
    other_tickets = discard_invalid_tickets(field_rules, other_tickets)
    # initialize field assingment to allow any potential order
    field_idxs = list(range(other_tickets.shape[1]))
    field_assignment = {field: [] for field in field_rules.keys()}
    # check for validity in the fields
    for field in field_rules.keys():
        # get valid ranges
        valid_ranges = field_rules[field]
        # test each field index for validity
        for field_idx in field_idxs:
            invalid_field_bool = np.any(
                np.array([
                    np.logical_and.reduce([
                        np.logical_not(
                            np.logical_and(
                                other_tickets[:, field_idx] >= val_pair[0],
                                other_tickets[:, field_idx] <= val_pair[1]
                            )
                        ) for val_pair in valid_ranges
                    ])
                ])
            )
            if not invalid_field_bool:
                field_assignment[field].append(field_idx)
    # check for any with only one valid index, remove that index from the rest
    while not np.all([len(idxs) == 1 for idxs in field_assignment.values()]):
        for field, field_idxs in field_assignment.items():
            if len(field_idxs) == 1:
                field_idx = field_idxs[0]
                for field_other in field_assignment.keys():
                    if field != field_other and field_idx in field_assignment[field_other]:
                        field_assignment[field_other].remove(field_idx)
    departure_multiplied = 1
    for field, field_idx in field_assignment.items():
        if field.startswith('departure'):
            departure_multiplied = departure_multiplied * my_ticket[field_idx[0]]
    return departure_multiplied


if __name__ == '__main__':
    # PART 1
    # sample data
    field_rules, my_ticket, other_tickets = read_input(r'data/day_16_sample_input.txt')
    sample_answer = 71
    calculated_sample_answer = process_data_part_1(field_rules, my_ticket, other_tickets)
    assert sample_answer == calculated_sample_answer
    # test data
    field_rules, my_ticket, other_tickets = read_input(r'data/day_16_input.txt')
    calculated_answer = process_data_part_1(field_rules, my_ticket, other_tickets)
    print('Part 1: %i' % calculated_answer)

    # PART 2
    # sample data - N/A
    # test data
    calculated_answer = process_data_part_2(field_rules, my_ticket, other_tickets)
    print('Part 2: %i' % calculated_answer)
