def report_analyzer():
    nSafeReports = 0
    puzzleInput = open("input.txt", "r")
    # parse the input
    for line in puzzleInput:
        # parse each line (report) into a list of ints
        report = [int(item) for item in line.split()]
        isDecrease = False
        isIncrease = False
        isSafe = True

        for i in range(len(report) - 1):
            # check the 2nd condition (two adjacent items must only differ by at least 1 or at most 3)
            if not (abs(report[i] - report[i + 1]) == 1 or abs(report[i] - report[i + 1]) == 2 or abs(
                    report[i] - report[i + 1]) == 3) and isSafe:
                # condition was not true somewhere, set isSafe to False
                isSafe = False
            else:
                if (report[i] > report[i + 1]):
                    isDecrease = True
                else:
                    isIncrease = True
        # check if only isIncrease or isDecrease are True (didn't violate 1st condition)
        if isIncrease != isDecrease and isSafe:
            nSafeReports += 1

    puzzleInput.close()
    return nSafeReports

# Put this logic in its own function to allow reuse
def is_safe(report):
    isDecrease = False
    isIncrease = False
    isSafe = True

    # find # of normal reports
    for i in range(len(report) - 1):
        # check the 2nd condition (two adjacent items must only differ by at least 1 or at most 3)
        if not (abs(report[i] - report[i + 1]) == 1 or abs(report[i] - report[i + 1]) == 2 or abs(
                report[i] - report[i + 1]) == 3) and isSafe:
            # condition was not true somewhere, set isSafe to False
            isSafe = False
        else:
            if (report[i] > report[i + 1]):
                isDecrease = True
            else:
                isIncrease = True
    # check if only isIncrease or isDecrease are True (didn't violate 1st condition)
    if isIncrease != isDecrease and isSafe:
        return True


def report_analyzer_one_unsafe():
    nSafeReports = 0
    puzzleInput = open("input.txt", "r")
    # parse the input
    for line in puzzleInput:
        # parse each line (report) into a list of ints
        report = [int(item) for item in line.split()]

        # check if it's a normal reports
        if (is_safe(report)):
            nSafeReports += 1
            continue

        # check if a single modification to a level will make it safe
        for i in range(len(report)):
            # Remove one level
            modified_report = report[:i] + report[i + 1:]
            if is_safe(modified_report):
                nSafeReports += 1
                break

    puzzleInput.close()
    return nSafeReports

print(report_analyzer())
print(report_analyzer_one_unsafe())
