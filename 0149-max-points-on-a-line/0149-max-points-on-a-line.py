from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        max_points = 2  

        for i in range(len(points)):
            slope_count = defaultdict(int)
            duplicate = 0
            local_max = 0

            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 == x2 and y1 == y2:
                    duplicate += 1
                elif x1 == x2:
                    slope = 'inf'
                    slope_count[slope] += 1
                    local_max = max(local_max, slope_count[slope])
                else:
                    slope = (y2 - y1) / (x2 - x1)
                    slope_count[slope] += 1
                    local_max = max(local_max, slope_count[slope])

            max_points = max(max_points, local_max + duplicate + 1)

        return max_points
