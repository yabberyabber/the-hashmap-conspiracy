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

### Go map

The standard go map structure uses a hash table with incremental bucket migration.  Here's a well-documented bit of source code: https://golang.org/src/runtime/hashmap.go.

## Results

This is what `driver.py` outputted when run on my intel quad core 2.4GHz i5-6300U CPU with 12GB of mempory running ubuntu 16.04.  There will be graphs below.

Please do not use these numbres to compare languages.  I'm not posting this data so that someone can claim that rust is faster than go, but so that we can observe the trends in time-per-operation as the sizes of the dataset grows across different implementations.  

Testing: go
dataset size, 20th P, 50th P, 80th P
10000, 0.003705, 0.004616, 0.005528
31622, 0.008861, 0.009598, 0.010335
100000, 0.020216, 0.021233, 0.022251
316227, 0.074205, 0.075378, 0.076552
1000000, 0.274524, 0.276072, 0.277621
3162277, 0.788122, 0.791232, 0.794342
10000000, 2.726348, 2.790962, 2.855576
Testing: rust
dataset size, 20th P, 50th P, 80th P
10000, 0.004413, 0.005331, 0.006249
31622, 0.008531, 0.009731, 0.010930
100000, 0.018307, 0.019321, 0.020335
316227, 0.062687, 0.063734, 0.064782
1000000, 0.234094, 0.237526, 0.240959
3162277, 0.698331, 0.744924, 0.791517
10000000, 2.362844, 2.545147, 2.727451
Testing: python
dataset size, 20th P, 50th P, 80th P
10000, 0.046060, 0.048722, 0.051385
31622, 0.074649, 0.091812, 0.108975
100000, 0.204210, 0.215228, 0.226247
316227, 0.617434, 0.624623, 0.631812
1000000, 1.823924, 1.842821, 1.861719
3162277, 5.831359, 6.175946, 6.520533
10000000, 20.035813, 21.017678, 21.999544
Testing: java
dataset size, 20th P, 50th P, 80th P
10000, 0.068792, 0.079755, 0.090717
31622, 0.067202, 0.112156, 0.157111
100000, 0.087700, 0.100021, 0.112342
316227, 0.118738, 0.132630, 0.146521
1000000, 0.291819, 0.325159, 0.358499
3162277, 2.083085, 2.324210, 2.565336
10000000, 8.781392, 9.947415, 11.113438
Testing: cpp
dataset size, 20th P, 50th P, 80th P
10000, 0.007208, 0.013016, 0.018824
31622, 0.018381, 0.035450, 0.052518
100000, 0.062319, 0.064199, 0.066079
316227, 0.266117, 0.269334, 0.272552
1000000, 0.832129, 0.999752, 1.167374
3162277, 3.215985, 3.497020, 3.778054
10000000, 11.819442, 12.256050, 12.692659

### cpp std::unordered_map

![graph for c++](/cpp.png?raw=true "C++ Performance")

### go

![graph for go](/go.png?raw=true "go Performance")

### java.util.HashMap

![graph for java.util.HashMap](/java.png?raw=true "java.util.HashMap Performance")

### python dictionary

![graph for python dict](/python.png?raw=true "Java dict Performance")

### Rust std::collections::HashMap

![Graph for rust's std::collections::HashMap](/rust.png?raw=true "Rust std::collections::HashMap")
