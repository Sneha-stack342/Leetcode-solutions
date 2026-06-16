class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            r=len(str(i))
            if r%2==0:
                c+=1
        return c


