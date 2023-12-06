from src.aoc2023.cube_conundrum import solve_part1, solve_part2

def test_solve():
    assert(solve_part1(["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"]) == 1)


def test_solve_part2():
    assert(solve_part2(["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"]) == 48)