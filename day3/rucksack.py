def priority_of_letter(letter: str) -> int:
    ascii_value = ord(letter)

    if letter.isupper():
        ascii_value -= 38
    else:
        ascii_value -= 96

    return ascii_value


def find_common_letter(line: str) -> str:
    first_half = line[:len(line)//2]
    second_half = line[len(line)//2:]

    common_letter = set(first_half).intersection(second_half).pop()
    return common_letter


def find_group_badge(group_rucksacks: list[str]) -> str:
    common_in_two_rucksacks = set(group_rucksacks[0]).intersection(group_rucksacks[1])
    group_badge = common_in_two_rucksacks.intersection(group_rucksacks[2])
    return group_badge.pop()


def part1() -> None:
    file = open('input.txt')
    priorities_sum = 0
    for line in file:
        common_letter = find_common_letter(line)
        priority = priority_of_letter(common_letter)
        priorities_sum += priority
    print(f"Part 1: {priorities_sum}")


def part2() -> None:
    file = open('input.txt')
    priorities_sum = 0
    group = []
    for index, line in enumerate(file):
        group.append(line.strip())
        if len(group) == 3:
            badge = find_group_badge(group)
            priorities_sum += priority_of_letter(badge)
            group.clear()

    print(f"Part 2: {priorities_sum}")


def main():
    part1()
    part2()

if __name__ == "__main__":
    main()