# Bit manipulation

## Why do it?

As an early CS student, I had no idea why bit operations were worth learning. Why work with data on the bit level, instead of using language abstractions like usual? 

Then at my first internship I had to use a bitmask to represent some boolean flags in a small message, and I started thinking about this stuff a bit more. The short answer is that they can make code faster and more efficient in certain circumstances, especially when memory is limited. Frequently these are low-level programs, like embedded devices or encryption.

It's also a good in-road to brushing up on (or learning) the fundamentals of how data is represented in memory. While language abstractions are a beautiful thing, understanding the basic building blocks can help us write better code and make sense of things at a deeper level. 

Address space is broken up into bytes (usually 8 bits). So if you want to store the boolean 'true', it will go into one byte - 0000 0001 [1]. That doesn't seem the most efficient, does it?


## Common operators

- NOT: AKA "bitwise complement", negates each bit. Ex]  ^ "0011 1111" -> "1100 0000"
- AND: Performs **logical AND** on the corresponding bits in two inputs. Ex]  "1111 0000" & "1100 1111" -> "1100 0000"
- OR: Performs **inclusive OR** on corresponding bits.  Ex]  "1111 1100" | "0000 1111" -> "1111 1111"
- XOR: Performs **exclusive OR** on corresponding bits.  Ex] "1111 1100" | "0000 1111" -> "1111 0000"


## Bit shifts



## Two's complement


## More practice 
- https://leetcode.com/problems/single-number/



Sources:
1. https://www.alexhyett.com/bitwise-operators/



