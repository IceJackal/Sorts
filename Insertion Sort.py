def InsertionSort0(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j-1] > A[j]:
            hold = A[j-1]
            A[j-1] = A[j]
            A[j] = hold
            j -= 1
    return A

def InsertionSort1(A):
    for i in range(1, len(A)):
        x = A[i]
        j = i
        while j > 0 and A[j-1] > x:
            A[j] = A[j-1]
            j -= 1
        A[j] = x
    return A
