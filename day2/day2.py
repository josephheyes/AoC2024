from itertools import compress


def is_safe(report):
    diffs = [(b - a) for a, b in zip(report, report[1:])]

    if (all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs)) and all(
        1 <= abs(diff) <= 3 for diff in diffs
    ):
        return True
    else:
        return False


def main():
    safe = 0

    with open("day2/input.txt") as input:
        reports = input.readlines()
        reports = [[int(level) for level in report.split()] for report in reports]

    for report in reports:
        if is_safe(report):
            safe += 1
            continue

        for i in range(0, len(report)):
            removed_level_report = report.copy()
            removed_level_report.pop(i)
            if is_safe(removed_level_report):
                safe += 1
                break

    print(safe)


if __name__ == "__main__":
    main()
