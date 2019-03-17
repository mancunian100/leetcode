## 一种基本方法，使用dict进行两层循环查找，时间复杂度O(n^2)超时不能通过
# class Solution:
#     def findAnagrams(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: List[int]
#         """
#         l1, l2 = len(s), len(p)
#         result = []
#         if l2 == 0:
#             return 0
#         if l1 < l2:
#             return result

#         for i in range(l1-l2+1):
#             if self.isAnagrams(s[i: i+l2], p):
#                 result.append(i)
#         return result
    
#     def isAnagrams(self, s, p):
#         dct = {}
#         for i in p:
#             if i not in dct.keys():
#                 dct[i] = 1
#             else:
#                 dct[i] += 1
#         for i in s:
#             if i not in dct.keys():
#                 return False
#             elif dct[i] > 0:
#                 dct[i] -= 1
#             else:
#                 return False
#         return True

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # 动态改变dict的取值，记住dict变成0后要去掉不然会留下一个0的值
        dct = {}
        for i in p:
            if i not in dct:
                dct[i] = 1
            else:
                dct[i] += 1
        l1, l2 = len(s), len(p)
        scan = {}
        result = []
        for i in range(l1):
            if s[i] not in scan:
                scan[s[i]] = 1
            else:
                scan[s[i]] += 1
            if i >= l2:
                scan[s[i-l2]] -=1
                if scan[s[i-l2]] == 0:
                    del scan[s[i-l2]]
            if scan == dct:
                result.append(i-l2+1)
        return result