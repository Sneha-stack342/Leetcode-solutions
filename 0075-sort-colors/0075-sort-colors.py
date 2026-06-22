class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c0=0
        c1=0
        c2=0
        for i in nums:
            if i==0:
                c0+=1
            elif i==1:
                c1+=1
            else:
                c2+=1
        nums[:]=[0]*c0+[1]*c1+[2]*c2
        