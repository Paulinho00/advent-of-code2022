def points_known_choices(line: str) -> int:
    opponent_choice = line[0]
    player_choice = line[2]
    points = 0

    if player_choice == 'X':
        points += 1
        if opponent_choice == 'A':
            points += 3
        elif opponent_choice == 'C':
            points += 6
    elif player_choice == 'Y':
        points += 2
        if opponent_choice == 'B':
            points += 3
        elif opponent_choice == 'A':
            points += 6
    elif player_choice == 'Z':
        points += 3
        if opponent_choice == 'C':
            points += 3
        elif opponent_choice == 'B':
            points += 6

    return points


def points_known_result(line: str) -> int:
    opponent_choice = line[0]
    round_result = line[2]
    points = 0

    if round_result == 'Z':
        points += 6
        if opponent_choice == 'A':
            points += 2
        elif opponent_choice == 'B':
            points += 3
        else:
            points += 1
    elif round_result == 'Y':
        points += 3
        if opponent_choice == 'A':
            points += 1
        elif opponent_choice == 'B':
            points += 2
        else:
            points += 3
    else:
        if opponent_choice == 'A':
            points += 3
        elif opponent_choice == 'B':
            points += 1
        else:
            points += 2

    return points


def main():
    file = open("input.txt")
    points_choices = 0
    points_results = 0
    for line in file:
        points_choices += points_known_choices(line)
        points_results += points_known_result(line)

    print(f"Part 1: {points_choices}")
    print(f"Part 2: {points_results}")


if __name__ == "__main__":
    main()
