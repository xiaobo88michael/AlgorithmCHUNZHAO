class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        a = reversed(s.split())
       
        return " ".join(a)
