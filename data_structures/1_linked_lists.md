# Linked lists

Unlike arrays, linked lists are a series of "nodes" dispersed in memory. Each node contains some data and points to a next node (by storing its address) - except the last node, which has a null "next" pointer. 

A *doubly-linked list* is a modification where each node (except the head) also has a 'previous' pointer, pointing to the element before it in the list. This prev pointer makes inserting or removing elements from the list pretty easy. 

Since nodes aren't contiguous in memory, you can't index into them like you can with arrays. Instead, you need to traverse the list in O(n) time. 

Recursive algorithms go hand-in-hand with linked lists, because each list's first element contains a pointer to a smaller linked list (node.next).

[Next: Hash tables](2_hash_tables.md)