from typing import List

report = [n.strip() for n in open('input.txt', 'r')]

def puzzle1() -> None:
    gamma_rate = ''
    epsilon_rate = ''

    for index in range(len(report[0])):
        zeroes = 0
        ones = 0

        for line in report:
            if line[index] == '0':
                zeroes += 1
            else:
                ones += 1

        gamma_rate += '1' if ones > zeroes else '0'
        epsilon_rate += '0' if ones > zeroes else '1'

    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    print(f'[Puzzle 1] Power consumption: {power_consumption}')


def most_common_digit(report: List[str], position: int) -> str:
    zeroes = 0
    ones = 0

    for line in report:
        if line[position] == '0':
            zeroes += 1
        else:
            ones += 1

    return '1' if ones >= zeroes else '0'


def least_common_digit(report: List[str], position: int) -> str:
    zeroes = 0
    ones = 0

    for line in report:
        if line[position] == '0':
            zeroes += 1
        else:
            ones += 1

    return '0' if zeroes <= ones else '1'


def get_oxygen_generator_rating() -> int:
    oxygen_generator_ratings = report.copy()

    for index in range(len(oxygen_generator_ratings)):
        if len(oxygen_generator_ratings) == 1:
            break
        digit = most_common_digit(oxygen_generator_ratings, index)
        oxygen_generator_ratings = [l for l in oxygen_generator_ratings if l[index] == digit]

    return int(oxygen_generator_ratings[0], 2)


def get_co2_scrubber_rating() -> int:
    co2_scrubber_ratings = report.copy()

    for index in range(len(co2_scrubber_ratings)):
        if len(co2_scrubber_ratings) == 1:
            break
        digit = least_common_digit(co2_scrubber_ratings, index)
        co2_scrubber_ratings = [l for l in co2_scrubber_ratings if l[index] == digit]

    return int(co2_scrubber_ratings[0], 2)


def puzzle2() -> None:
    oxygen_generator_rating = get_oxygen_generator_rating()
    co2_scrubber_rating = get_co2_scrubber_rating()
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating

    print(f'[Puzzle 2] Life support rating: {life_support_rating}')


if __name__ == '__main__':
    puzzle1()
    puzzle2()
