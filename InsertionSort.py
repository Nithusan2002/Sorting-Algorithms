def insertionSort(array):
    for i in range (1, len(array) - 1):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            # Swap arr[j] with the element before it
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1

def main():
   array = [64, 34, 25, 12, 22, 11, 90]
   print('Array:', array)
   insertionSort(array)
   print('Sorted array:', array)

if __name__ == '__main__':
   main()
