class Solution:
    def maxArea(self, height):
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # Calculate the area between the two lines
            h = min(height[left], height[right])
            w = right - left
            area = h * w

            # Update the maximum area if the current area is greater
            max_area = max(max_area, area)

            # Move the pointers towards each other
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


solution = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = solution.maxArea(height)
print(result)