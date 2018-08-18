class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 转换2进制，对0和1处理一下，并转换回来
        result = 0
        binary = ''
        while num:
            binary = binary + str(num % 2)
            num //= 2
        reverse = ''
        for i in binary:
            if i == '1':
                reverse = '0' + reverse
            else:
                reverse = '1' + reverse
        while reverse:
            result *= 2
            result += int(reverse[0])
            reverse = reverse[1:]
        return result