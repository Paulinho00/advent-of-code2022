def convert_assignment_to_list(assignment: str) -> set[int]:
    bounds = assignment.split('-')
    low_bound = (int(bounds[0]))
    high_bound = (int(bounds[1]))
    assignment = {section for section in range(low_bound, high_bound+1)}
    return assignment


def check_pairs_for_contain(first_assignments: set[int], second_assignments: set[int]) -> bool:
    if first_assignments.issubset(second_assignments):
        return True
    elif second_assignments.issubset(first_assignments):
        return True
    else:
        return False


def check_pairs_for_overlap(first_assignments: set[int], second_assignments: set[int]) -> bool:
    if any(section in first_assignments for section in second_assignments):
        return True
    elif any(section in second_assignments for section in first_assignments):
        return True
    else:
        return False


def part1() -> int:
    file = open("input.txt")
    contain_counter = 0
    for line in file:
        pairs = (line.strip()).split(',')
        first_pair = convert_assignment_to_list(pairs[0])
        second_pair = convert_assignment_to_list(pairs[1])
        if check_pairs_for_contain(first_pair, second_pair):
            contain_counter += 1

    print(f"Part 1: {contain_counter}")


def part2() -> int:
    file = open("input.txt")
    overlapped_counter = 0
    for line in file:
        pairs = (line.strip()).split(',')
        first_pair = convert_assignment_to_list(pairs[0])
        second_pair = convert_assignment_to_list(pairs[1])
        if check_pairs_for_overlap(first_pair, second_pair):
            overlapped_counter += 1

    print(f"Part 2: {overlapped_counter}")


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()

