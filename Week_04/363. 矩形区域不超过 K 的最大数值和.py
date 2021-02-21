class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def dpmax(arr,k):
            rollsum = arr[0]
            rollmax = rollsum
            for i in range(1,len(arr)):
                if rollsum >0:
                    rollsum += arr[i]
                else:
                    rollsum = arr[i]
                if rollsum > rollmax:
                    rollmax = rollsum
            if rollmax <= k:
                return rollmax
            
            max_r = float('-inf')
            for i in range(len(arr)):
                sum_t = 0
                for j in range(i,len(arr)):
                    sum_t += arr[j]
                    if sum_t>max_r and sum_t<=k:
                        max_r = sum_t
                    if max_r==k:
                        return k
            return max_r

            


        r,c = len(matrix),len(matrix[0])
        max_r = float('-inf')


        for i in range(c):
            rowsum = [0]*r
            for j in range(i,c):
                for l in range(r):
                    rowsum[l] += matrix[l][j]
                max_r = max(max_r,dpmax(rowsum,k))
                if max_r == k:
                    return k
        return max_r
