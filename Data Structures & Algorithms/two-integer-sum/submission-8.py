class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        indices={}

        # A mein num, aur uska index store krna 

        for i,num in enumerate(nums): # (0,3),(1,4),(2,5),(3,6)
            indices[num]=i # { 3:0, 4:1, 5:2, 6:3 }

        # find the diff between target and curr

        for i,num in enumerate(nums):  # (0,3),(1,4),(2,5),(3,6) i= 0,1 num=2,3
            diff=target-num #7-3=4 
            # is 4 in the indices dict?
            if diff in indices and indices[diff] != i: #indices[4]=1 and i= 0 so yea, basically this is for not counting a number as a duplicate
                return [i,indices[diff]]
        
        return []




        

    