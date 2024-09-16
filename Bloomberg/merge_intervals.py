class Solution:
    def mergeIntervals(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for current in intervals[1:]:
            previous = merged[-1]

            if current[0] <= previous[1]:
                previous[1] = max(previous[1], current[1])
            else:
                merged.append(current)
        
        return merged
    
solution = Solution()

interOne = [[1,3],[2,6],[8,10],[15,18]]
interTwo = [[1,4],[4,5]]

resultOne = solution.mergeIntervals(interOne)
resultTwo = solution.mergeIntervals(interTwo)

print( f"Result One: ${resultOne}\nResult Two: ${resultTwo}")