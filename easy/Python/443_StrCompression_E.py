class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) < 2:
            return len(chars)
        
        count = 1
        item = chars[0]
        s = ''
        for i in chars[1:]:
            if i != item:
                s += item
                if count > 1:
                     s += str(count)
                item = i
                count = 1
            else:
                count += 1
                
        s += item
        if count > 1:
            s += str(count)
            
        ls = list(s)
        chars[0:len(ls)] = ls
        return len(ls)
        