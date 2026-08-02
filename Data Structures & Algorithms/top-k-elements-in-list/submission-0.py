from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Count frequency of each number
        count = Counter(nums)

        # Step 2: Create buckets
        # Index i will store numbers that appear exactly i times
        buckets = [[] for _ in range(len(nums) + 1)]

        # Step 3: Place each number into the bucket matching its frequency
        for num, freq in count.items():
            buckets[freq].append(num)

        # Step 4: Start from the highest frequency bucket and collect results
        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res