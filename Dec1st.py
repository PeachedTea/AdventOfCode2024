
def list_distance_solver():
    total = 0
    i = 0
    masterlist = [[], []]
    puzzleInput = open("input.txt", "r")
    # parse the input
    for line in puzzleInput:
        list1 = line.split('   ')
        masterlist[0].append(list1[0])
        masterlist[1].append(list1[1])
        i += 1
    puzzleInput.close()
    # sort the lists then find the difference of each element
    masterlist[0].sort()
    masterlist[1].sort()
    for i in range(len(masterlist[0])):
        total += abs((int(masterlist[0][i]) - int(masterlist[1][i])))

    return total

print(list_distance_solver())