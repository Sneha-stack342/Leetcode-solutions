class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        d=len(nums)
        act=d*(d+1)//2
        acs=sum(nums)
        return act-acs
        