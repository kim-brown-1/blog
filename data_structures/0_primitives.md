# Primitives

Coming soon.

Note: this section is heavily based on C. 

How are they represented in memory? 

## Bits and Bytes ##
How the heck does a computer store a bit anyway? 
This isn't a physics blog, so we'll only shortly touch base on this. A bit can be either 1 or 0, "on" or "off". It might be a "tiny dent on a CD or DVD" [2] or a magnetic region. 

8 bits together are one byte, and 4 bytes are a word (usually). Frequently, a character (char) takes up one byte, and any number takes up one word (4 bytes x 8 bits = 32 bits). 

TODO: hex/ octal, binary


## Char ##

In C, each char takes up one byte and is stored as an integer from -128 to 127 or 0 to 255 (?). Each integer is mapped to a character using a specified maapping, for example ASCII ("American Standard Code for Information Interchange") [1]. 

## Numbers ## 

TODO: signed/ unsigned int, float, etc.

An unsigned int is pretty simple. We use one word (32 bits) to store the integer, so the largest value we can have is 2^32 - 1. 

We only have to make a slight adjustment to support negative numbers: use the leftmost bit to represent the sign of a number. This makes the range -2^31 - 1 to +2^31 - 1. 2^31 is approximately 2.1 billion. 

Now let's make things a bit more complicated. How do we support real numbers, like floats? 

A floating-point number in memory has three separate parts: the sign bit, exponent (e), and "mantissa" (m). It represents the number m x 2^e.  





Next: [Arrays and strings](1_arrays_and_strings.md)

## Sources
1. https://iq.opengenus.org/character-in-c/amp/
2. statmath.wu.ac.at (TODO)