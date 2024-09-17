# Sorting
Sorting is about arranging elements from a data structure so that a comes before b if a ⪯ b. 
There are three problems we can solve with sorting.
<ol>
  <li>Collect things that belong together</li>
  <ul>
    <li>If you have things that fall into different categories, we can arrange the categories</li>
    <li>If we sort by categories, we collect everything that falls into the same category</li>
  </ul>
  <li>Match</li>
  <ul>
    <li>Given two or more sequential structures, we can find matching elements by traversing over the array only once</li>
  </ul>
  <li>Search</li>
  <ul>
    <li>Searching in a sorted array is much faster than searching in an unsorted array</li>
  </ul>
</ol>

# Different Sorting Algorithms:
## Selection Sort
Selection sort is a straightforward sorting algorithm, specifically an in-place comparison sort. It has a time complexity of O(n<sup>2</sup>), which makes it inefficient for large lists. In general, it tends to perform worse than similar algorithms like insertion sort. Nevertheless, selection sort is known for its simplicity and can have performance advantages in certain situations, especially where memory is limited.

The algorithm divides the original list into two parts: a section of elements already sorted, constructed from left to right at the beginning of the list, and a section of remaining unsorted items that make up the rest of the list. Initially, the sorted section is empty, and the unsorted section is the entire original list. The algorithm operates by locating the smallest (or largest, depending on the sorting order) element in the unsorted section, swapping it with the leftmost unsorted element (placing it in sorted order), and then shifting the boundaries of the sorted section one element to the right.

In simpler terms, the algorithm gradually builds up a sorted section of the list from left to right by finding the smallest element in the remaining unsorted section and placing it in its correct position. This process is repeated until the entire list is sorted.

| Worst Case | Average Case |
|------------|--------------|
| O(n<sup>2</sup>) | O(n<sup>2</sup>) |

| In-place? | Stable? |
|-----------|---------|
| Yes       | No      |

## Insertion Sort
Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However, insertion sort has several advantages:

1. Simple implementation
2. Efficient for small data sets
3. Adaptive, i.e., efficient for data sets that are already substantially sorted
4. More efficient in practice than most other simple quadratic (i.e., O(n<sup>2</sup>)) algorithms such as selection sort or bubble sort
5. Stable; does not change the relative order of elements with equal keys

The algorithm divides the input list into two parts: a sorted sublist of items which is built up from left to right and an unsorted sublist. At each iteration, the algorithm removes one element from the unsorted sublist, finds the location it belongs within the sorted sublist, and inserts it there. It repeats until no input elements remain.

| Worst Case | Average Case |
|------------|--------------|
| O(n<sup>2</sup>) | O(n<sup>2</sup>) |

| In-place? | Stable? |
|-----------|---------|
| Yes       | Yes     |

## Bubble Sort
Bubble sort is a straightforward comparison-based sorting algorithm. It is based on repeatedly stepping through the list, comparing each pair of adjacent items, and swapping them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted. 

Although the algorithm is simple to understand and implement, it is inefficient for large datasets—more advanced algorithms like quicksort or merge sort are much faster on large datasets.

| Worst Case | Average Case |
|------------|--------------|
| O(n<sup>2</sup>) | O(n<sup>2</sup>) |

| In-place? | Stable? |
|-----------|---------|
| Yes       | Yes     |

## Merge Sort
Merge sort is an efficient, stable, comparison-based, divide-and-conquer sorting algorithm. Most implementations produce a stable sort, which means that the order of equal elements is the same in the input and output. Merge sort is a good choice for sorting linked lists as well as arrays and provides guaranteed O(n log n) performance.

The algorithm works by dividing the unsorted list into 'n' sublists, each containing one element (a list of one element is considered sorted), and then repeatedly merging sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

| Worst Case | Average Case |
|------------|--------------|
| O(n log n) | O(n log n)   |

| In-place? | Stable? |
|-----------|---------|
| No        | Yes     |
