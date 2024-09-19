def pairs(s):
    if len(s) < 2:
        return 0
    indexLocations = [] # To make this O(n) we need to store the index locations to then calculate each index locations' contribution to the sum of distances, instead of doing 2 for loops and checking each pair separately.

    
    for index in range(len(s)): # O(n), we check each element in the string, and pass the index of all the 1 elements to the indexLocations list.
        if s[index] == "1":
            indexLocations.append(index)
    if len(indexLocations) < 2:
        return 0
    
    sumOfPairs = 0 # Initialize

    for index in range(len(indexLocations)): # O(n)
        # We calculate the sum of pairs in one pass by checking the contribution of each 1 element in the string to the sum, since each 1 element contributes to the sum of pairs by the amount of 1 elements that are to the right of it.
        # We do this by adding the distances of all the 1 elements to the right of the current 1 element, and subtract the distances of the 1 elements to the left.
        sumOfPairs = sumOfPairs + index*indexLocations[index] - indexLocations[index]*(len(indexLocations)-1-index)
    

    return sumOfPairs

if __name__ == "__main__":
    print(pairs("100101"))
    print(pairs("101"))
    print(pairs("100100111001"))