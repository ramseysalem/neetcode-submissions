class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [] # pair of [temp, index]

        result = [0] * len(temperatures)

        for i, n in enumerate(temperatures):

            while stack and n > stack[-1][0]:
                stackN, stackI = stack.pop() 
                result[stackI] = (i - stackI)
            stack.append([n, i])
        return result 









                





        