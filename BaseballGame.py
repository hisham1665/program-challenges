#leet code no 682
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for  ch in operations:
            if ch == '+' :
                su = record[-1] + record[-2] 
                record.append(su)
            elif  ch == 'D' :
                pro = record[-1] * 2
                record.append(pro)
            elif ch =='C' :
                record.pop()
            else :
                record.append(int(ch))
        return sum(record)
