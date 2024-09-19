def changes(A):
    changesMade = 0 # The number of changes made.
    for i in range(1, len(A)):
        if A[i-1] == A[i]:
            changesMade += 1
            A[i] = -2 # Change it to -2 since it's out of range of the given limits.
    return changesMade

if __name__ == "__main__":
    print(changes([1, 1, 2, 2, 2]))
    print(changes([1, 2, 3, 4, 5]))
    print(changes([1, 1, 1, 1, 1]))