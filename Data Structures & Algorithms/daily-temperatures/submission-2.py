class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = [] # pair : [index,temp]

        #stack[-1][0] is index, stack[-1][1] is temperature
        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][1]:
                stackInd, stackT=stack.pop()
                res[stackInd]=i-stackInd
            stack.append([i,t])
        

        return res



        