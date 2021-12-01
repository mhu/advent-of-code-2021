from typing import List

report = [int(l.strip()) for l in open('input.txt', 'r')]


def puzzle1() -> None:
    counter = 0

    for index, current in enumerate(report):
        if index == 0:
            continue

        if current > report[index - 1]:
            counter += 1

    print(f'Number of measurement increments: {counter}')


def get_group_sum(start_index) -> int:
    return sum(
        (
            report[start_index],
            report[start_index + 1],
            report[start_index + 2]
        )
    )


def puzzle2() -> None:
    counter = 0
    previous_group = get_group_sum(0)

    for index in range(1, len(report) - 2):
        current_group = get_group_sum(index)
        if current_group > previous_group:
            counter += 1

        previous_group = current_group

    print(f'Number of group increments: {counter}')


if __name__ == '__main__':
    puzzle1()
    puzzle2()
