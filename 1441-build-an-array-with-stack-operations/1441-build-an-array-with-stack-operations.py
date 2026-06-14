class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        r=[]
        for i in range(1,target[-1]+1):
            if i in target:
                r.append("Push")
            elif i not in target:
                r.append("Push")
                r.append("Pop")
        return r



            

           