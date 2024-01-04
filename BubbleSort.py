def BubbleSort(array):
    for i in range (0, len(array) - 2):
       for j in range (0, len(array) - i - 2):
        if array[j] > array[j + 1]:
           array[j], array[j + 1] = array[j + 1], array[j]

def main():
   array = [64, 34, 25, 12, 22, 11, 90]
   print('Array:', array)
   BubbleSort(array)
   print('Sorted array:', array)

if __name__ == '__main__':
   main()
