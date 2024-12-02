
def report_analyzer():
    nSafeReports = 0
    isDecrease = False
    isIncrease = False

    puzzleInput = open("input.txt", "r")
    # parse the input
    for line in puzzleInput:
        # parse each line (report) into a list of ints
        report = [int(item) for item in line.split()]
        for i in range(len(report)-1):
            # check the 2nd condition (two adjacent items must only differ by at least 1 or at most 3)
            if abs(report[i] - report[i + 1]) == 1 or abs(report[i] - report[i + 1]) == 2 or abs(report[i] - report[i + 1]) == 3:
                # check the 1st condition (must always be increasing or decreasing)
                if (report[i] > report[i+1]):
                    isDecrease = True
                else:
                    isIncrease = True
        # check if only isIncrease or isDecrease are True (didn't violate 1st condition)
        if ((isDecrease and not isIncrease) or (not isDecrease and isIncrease)):
            nSafeReports += 1
        # reset the bool vars
        isDecrease = False
        isIncrease = False

    puzzleInput.close()
    return nSafeReports


print(report_analyzer())