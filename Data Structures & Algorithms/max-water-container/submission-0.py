class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0

        l = 0
        r = len(heights) - 1
        while(l < r):
            new_area = (r - l) * min(heights[l], heights[r])
            area = max(new_area, area)

            if(heights[l] > heights[r]):
                r -= 1
            else:
                l += 1
        return area