'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
'''


class Solution:
    def binarySearch(self, nums, target, start, end):
        if end < start:
            return -1
        mid = (start+end)//2
        if nums[mid] == target:
            return mid
        if nums[start] <= target < nums[mid]:  # left side is sorted and has target
            return self.binarySearch(nums, target, start, mid-1)
        elif nums[mid] < target <= nums[end]:  # right side is sorted and has target
            return self.binarySearch(nums, target, mid+1, end)
        elif nums[mid] > nums[end]:  # right side is pivoted
            return self.binarySearch(nums, target, mid+1, end)
        else:  # left side is pivoted
            return self.binarySearch(nums, target, start, mid-1)

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        return self.binarySearch(nums, target, 0, len(nums)-1)
