class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        freq = collections.Counter(tasks)

        maxExec = max(freq.values())

        maxCount = sum(1 for v in freq.values() if v==maxExec)

        return max((maxExec-1)*(n+1)+maxCount,len(tasks))
