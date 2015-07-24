def SelectionSort(A):
    for i in range(len(A)):
        imin = i
        for j in range(i+1, len(A)):
            if A[j] < A[imin]:
                imin = j
        if A[i] != imin:
            hold = A[i]
            A[i] = A[imin]
            A[imin] = hold
    return A
