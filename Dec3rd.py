# overall a somewhat inefficient algorithm, but the first thing that came to mind was to check for the mul pattern by
# comparing each letter in the input. Will maybe come up with a better solution after my first one
def mul_finder():
    mulTotal = 0
    puzzleInput = open("input.txt", "r")
    numberVals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    do = True

    # parse the input (appears to be a single line)
    for line in puzzleInput:
        # loop through each letter in the line until a pattern of 'mul(' is found
        for i in range(len(line)):

            # check for the new do and don't instructions
            if line[i:i + 4] == 'do()':
                do = True
                i += 4
                continue
            if line[i:i + 7] == "don't()":
                do = False
                i += 7
                continue

            # check for the mul instruction

            if line[i:i + 4] == "mul(":
                i += 4
                # check if the next letter is a member of numberVals
                if numberVals.count(line[i]) > 0 and i < len(line):
                    # save the value for if it's a real mul instruction
                    x = line[i]
                    i += 1
                    # check if it's greater than 1 digit
                    while numberVals.count(line[i]) > 0 and i < len(line):
                        x += line[i]
                        i += 1
                    if line[i] == ',' and i < len(line):
                        i += 1
                        if numberVals.count(line[i]) > 0 and i < len(line):
                            # save the value for if it's a real mul instruction
                            y = line[i]
                            i += 1
                            # check if it's greater than 1 digit
                            while numberVals.count(line[i]) and i < len(line):
                                y += line[i]
                                i += 1
                            if line[i] == ')':
                                # it's likely a real mul instruction, check the 1-3 digit condition
                                # for the multiplicands and that 'do' is True
                                if (1 <= len(y) <= 3 and 1 <= len(x) <= 3) and do:
                                    mulTotal += int(x) * int(y)

    return mulTotal


print(mul_finder())
