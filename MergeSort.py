def merge(A1, A2, A):
    i = 0
    j = 0
    
    while i < len(A1) and j < len(A2):
        if A1[i] <= A2[j]:
            A[i + j] = A1[i]
            i += 1
        else:
            A[i + j] = A2[j]
            j += 1
    while i < len(A1):
        A[i + j] = A1[i]
        i += 1

    while j < len(A2):
        A[i + j] = A2[j]
        j += 1
    return A

def MergeSort(A):
    if len(A) <= 1:
        return A
    i = len(A) // 2
    A1 = MergeSort(A[:i])
    A2 = MergeSort(A[i:])
    return merge(A1, A2, A)

def main():
    a = [9, 8, 1, 3, 0, 7, 6, 4, 5, 2]
    MergeSort(a)
    print('Sorted array', a)


if __name__ == "__main__":
    main()
