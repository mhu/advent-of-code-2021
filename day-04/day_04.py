from typing import List, Tuple


boards = []
drawn_numbers = []


with open('input.txt', 'r') as f:
    drawn_numbers = [n for n in f.readline().strip().split(',')]

    board = []
    for line in f.readlines()[1:]:
        line = line.strip()

        if len(line) > 0:
            line = line.replace('  ', ' ')
            board.append(line.split(' '))
        else:
            boards.append(board)
            board = []


def numbers_in_rows(board: List[str], numbers: List[str]) -> bool:
    for row in board:
        for value in row:
            if value not in numbers:
                break
        else:
            return True
    return False


def numbers_in_columns(board: List[str], numbers: List[str]) -> bool:
    for index in range(5):
        for row in board:
            if row[index] not in numbers:
                break
        else:
            return True
    return False


def get_winning_board() -> Tuple[List[str], List[str]]:
    for index in range(5, len(drawn_numbers) + 1):
        for board in boards:
            if numbers_in_rows(board, drawn_numbers[:index]) or numbers_in_columns(board, drawn_numbers[:index]):
                return (board, drawn_numbers[:index])


def get_unmarked_numbers(board: List[str], marked_numbers: List[str]) -> List[str]:
    board_flat = []
    for row in board:
        board_flat += row
    return [int(n) for n in board_flat if n not in marked_numbers]


def calculate_board_score(board: List[str], marked_numbers: List[str]) -> int:
    unmarked_numbers = get_unmarked_numbers(board, marked_numbers)
    return sum(unmarked_numbers) * int(marked_numbers[-1])


def puzzle1() -> None:
    board, marked_numbers = get_winning_board()
    score = calculate_board_score(board, marked_numbers)

    print(f'[Puzzle 1] Final score: {score}')


def get_last_winning_board() -> Tuple[List[str], List[str]]:
    for index in range(5, len(drawn_numbers) + 1):
        for board in boards:
            if numbers_in_rows(board, drawn_numbers[:index]) or numbers_in_columns(board, drawn_numbers[:index]):
                if len(boards) > 1:
                    boards.remove(board)
                else:
                    return (board, drawn_numbers[:index])


def puzzle2() -> None:
    board, marked_numbers = get_last_winning_board()
    score = calculate_board_score(board, marked_numbers)

    print(f'[Puzzle 2] Final score: {score}')


if __name__ == '__main__':
    puzzle1()
    puzzle2()
