commands = [n.strip() for n in open('input.txt', 'r') if n]

def puzzle1() -> None:
    horizontal_pos = 0
    depth = 0

    for command in commands:
        direction, value = command.split(' ')
        value = int(value)

        if direction == 'up':
            depth -= value
        elif direction == 'down':
            depth += value
        elif direction == 'forward':
            horizontal_pos += value

    print(f'[Puzzle 1] Final horizontal position * final depth: {horizontal_pos * depth}')


def puzzle2() -> None:
    horizontal_pos = 0
    aim = 0
    depth = 0

    for command in commands:
        direction, value = command.split(' ')
        value = int(value)

        if direction == 'up':
            aim -= value
        elif direction == 'down':
            aim += value
        elif direction == 'forward':
            horizontal_pos += value
            depth += aim * value

    print(f'[Puzzle 2] Final horizontal position * final depth: {horizontal_pos * depth}')


if __name__ == '__main__':
    puzzle1()
    puzzle2()
