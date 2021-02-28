class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        possible = ["A","C","G","T"]

        queue = [(start,0)]

        while queue:
            word,step = queue.pop(0)
            if word == end:
                return step
            
            for i in range(len(word)):
                for p in possible:
                    temp = word[:i] + p + word[i+1:]
                    if temp in bank:
                        bank.remove(temp)
                        queue.append((temp,step+1))
        
        return -1
