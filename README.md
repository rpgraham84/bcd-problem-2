Random Ad problem for BCD Travel
==============================================


Problem Description
-------------------

It is time to earn some money, so let us show Ads. We have many ads and we need to serve them equally. In other words, assume you have an array of N unique Ad ids in a file. It is big, but still fits in memory. So it is better not to copy this list, in other words additional memory might be constant. You have to print K equally distributed random unique Ad ids from this list. Items should not recur as we don’t want to show the same Ad twice. 

Input​: The file with unique Ad ids, one per line and K number of random Ad ids to print.

Output​: K random, equally distributed non-recurring Ad ids .


Design and Rationale
--------------------
Anybody can import random and use shuffle to solve this problem. I wanted to add
a twist to the challenge by not importing random. Instead, I implemented my
own Knuth-Durstenfeld shuffle algorithm (which is the same algorithm as 
random.shuffle) that uses os.urandom for its "roll." The unittests can't
confirm the even distribution of the data, but I did write 2 tests to verify what
could be shown by testing. One test ensures that if k is larger than the number 
of lines in the file, a ValueError is thrown. The other test confirms that no
line appears more than once.


Usage
-----

````bash
python solution.py <input_file> <k>
````

Should print k unique lines from input_file with no repeats, uniformly distributed.



Testing
-------

````bash
python -m unittest -v tests.solution_tests
````

