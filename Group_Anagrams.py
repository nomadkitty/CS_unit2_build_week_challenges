'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        '''
        idea 2: sort each word of the list
        build a dictionary with key of sorted words and indices in the strs array
        return the words of indices of the array
        '''
        result = []
        # sort each word in the given array
        wordSort = ["".join(sorted(word)) for word in strs]

        # create a dictionary with indieces array as value, sorted word as key
        dict = {}
        for idx, ele in enumerate(wordSort):
            dict.setdefault(ele, []).append(idx)

        # append the words according to the dict values
        for idxlist in dict.values():
            result.append([strs[i] for i in idxlist])
        return result
