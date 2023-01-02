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

## SSTables/ LSM-Trees/ Memtables 

The LSM Tree is another log-structured database variant - it stands for "Log Structured Merge Tree". Here we want our key-values to be sorted, maybe to optimize range queries, or maybe for other reasons.

The approach is fairly simple. We keep a balanced in-memory tree of our choice (red-black, AVL tree, etc.) to store the data in sorted order. We add the keys to this tree as they are inserted, and then at some point, write the KV-pairs in sorted order out to a file. This tree is also known as a *memtable*. 

The file we write the sorted pairs to is called the SSTable (Sorted String Table). We keep many of these, each a "segment" as explained above. We also merge and compact these ever so often: deleting keys, discarding outdated values, and keeping the merged tables sorted. 

So, how do we find something by key? First check the memtable. If it's not there, start checking each SSTable from newest to oldest. 

At first I thought it'd be easy to find a key if present in an SSTable: we can use binary search, right? Not so fast. Every record can have a completely different size, which makes binary search tricky (it would involve a lot of scanning for keys). A simpler approach is to maintain a "sparse hash index" alongside the memtable in memory. Similar to the keywords at the top of each page in a real-world dictionary, we keep some subset of the keys and their corresponding byte offsets in the file. Then, if we want to find a word, we find a key close to it alphabetically in the hash index, and scan from there onward. 

Since we're inserting keys in-memory, what happens if the program crashes? The answer is simple: immediately write every transaction to a log on disk, which can be used later to restore the memtable if needed. Once the memtable is written to an SSTable, the recovery log can be deleted.

One concern when using SSTables is that it can take a really long time to find a word that *doesn't* exist in the database. We have to scan every SSTable ever created to make sure it isn't there. One optimization is to use a [bloom filter](https://brilliant.org/wiki/bloom-filter/#:~:text=A%20bloom%20filter%20is%20a,is%20added%20to%20the%20set.): this tells us quickly whether the key is not in the database. 

## Test & solidify knowledge 

## More resources

[Google's paper on Bigtable](https://static.googleusercontent.com/media/research.google.com/en//archive/bigtable-osdi06.pdf), their influential home-grown database which uses SSTables. 

 