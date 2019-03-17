class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 赖皮使用int转换为int求和，再把大于1的位进位处理
        result = ''
        s = str(int(a) + int(b))
        l = len(s)
        count = 0
        for i in range(l):
            temp = int(s[l-1-i]) + count
            count = 0
            if temp > 1:
                result = str(temp-2) + result
                count = 1
            else:
                result = str(temp) + result
        if count == 1:
            result = '1' + result
        return str(result)