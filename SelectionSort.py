def SelectionSort(array):
    for i in range (0, len(array)-1):
        k = i
        j = i + 1
        for j in range (i + 1, len(array)):
            if array[j] < array[k]:
                k = j
        if i != k:    
            array[i], array[k] = array[k], array[i]

def main():
    unsortedList = [12, 11, 13, 5, 6, 9, 8, 15, 17, 3, 20, 2, 14, 7, 19, 1, 10, 4, 16, 18]
    SelectionSort(unsortedList)
    print(unsortedList)


if __name__ == '__main__':
    main()
