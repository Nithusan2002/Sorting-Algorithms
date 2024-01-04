# Python program for implementation of Selection Sort
def SelectionSort(array):
    # Traversing the whole array
    for i in range (0, len(array)-1):
        # Finding the minimum element in the unsorted list
        k = i
        j = i + 1
        for j in range (i + 1, len(array)):
            if array[j] < array[k]:
                k = j
        if i != k:    
            # Swap the found minium element with the first element
            array[i], array[k] = array[k], array[i]

def main():
    unsortedList = [12, 11, 13, 5, 6, 9, 8, 15, 17, 3, 20, 2, 14, 7, 19, 1, 10, 4, 16, 18]
    SelectionSort(unsortedList)
    print('Sorted list:', unsortedList)


if __name__ == '__main__':
    main()
