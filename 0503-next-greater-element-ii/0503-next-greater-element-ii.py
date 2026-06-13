class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        r=[]
        a=nums+nums
        for i in range(len(nums)):
            x=nums[i]
            d=a[i+1:len(a)]
            for j in d:
                if j>x:
                    r.append(j)
                    break
            else:
                r.append(-1)
        return r
            
        
           

            
