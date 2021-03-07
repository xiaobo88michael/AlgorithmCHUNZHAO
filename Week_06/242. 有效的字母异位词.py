class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        words = [chr(i) for i in range(97,123)]
        value = [0]*26
        wordDict_s = dict(zip(words,value))
        wordDict_t = dict(zip(words,value))
        for word in s:
            wordDict_s[word] += 1
        for word in t:
            wordDict_t[word] += 1
        if wordDict_s == wordDict_t:
            return True
        return False
