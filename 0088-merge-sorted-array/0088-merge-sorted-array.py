class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        a=nums1[:m]
        d=a+nums2
        d.sort()
        for i in range(m+n):
            nums1[i]=d[i]
        
        