class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        path = []
        dic = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        n = len(digits)
        if n==0:
            return res
        
        def backtrack(index):
            if index == n:
                res.append("".join(path))
            else:
                digit = digits[index]
                for i in dic[digit]:

                    path.append(i)
                    backtrack(index+1)
                    path.pop()
        
        backtrack(0)
        return res
