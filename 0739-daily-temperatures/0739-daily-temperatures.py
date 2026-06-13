class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        a=len(temperatures)
        s=[0]*a
        for i in range(a-1,-1,-1):
            while stack and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop()
            if stack:
                s[i]=stack[-1]-i
            stack.append(i)
        return s

            

    
   
            

        