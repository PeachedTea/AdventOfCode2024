
def list_distance_solver():
    total = 0
    puzzleInput = open("input.txt", "r")
    # parse the input
    for line in puzzleInput:
        list1 = line.split('   ')
        total += abs(int(list1[0]) - int(list1[1]))
    puzzleInput.close()
    return total

print(list_distance_solver())