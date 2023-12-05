def load_games():
    games = {}

    for line in open('2.txt'):
        game, values = line.split(':')

        game_num = int(''.join(c for c in game if c.isdigit()))
        games[game_num] = []

        rounds = values.split(';')
        for r in rounds:
            round = {}
            colors = r.strip().split(',')
            for c in colors:
                count, color = c.strip().split(' ')
                round[color[0]] = int(count)
            games[game_num].append(round)

    return games


def part_one():
    games = load_games()
    limits = {'r': 12, 'g': 13, 'b': 14}
    impossible_games = set()

    for num, rounds in games.items():
        for r in rounds:
            for k, v in r.items():
                if v > limits[k]:
                    impossible_games.add(num)

    return sum(set(games.keys()) - impossible_games)


def part_one_parse_time():
    limits = {'red': 12, 'green': 13, 'blue': 14}

    def check_line_validity(line):
        game, values = line.split(':')
        game_num = int(game.removeprefix('Game '))

        for r in values.split(';'):
            for c in r.strip().split(','):
                count, color = c.strip().split(' ')
                if int(count) > limits[color]:
                    return 0
        return game_num

    return sum([check_line_validity(l) for l in open('2.txt').readlines()])


def part_two():
    games = load_games()
    cube_power = 0

    for rounds in games.values():
        red_max = max((r.get('r', 0) for r in rounds))
        green_max = max((r.get('g', 0) for r in rounds))
        blue_max = max((r.get('b', 0) for r in rounds))

        cube_power += red_max * green_max * blue_max

    return cube_power


def part_two_mini():
    gms = load_games().values()
    mx = lambda k, l: max((i.get(k, 0) for i in l))
    return sum(mx('r', r) * mx('g', r) * mx('b', r) for r in gms)


print('Part one, v1:', part_one())
print('Part one, v2:', part_one_parse_time())
print('Part two, v1:', part_two())
print('Part two, v2:', part_two_mini())