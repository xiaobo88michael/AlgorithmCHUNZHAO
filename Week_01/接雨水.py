class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        sums = 0
        stack = []
        current = 0

        while current < len(height):
            while len(stack)!=0 and height[current] > height[stack[-1]]:
                h = height[stack[-1]]
                stack = stack[:len(stack)-1]
                if len(stack)==0:
                    break
                distance = current - stack[-1] -1
                mins = min(height[current],height[stack[-1]])
                sums += (mins - h) * distance
            
            stack.append(current)
            current+=1
        
        return sums
