// https://leetcode.com/problems/best-poker-hand

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:

        def flush():

            for i in range(1, len(suits)):

                if not suits[i-1] == suits[i]:
                    return False
            
            return True


        def kinds():

            max_kinds = 1
            countMap = {}

            for rank in ranks:

                if countMap.get(rank) != None:
                    countMap[rank] += 1
                    max_kinds = max(countMap.get(rank), max_kinds)
                else: 
                    countMap[rank] = 1

            return max_kinds 

        if flush():
            return "Flush"

        kinds = kinds()
        if kinds == 1: 
            return "High Card"
        if kinds == 2:
            return "Pair"
        if kinds >= 3:
            return "Three of a Kind"
            


                    

            

            

            
        
        