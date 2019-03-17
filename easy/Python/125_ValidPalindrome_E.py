class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ss = ''
        for i in s:
            if i.isalnum():
                ss += i
        ss = ss.lower() 
        
        l = int(len(ss)/2)
        for i in range(0, l):
            if ss[i] != ss[-1-i]:
                return False
        return True

s = "0p"
re = Solution().isPalindrome(s)
print(re)