class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        if s == "":
            return -1
        for v in s:
            if v not in dic:
                dic[v] = 1
            else:
                dic[v]+=1
        
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i 
        return -1
