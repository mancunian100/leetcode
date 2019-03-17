class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        # 学习了类似于张量的扫描式的搜索方法
        # 注意可以对minutesToTest // minutesToDie进行＋1因为最后还没死的话就是最后一个有毒，排除法
        if buckets == 1:
            return 0
        unit = minutesToTest // minutesToDie + 1
        result = 1
        while unit**result < buckets:
            result += 1
        return result