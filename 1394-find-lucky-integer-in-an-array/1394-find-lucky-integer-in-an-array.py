class Solution:
    def findLucky(self, arr: List[int]) -> int:
        r=[]
        for i in arr:
            a=arr.count(i)
            if i==a:
                r.append(i)
        if r:
            return max(r)
        return -1
        