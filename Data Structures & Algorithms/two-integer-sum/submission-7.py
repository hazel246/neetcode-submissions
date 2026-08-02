class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        A=[]

        for i,num in enumerate(nums):
            A.append([num,i])

            # A= [ [3,0] [4,1] [5,2] [6,3] ]
        A.sort()
            # A = [ [3,0] [4,1] [5,2] [6,3] ]

        i , j = 0, len(nums)-1
        while(i<j):
            #add only the first number of i&j
            curr = A[i][0]+A[j][0]
            if curr == target:
                return [min(A[i][1],A[j][1]),max(A[i][1],A[j][1])]

            elif curr<target:
                i+=1
            else:
                j-=1

        return [] 

        

    