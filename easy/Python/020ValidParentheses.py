class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 每增加一个左括号就在堆栈种增加一个一样的的，每遇到一个右括号就在堆栈中消去对应的左括号
        # 如果没有对应的就错误，如果最后堆栈是空的就返回正确
        if len(s) % 2 != 0:
            return False
        stack = []
        dct = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i in dct.values():
                stack.append(i)
            else:
                if stack == [] or dct[i] != stack.pop():
                    return False
        return stack == []