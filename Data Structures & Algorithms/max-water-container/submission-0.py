class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = []
        for i, a in enumerate(heights):
            for j, b in enumerate(heights):
                minValue = min(a, b)
                indexValue = j - i
                res.append(minValue * indexValue)
        return max(res)

