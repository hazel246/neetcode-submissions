from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums):
        freq = Counter(nums)

        pairs = 0

        for count in freq.values():
            pairs += count * (count - 1) // 2

        return pairs
        