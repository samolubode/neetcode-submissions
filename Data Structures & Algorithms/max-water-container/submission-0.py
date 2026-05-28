class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # calc maxWater
        # shift the lesser arm every time
        i = 0
        j = len(heights) - 1
        maxWater = 0

        while i < j:
            # shorter height
            sh = min(heights[j], heights[i])
            # water
            water = sh * (j - i)
            # max water
            maxWater = max(maxWater, water)

            if heights[j] > heights[i]:
                i += 1
            else:
                j -= 1
        
        return maxWater

        
        