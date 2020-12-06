import numpy as np


def process_data_part_1(a, fields):
    return np.sum([np.all([f in i_a for f in fields]) for i_a in a])


def process_data_part_2(a):
    bool_valid = np.ones(len(a), dtype=bool)
    for i, l in enumerate(a):
        # extract fields:
        list_of_fields = l.split(' ')
        dict_of_fields = {f_l.split(':')[0]: f_l.split(':')[1] for f_l in list_of_fields}
        # check for key presence
        skip = False
        for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
            if key not in list(dict_of_fields.keys()):
                bool_valid[i] = False
                skip = True
        if skip:
            continue
        # byr validation
        try:
            val = int(dict_of_fields['byr'])
            if val < 1920 or val > 2002:
                bool_valid[i] = False
                continue
        except:
            bool_valid[i] = False
            continue
        # iyr validation
        try:
            val = int(dict_of_fields['iyr'])
            if val < 2010 or val > 2020:
                bool_valid[i] = False
                continue
        except:
            bool_valid[i] = False
            continue
        # eyr validation
        try:
            val = int(dict_of_fields['eyr'])
            if val < 2020 or val > 2030:
                bool_valid[i] = False
                continue
        except:
            bool_valid[i] = False
            continue
        # hgt validation
        if dict_of_fields['hgt'].endswith('cm'):
            try:
                val = int(dict_of_fields['hgt'][:-2])
                if val < 150 or val > 193:
                    bool_valid[i] = False
                    continue
            except:
                bool_valid[i] = False
                continue
        elif dict_of_fields['hgt'].endswith('in'):
            try:
                val = int(dict_of_fields['hgt'][:-2])
                if val < 59 or val > 76:
                    bool_valid[i] = False
                    continue
            except:
                bool_valid[i] = False
                continue
        else:
            bool_valid[i] = False
            continue
        # hcl validation
        if not dict_of_fields['hcl'].startswith('#'):
            bool_valid[i] = False
            continue
        valid_vals = [str(j) for j in range(10)] + ['a', 'b', 'c', 'd', 'e', 'f']
        if np.sum([dict_of_fields['hcl'].count(val) for val in valid_vals]) != 6:
            bool_valid[i] = False
            continue
        # ecl validation
        valid_vals = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if not np.any([dict_of_fields['ecl'] == val for val in valid_vals]):
            bool_valid[i] = False
            continue
        # pid validation
        if len(dict_of_fields['pid']) != 9:
            bool_valid[i] = False
            continue
        try:
            vals = [int(j) for j in dict_of_fields['pid']]
        except:
            bool_valid[i] = False
            continue
    return np.sum(bool_valid)


if __name__ == '__main__':
    # PART 1
    # sample data
    sample_data = np.array([
        'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm',
        'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929',
        'hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm',
        'hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in'
    ])
    sample_answer = 2
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    calculated_sample_answer = process_data_part_1(sample_data, required_fields)
    assert sample_answer == calculated_sample_answer
    # test data
    test_data = []
    with open(r'data/day_4_input.txt', 'rb') as f:
        contents = f.readlines()
        current_line = ''
        for line in contents:
            line = line.decode('utf-8')
            line = line.strip('\r\n')
            if len(line) != 0:
                if len(current_line) != 0:
                    current_line = current_line + ' ' + line
                else:
                    current_line = line
            else:
                test_data.append(current_line)
                current_line = ''
    if len(current_line) != 0:
        test_data.append(current_line)
    test_data = np.array(test_data)
    calculated_answer = process_data_part_1(test_data, required_fields)
    print('Part 1: %i of %i passports are valid' % (calculated_answer, len(test_data)))

    # PART 2
    # sample data
    sample_data = np.array([
        'eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926',
        'iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946',
        'hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277',
        'hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007',
        'pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f',
        'eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm',
        'hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022',
        'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'
    ])
    sample_answer = 4
    calculated_sample_answer = process_data_part_2(sample_data)
    assert sample_answer == calculated_sample_answer
    # test data
    calculated_answer = process_data_part_2(test_data)
    print('Part 2: %i of %i passports are valid' % (calculated_answer, len(test_data)))
