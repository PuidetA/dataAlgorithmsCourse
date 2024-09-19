import math

def calculations(n):
    answer1 = (0.5*n)**2
    answer2 = 22*n
    answer3 = 10 * n * math.log(n, 2)
    answer4 = (1.3)**n
    print ("With n =", n, "\n", "T(n) = 0.5n^2: ", answer1, "\n", "T(n) = 22n: ", answer2, "\n", "T(n) = 10n log2(n): ", answer3, "\n", "T(n) = 1.3^n: ", answer4, "\n\n")

def nlog2n(n):
    #find closest number to n, given the amount of n (amount of instructions). This is to solve time complexity, result should be how many n's can one do within the amount of instructions given.
    amountOfInstructionsRequired = 0
    currentInstructionCount = 1
    while(True):
        amountOfInstructionsRequired = currentInstructionCount * math.log(currentInstructionCount, 2)   
        if amountOfInstructionsRequired >= n:
            currentInstructionCount -= 1
            return currentInstructionCount
        currentInstructionCount += 1


def algorithmInstructionCheckWithPowers(n, x):
    amountOfInstructionsRequired = 0
    currentInstructionCount = 1
    while(True):
        amountOfInstructionsRequired = currentInstructionCount**x
        if amountOfInstructionsRequired >= n:
            currentInstructionCount -= 1
            return currentInstructionCount
        currentInstructionCount += 1

def algorithmInstructionCheckWith2toN(n):
    amountOfInstructionsRequired = 0
    currentInstructionCount = 1
    while(True):
        amountOfInstructionsRequired = 2**currentInstructionCount
        if amountOfInstructionsRequired >= n:
            currentInstructionCount -= 1
            return currentInstructionCount
        currentInstructionCount += 1

if __name__ == "__main__":
    #calculations(15)
    #calculations(30)
    #calculations(45)
    #calculations(90)
    #print(nlog2n(10**9))
    #print(algorithmInstructionCheckWithPowers(10**9, 5))
    #print(algorithmInstructionCheckWith2toN(10**9))
    #print(algorithmInstructionCheckWithPowers((10**9)*24*60*60, 5))
    #print(algorithmInstructionCheckWith2toN((10**9)*24*60*60))
    print(algorithmInstructionCheckWith2toN((10**9)*365*24*60*60))