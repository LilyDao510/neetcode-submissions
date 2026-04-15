class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = len(heights)
        l,r = 0, i- 1
        max_res = 0

        while l < r:
            a = r -l
            res = a * min(heights[r],heights[l])
            max_res = max(max_res,res)

            if heights[r] < heights[l]:
                r -= 1
            elif heights[r] >= heights[l]:
                l += 1
        return max_res


        