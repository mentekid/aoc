import re
import sys

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def get_counts(string, color):
    matches = re.findall(f"(\d+) {color}", string)
    if matches:
        return [int(m) for m in matches]

def parse_line(line):
    game, results = line.split(":")

    reds = get_counts(results, "red")
    greens = get_counts(results, "green")
    blues = get_counts(results, "blue")

    game_no = re.findall("Game (\d+)", game)

    return reds, greens, blues, int(game_no[0])

def is_possible(reds, greens, blues):
    return max(reds) <= MAX_RED and max(greens) <= MAX_GREEN and max(blues) <= MAX_BLUE

def solve_part1(lines):
    answer = 0
    for line in lines:
        reds, greens, blues, game_idx = parse_line(line)

        answer += game_idx if is_possible(reds, greens, blues) else 0
    return answer

def solve_part2(lines):
    answer = 0
    for line in lines:
        reds, greens, blues, game_idx = parse_line(line)

        max_reds = max(reds)
        max_greens = max(greens)
        max_blues = max(blues)
        power = max_reds * max_greens * max_blues

        answer += power
    return answer

if __name__ == "__main__":
    print(solve_part2([line for line in sys.stdin]))