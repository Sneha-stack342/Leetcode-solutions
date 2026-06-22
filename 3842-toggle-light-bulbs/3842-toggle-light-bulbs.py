class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        bulbs.sort()
        r=[]
        for i in bulbs:
            a=bulbs.count(i)
            if a%2!=0 and i not in r:
                r.append(i)
        return r

        