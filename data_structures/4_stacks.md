# Stacks

Coming soon


A stack is last in, first out. Picture a huge stack of plates - you can only add to the top or take plates off one at a time, but can't access plates anywhere else (without them toppling over!).

How are stacks implemented under the hood? As with most data structures, there are multiple approaches. One very simple approach is with an array. 

## Array implementation  ##

Say you want a stack with a fixed limit, for example 100 elements. First initialize an array of size 100. When "pushing" an item onto the stack, first check the size - if we aren't over limit, insert the item at the next empty position. When popping, retrieve the last item in the array, delete it, and return it. 

If we want a stack with a really large limit, it wouldn't be efficient to allocate a gigantic array right off the bat - what if we only use the first few elements? Instead, we can optimize with the dynamic resizing approach. For example, we start with an array of size x and double the array each time we run out of space. Note that "doubling" the array isn't trivial - we need to allocate double the memory, then copy all elements over to the new array, and finally add the new one. (TODO: amortized cost of insert)

## Linked list implementation ##

One benefit of using a linked list over an array is that we can allocate exactly how much space we need, and just keep adding nodes as we go along. 




## Practice ##
- https://leetcode.com/problems/design-a-stack-with-increment-operation/

Next: [Queues](5_queues.md)