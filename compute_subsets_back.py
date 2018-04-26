"""

A backtracking solution to compute all subsets via voodoo, also known as backtracking...

Developed exclusively on:

Pythonista 3 by omz:software

https://itunes.apple.com/us/app/pythonista-3/id1085978097?mt=8

author:  c.gleeson 2018

"""
import timeit

def compute_subsets(nums):
    """
    compute all subsets via backtracking
    """
    subsets = []
    backtrack(subsets, [], nums, 0)
    print("Number of subsets computed for set:\n%s \nis:%s" % (nums, len(subsets)))
    print("Time spent in seconds:")
    return subsets

def backtrack(subsets, temp, nums, start):
    print(temp)
    subsets.append(temp)
    for i in range(start, len(nums)):
        backtrack(subsets, temp + [nums[i]], nums, i + 1)

def a_timer(n):
    _setup = 'from __main__ import compute_subsets'
    _call = 'compute_subsets(range(0,' + str(n) + '))'
    # timeit.repeat statement
    times = timeit.repeat(setup = _setup,
                          stmt = _call,
                          repeat = 1,
                          number = 1)
    return times



if __name__ == "__main__":
    #testing
    size_of_set = 16
    print(a_timer(size_of_set))
