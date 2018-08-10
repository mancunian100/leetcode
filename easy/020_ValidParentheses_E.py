class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        smp = ')]}'
        mystr = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        
        if s == '':
            return True
        elif len(s)%2 != 0:
            return False
        elif s[0] in smp:
            return False
        else:
            for i in s:
                if i in smp:
                    if st[-1] == mystr[i]:
                        st.pop(-1)
                    else:
                        return False
                else:
                    st.append(i)
        if st == []:
            return True
        else:
            return False