import numpy as np
import networkx as nx


def process_data_part_1(a, bag_type):
    # get the rule definition
    dict_bag_sets = {}
    for rule in a:
        # get rid of period at the end
        rule = rule[:-1]
        # get the split on what contains what
        rule_split = rule.split(' contain ')
        assert len(rule_split) == 2
        outer = ' '.join(rule_split[0].split(' ')[:-1])
        inner = rule_split[1]
        # get the inner bag list, ignoring the numbers, no need to incorporate bags that can't contain others
        if inner != 'no other bag':
            inner_split = inner.split(', ')
            inner_list = []
            for sub_inner in inner_split:
                # get the bag color
                bag_color = ' '.join(sub_inner.split(' ')[1:-1])
                inner_list.append(bag_color)
            dict_bag_sets[outer] = inner_list
    # get the count of outer bags that can contain a bag of color bag_type in one of the layers
    dict_bool = {key: False for key in dict_bag_sets.keys()}
    for key, vals in dict_bag_sets.items():
        if bag_type in vals:
            dict_bool[key] = True
    sum_start = 0
    sum_new = np.sum(list(dict_bool.values()))
    while sum_new != sum_start:
        for key, check in dict_bool.items():
            if check:
                for sub_key, vals in dict_bag_sets.items():
                    if key in vals:
                        dict_bool[sub_key] = True
        sum_start = sum_new
        sum_new = np.sum(list(dict_bool.values()))
    return np.sum(list(dict_bool.values()))


def process_data_part_2(a, bag_type):
    # generate the directed network
    bag_network = nx.DiGraph()
    for rule in a:
        # get rid of period at the end
        rule = rule[:-1]
        # get the split on what contains what
        rule_split = rule.split(' contain ')
        assert len(rule_split) == 2
        outer = ' '.join(rule_split[0].split(' ')[:-1])
        if outer not in list(bag_network.nodes):
            bag_network.add_node(outer)
        inner = rule_split[1]
        # get the inner bags
        if inner != 'no other bag' and inner != 'no other bags':
            inner_split = inner.split(', ')
            for sub_inner in inner_split:
                # get the number and the bag color
                num = int(sub_inner.split(' ')[0])
                bag_color = ' '.join(sub_inner.split(' ')[1:-1])
                # add the node and edge
                if bag_color not in list(bag_network.nodes):
                    bag_network.add_node(bag_color)
                bag_network.add_edge(outer, bag_color, count=num)
    # get the count of bags that can fit in a bag of bag_type
    count = get_counts(bag_network, bag_type) - 1
    return count


def get_counts(graph, color):
    if len(list(graph.successors(color))) == 0:
        count = 1
    else:
        count = 1
        for sub_color in graph.successors(color):
            edge_count = graph.get_edge_data(color, sub_color)['count']
            count += edge_count * get_counts(graph, sub_color)
    return count


if __name__ == '__main__':
    # PART 1
    # sample data
    sample_data = np.array([
        'light red bags contain 1 bright white bag, 2 muted yellow bags.',
        'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
        'bright white bags contain 1 shiny gold bag.',
        'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
        'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
        'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
        'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
        'faded blue bags contain no other bags.',
        'dotted black bags contain no other bags.'
    ])
    sample_answer = 4
    calculated_sample_answer = process_data_part_1(sample_data, 'shiny gold')
    assert sample_answer == calculated_sample_answer
    # test data
    test_data = np.loadtxt(r'data/day_7_input.txt', dtype=str, delimiter='\n')
    calculated_answer = process_data_part_1(test_data, 'shiny gold')
    print('Part 1: %i' % calculated_answer)
    # note: could solve this with a directed graphical network

    # PART 2
    # sample data
    sample_data = np.array([
        'shiny gold bags contain 2 dark red bags.',
        'dark red bags contain 2 dark orange bags.',
        'dark orange bags contain 2 dark yellow bags.',
        'dark yellow bags contain 2 dark green bags.',
        'dark green bags contain 2 dark blue bags.',
        'dark blue bags contain 2 dark violet bags.',
        'dark violet bags contain no other bags'
    ])
    sample_answer = 126
    calculated_sample_answer = process_data_part_2(sample_data, 'shiny gold')
    assert sample_answer == calculated_sample_answer
    # test data
    calculated_answer = process_data_part_2(test_data, 'shiny gold')
    print('Part 2: %i' % calculated_answer)
