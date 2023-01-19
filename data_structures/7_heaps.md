# Heaps

Coming soon

A heap is a tree-based data structure that satisfies the heap property: a parent node is either greater than or equal to (in a max heap) or less than or equal to (in a min heap) any of its children. This means that the max or min element is always at the root. 

## Operations 

Common heap operations are:
1. Insert: Add a new element.
2. Extract-min/max: Remove and return the element with the min or max value.
3. Peek-min/max: Return the element with the minimum or maximum value without removing it.
4. Delete: This operation removes an element while maintaining the heap property.
5. Increase/decrease key: Modify the value of an element and re-arrange the elements to maintain the heap property.
6. Build heap: Construct a heap from an array of elements.
7. Merge: Merge two heaps into one.
8. Heapify: Restore the heap property when an element is removed or modified.

Most of these operations are usually implemented in O(log n) time.

## Implementation 

Heaps are generally implemented as binary trees. A binary heap is a complete binary tree, which means that all levels of the tree are fully filled except possibly the last level, and all nodes in the last level are as far left as possible. 

A heap can also be implemented as an array. The element at index i’s left child is at 2i+1, and the right child is at 2i+2. 

Heaps are commonly used to implement priority queues, and sorting algorithms such as heapsort. They are also useful in graph algorithms, for finding the next vertex to visit. Finally, they can be used to efficiently find the median of a sequence. 


Coming soon:
- Heap & heapsort Python implementation 
- Median implementation using max and min heap  





Next: [Binary search tree](8_binary_search_trees.md)