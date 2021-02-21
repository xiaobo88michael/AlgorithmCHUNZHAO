class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = collections.defaultdict(int)
        for c in t:
            need[c]+=1
        needcnt = len(t)
        res = (0,float('inf'))
        i = 0
        for j,v in enumerate(s):
            if need[v]>0:
                needcnt-=1
            need[v]-=1
            if needcnt==0:
                while True:
                    c=s[i]
                    if need[c]==0:
                        break
                    need[c]+=1
                    i+=1
                if j-i<res[1]-res[0]:
                    res=(i,j)
                need[s[i]]+=1
                needcnt+=1
                i+=1
        return "" if res[1]>len(s) else s[res[0]:res[1]+1]
