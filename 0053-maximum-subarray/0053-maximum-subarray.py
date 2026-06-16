class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        current=nums[0]
        for i in range(1,len(nums)):
            current=max(nums[i],current+nums[i])
            maxsum=max(maxsum,current)
        return maxsum

        