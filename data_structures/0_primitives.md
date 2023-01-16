# Primitives

Note: this section is heavily based on C. 


## Bits and Bytes ##
Bits are the most fundamental element of computer science - like atoms in the life sciences. A bit can be either 1 or 0, "on" or "off". How on Earth does a computer store a bit? This isn't a physics blog, but the simplest explanation is that it's often a tiny dent or magnetic region on disk or other types of hardware.

8 bits together form one "byte", and usually 4 bytes make up one "word". Generally, a character takes up one byte, and any number takes up one word (4 bytes x 8 bits = 32 bits in one word). 


## Char ##
In C, each char takes up one byte and is stored as an integer from -128 to 127 or 0 to 255. Each integer is mapped to a character using a specified maapping, for example ASCII ("American Standard Code for Information Interchange") [1]. 

## Numbers ## 
Now let's think about storing one unsigned (non-negative) integer. We use one word (32 bits) to store the integer, so the largest value we can have is 2^32 - 1. Why? There are two possible values (0 and 1), and 32 slots to store those in. 

We only have to make a slight adjustment to support signed integers (negative or positive): use the leftmost bit to represent the sign. This broadens our range enormously - we can now store anything from -2^31 - 1 to +2^31 - 1! (2^31 is approximately 2.1 billion). 

Now let's make things a bit more complicated. How do we support real numbers, like floats? 

A floating-point number in memory has three separate parts: the sign bit, exponent (e), and "mantissa" (m). It represents the number m x 2^e.  [TODO]




Next: [Arrays and strings](1_arrays_and_strings.md)

## Sources
1. https://iq.opengenus.org/character-in-c/amp/
2. statmath.wu.ac.at (TODO)