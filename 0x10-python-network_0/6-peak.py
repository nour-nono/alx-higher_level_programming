#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""
    if list_of_integers is None or list_of_integers == []:
        return None
    n = len(nums)
    low, high = 0, n-1
    if n == 1 or nums[0] > nums[1]:
        return list_of_integers[0]
    if nums[-1] > nums[-2]:
        return list_of_integers[n-1]
    while low <= high:
        mid = ((high-low)//2) + low
        # Peak element is present in right side
        if nums[mid] < nums[mid+1]:
            low = mid+1
        # Peak element is present in left side
        elif nums[mid] < nums[mid-1]:
            high = mid-1
        else:
            return list_of_integers[mid]
