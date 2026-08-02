class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #target=7


        prevMap={} #assume 2:0 in there after 1st iteration

        for i,num in enumerate(nums): #(1:5)
            diff=target-num #7-5=2 

            if diff in prevMap: #2 is in prevMap so
                return [prevMap[diff],i]
            prevMap[num]=i #or else add it to prevMap, this is how 2 was added




        

    