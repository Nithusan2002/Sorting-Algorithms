# Sorting
Sorting is about arranging elements from a data structur so that a comes befor b if a ⪯ b. 
There are three problemes we can solve with sorting.
<ol>
  <li>Collect things that belong together</li>
  If you have things that fall into different categories, we can arrange the categories and if we sort by categories, we collect everything that falls into the same category
  <li>Match</li>
  Given two or more sequential structures, we can find matching elements by traversing over the array only once
  <li>Search</li>
  Searching in a sorted array is much faster than searching in an unsorted array
</ol>

# Different Sorting Algorithms:
## Selection sort
Selection sort is a straightforward sorting algorithm, specifically an in-place comparison sort. It has a time complexity of O(n<sup>2</sup>), which makes it inefficient for large lists. In general, it tends to perform worse than similar algorithms like insertion sort. Nevertheless, selection sort is known for its simplicity and can have performance advantages in certain situations, especially where memory is limited.

The algorithm divides the original list into two parts: a section of elements already sorted, constructed from left to right at the beginning of the list, and a section of remaining unsorted items that make up the rest of the list. Initially, the sorted section is empty, and the unsorted section is the entire original list. The algorithm operates by locating the smallest (or largest, depending on the sorting order) element in the unsorted section, swapping it with the leftmost unsorted element (placing it in sorted order), and then shifting the boundaries of the sorted section one element to the right.

In simpler terms, the algorithm gradually builds up a sorted section of the list from left to right by finding the smallest element in the remaining unsorted section and placing it in its correct position. This process is repeated until the entire list is sorted.

|Worst Case|Average Case|
|---|---|
|O(n<sup>2</sup>)|O(n<sup>2</sup>)

|In-place?|Stable?|
|---|---|
|Yes|No|

## Insertion Sort

## Bubble sort

## Merge sort
