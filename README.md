# The hash map conspiracy

There's a conspiracy afoot.  If you look at any introductory data structures textbook, they'll tell you a heinous lie.  They'll tell you something which is both theoretically and practically false.

This lie is so insidious and pervasive that it's even in wikipedia.  Check this shit: https://en.wikipedia.org/wiki/Hash_table.  See that box on the right that lists the average and worst case complexity for insertion and search on the hash table?  That's a conspiracy.  The man is trying to bring you down.  Don't listen to him, we're going to forge our own path.

This experiment was inspired by a blog post by one of my professors at Cal Poly: https://www.brinckerhoff.org/blog/2017/05/25/hash-table-timings/.  My aim here is to expand the findings to other hash table implementations and other runtime environments.  I also aim to find out why this lie is so pervasive, and to find the fallacious arguments people use to support this "constant time conspiracy".  

## Experimental design

All the source code and results for this experiment are stored in this repository.  One should be able to reproduce all the computation done here simply by calling `make`.  Each subdirectory contains a different implementation of a hash table.  Each executable file takes in one argument which is the size of the table to operate on.  We operate on tables ranging from 10^5 to 10^8 entries.  For each dataset size, we run 11 trials and report the median result as well as an approximation of the inner quartile range.  

Below are the different hash table implementations we used.

### C++ with stl::unordered_map

Interestingly enough, the stl::map is implemented using a red/black tree.  The stl::unordered_map, however, is implemented as a classic array mapping hashes-mod-something to linked-list-buckets.  

### Java with java.util.HashMap

For details, check out https://docs.oracle.com/javase/7/docs/api/java/util/HashMap.html.  Surprisingly, the javadoc goes into fair detail about the exact implementation used.
