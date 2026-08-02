class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        #A=[]

        #for i,num in enumerate(nums):
            #A.append([num,i])

            # A= [ [3,0] [4,1] [5,2] [6,3] ]
        #A.sort()
            # A = [ [3,0] [4,1] [5,2] [6,3] ]
        

        for i in range(len(nums)): #for 0 and for 1 
            for j in range(i+1,len(nums)):
                curr=nums[i]+nums[j]
                if curr==target:
                    return [i,j]
        return []