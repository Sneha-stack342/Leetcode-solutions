class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r=[]
        for i in range(len(nums1)):
            x=nums1[i]
            for j in range(len(nums2)):
                if nums2[j]==x:
                    d=nums2[j+1:len(nums2)]
                    for k in d:
                        if k>x:
                            r.append(k)
                            break
                    else:
                        r.append(-1)
        return r

               
        