def main():
    file = open("input.txt", "r")
    elves = []
    elfs_calories = 0
    for line in file:
        if line == "\n":
            elves.append(elfs_calories)
            elfs_calories = 0
            continue
        elfs_calories += int(line[:-1])

    elves.append(elfs_calories)
    elves.sort(reverse=True)
    sum_top3 = sum(elves[0:3])
    print(elves[0], sum_top3)


if __name__ == '__main__':
    main()
