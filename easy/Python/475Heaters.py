class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        # 这题对边界的处理感觉很巧妙，我自己想不出来，这题是直接搬的答案
        houses.sort()
        heaters.sort()
        radius, i = 0, 0
        for house in houses:
            while i < len(heaters) and heaters[i] < house:
                i += 1
            if i == 0:
                radius = max(radius, heaters[i] - house)
            elif i == len(heaters):
                radius = max(radius, houses[-1] - heaters[-1])
            else:
                radius = max(radius, min(house - heaters[i-1], heaters[i] - house))
        return radius