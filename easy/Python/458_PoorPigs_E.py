class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        # 本题考虑多维编码 
        status = minutesToTest // minutesToDie + 1
        
        if buckets == 1:
            return 0
        
        re, pigs = status, 1
        while re < buckets:
            re *= status
            pigs += 1
            
        return pigs