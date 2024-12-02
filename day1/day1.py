def main():
    with open("example.txt") as input:
        lines = input.readlines()
        lines = [line.split() for line in lines]
        left = sorted([int(line[0]) for line in lines])
        right = sorted([int(line[1]) for line in lines])

    print(f"part 1: {sum([abs(l - r) for l, r in zip(left, right)])}")

    print(f"part 2: {sum([l * right.count(l) for l in left])}")


if __name__ == "__main__":
    main()
