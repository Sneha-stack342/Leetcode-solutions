class Solution:
    def calPoints(self, operations: List[str]) -> int:
        r=[]
        for i in range(len(operations)):
            if operations[i] not in "CD+":
                r.append(int(operations[i]))
            elif operations[i]=="C":
                r.pop()
            elif operations[i]=="D":
                r.append(2*r[-1])
            elif operations[i]=="+":
                a=r[-1]+r[-2]
                r.append(a)
               
        return sum(r)

                          

                



        

        