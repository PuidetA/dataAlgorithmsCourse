def isort(A):
    i=1
    for i in range(len(A)):
        j=i-1
        while(j>=0) and A[j]>A[j+1]:
            A[j], A[j+1]=A[j+1], A[j]
            j=j-1
    return

if __name__ == "__main__": 
    A = [4, 3, 6, 2, 9, 7, 1, 8, 5]
    isort(A)
    print(A)