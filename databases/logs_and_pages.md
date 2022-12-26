# Log-structured storage engines

## Resources

 - [Designing Data-Intensive Applications](https://www.amazon.com/Designing-Data-Intensive-Applications-Reliable-Maintainable/dp/1449373321) by Martin Kleppmann

## Logs

A log is an append-only data file. This makes writing to it efficient, and usually done by only one thread. Binary is the most efficient way of encoding these files. Logs often store key-value pairs, where the most recent value should be retrievable by key.

## Hash index

A *hash index* is a data structure that complements key-value log storage nicely. Imagine that we have one log file of key-value pairs: we will keep an in-memory hash table where each key maps to the byte offset of the latest value. This makes reading much faster than if we had to scan the file backwards to find the key. 

Image: https://ebrary.net/htm/img/15/554/17.png

One real-world example of this is [Bitcask](https://docs.riak.com/riak/kv/2.2.3/setup/planning/backend/bitcask/index.html). 

How do we avoid running out of space when writing is append-only? *Segmentation and compaction*. We write logs to one "segment", or fixed-size file, then move on to a new file, and so on. Some time after each segment's filled, a background thread performs compaction: it removes all duplicate keys, and only keeps the most recent value for each key. This compacted segment is written to a new file, and the old one is deleted once reads are switched to the new file. Finally, we make sure to also merge compressed segments together: this prevents data fragmentation, and ideally keeps the number of segment files small.

Note that since we have multiple segment files, we need to keep one hash index for each. When looking up a value, we start with the most recent index and move backwards. 

What are the cons of using a hash index? For one, we need to keep all keys in memory - if we have too many for that, keeping hash maps on disk isn't really an option, so we're out of luck. Also, range queries are inefficient (key-value data isn't sorted), so if your application needs to make a lot of those, this won't be a good fit. 

## Coming soon: SSTables & LSM-Trees

## Test & solidify knowledge 

 - https://leetcode.com/problems/design-hashmap/
 - Please read Designing Data-Intensive Applications (linked above). It's fantastic and goes much more into depth. 
