def cat_nums(l):
    try: return int(l[0] + l[-1])
    except IndexError: return 0

def part_one_mini():
    return sum([cat_nums([c for c in ln if c.isdigit()]) for ln in open('1.txt').readlines()])


def concat_list_end_digits_to_int(string_list):
    try:
        return int(string_list[0] + string_list[-1])
    except IndexError:
        return 0

def part_one():
    ints_to_sum = []
    for line in open('1.txt').readlines():
        digits_from_line = [c for c in line if c.isdigit()]
        ints_to_sum.append(concat_list_end_digits_to_int(digits_from_line))
    return sum(ints_to_sum)


def part_two():
    number_strings = {
        'one':   '1',
        'two':   '2',
        'three': '3',
        'four':  '4',
        'five':  '5',
        'six':   '6',
        'seven': '7',
        'eight': '8',
        'nine':  '9',
    }

    lines = []

    for line in open('1.txt').readlines():
        digit_positions = {i: c for i, c in enumerate(line) if c.isdigit()}

        for num in number_strings.keys():
            found_index = line.find(num)
            while found_index > -1:
                digit_positions[found_index] = number_strings[num]
                found_index = line.find(num, found_index + 1)

        sorted_digits = [digit_positions[p] for p in sorted(digit_positions)]
        lines.append(concat_list_end_digits_to_int(sorted_digits))

    return sum(lines)


print("Part one, v1:", part_one())
print("Part one, v2:", part_one_mini())
print("Part two:", part_two())