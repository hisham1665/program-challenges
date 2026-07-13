class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        i = 0
        num = len(tickets)
        count = 0
        while tickets[k] != 0:
            if tickets[i] > 0 :
                tickets[i] -= 1
                count += 1
            i = (i+1) % num
        return count
