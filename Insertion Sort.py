def InsertionSort(data):

    for i in range(1, len(data)):
        j = i
        while j > 0 and data[j-1] > data[j]:
            hold = data[j-1]
            data[j-1] = data[j]
            data[j] = hold
            j -= 1
    return data
