class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        num_count=Counter(nums)
        #num_count={1:1,2:1,3:2}

        is_duplicate=False

        for i in num_count:

            if num_count[i]>1:
                is_duplicate=True
                break

        return is_duplicate

            



