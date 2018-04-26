# compute_subsets_backtrack
A quick way to compute all subsets of a range of numbers via backtracking, developed on Pythonista 3

If you are like...what?  "A real python env on mobile?", check out the following:
https://itunes.apple.com/us/app/pythonista-3/id1085978097?mt=8

# Tuning:
To tune the size of the computation done here, please change the value of size_of_set in the main routine

An example real run time on a modern osx laptop for a set of 16 elements (65536 subsets):  ~3.2 sec

An example real run time on an iPhone6 SE with no other apps running for a set of only 12 elements (4096 subsets): ~3.86 sec

# Sample output (truncated for obvious reasons):

`[]\
[0]\
[0, 1]\
[0, 1, 2]
[0, 1, 2, 3]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4, 5]
[0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
...
<output truncated massively>
...
[11, 13, 14, 15]
[11, 13, 15]
[11, 14]
[11, 14, 15]
[11, 15]
[12]
[12, 13]
[12, 13, 14]
[12, 13, 14, 15]
[12, 13, 15]
[12, 14]
[12, 14, 15]
[12, 15]
[13]
[13, 14]
[13, 14, 15]
[13, 15]
[14]
[14, 15]
[15]
Number of subsets computed for set:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
is:65536
Time spent in seconds:
[3.2600250244140625]`
