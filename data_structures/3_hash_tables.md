# Hash tables

A hash table maps keys to values. 

They can be implemented in different ways, but one common implementation uses an array of linked lists and a hash function. Here's how the major operations are done.

Insert: Pass the key into the hash function and get an int output. Then we map that output to an index of the array- maybe using mod. Store the key/value pair in the linked list at the index (if it isn't already there). The linked list provides room for collisions (two keys being mapped to the same index). 

Find key: Hash the key, map it to the index in the same way. Search through the linked list for it. Worst case runtime is O(n) - all keys were mapped to the same index. The average runtime for insertions, deletions, and lookups, if the hash function is decent, and the array is large enough, is O(1).

One optimization of this approach is to use a BST instead of a linked list at each array index. We could then have a smaller array with decent lookup - O(log n).

Coming soon: 
- Hash functions for strings, objects
- Resizing

Practice: 
- https://leetcode.com/problems/design-hashmap/description/

[View simple implementation](code/hash_table.py)






Next: [Stacks](4_stacks.md)