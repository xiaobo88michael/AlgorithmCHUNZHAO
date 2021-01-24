class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        res = []

        for i in range(len(strs)):
            temp = strs[i]
            temp="".join((lambda x:(x.sort(),x)[1])(list(temp)))
            if temp not in dic:
                dic[temp]=[strs[i]]
            else:
                dic[temp].append(strs[i])
            
        
        for i in dic:
            res.append(dic[i])
        
        return res
