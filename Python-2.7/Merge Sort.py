def TopDownMergeSort(A):
    if len(A) >1 :
        midPoint = len(A) // 2
        leftHalf = A[:midPoint]
        rightHalf = A[midPoint:]

        TopDownMergeSort(leftHalf)
        TopDownMergeSort(rightHalf)

        i = j = k = 0
        
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                A[k] = leftHalf[i]
                i += 1
            else:
                A[k] = rightHalf[j]
                j += 1
            k += 1

        while i < len(leftHalf):
            A[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            A[k] = rightHalf[j]
            j += 1
            k += 1

"""
Note this is a recursive function so A should be global. e.g.
>>> A = [6,2,8,0,2,1,5]
>>> TopDownMergeSort(A)
>>> print A
[0, 1, 2, 2, 5, 6, 8]
"""
