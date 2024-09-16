# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

class Solution:
    def mergeIntervals(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        
        # sort intervals in ascending order using their start times
        intervals.sort(key=lambda x: x[0])

        # list to store merged intervals initialized with the first interval
        merged = [intervals[0]]

        for current in intervals[1:]:
            # last interval in the merged list
            previous = merged[-1]

            # where the end time of an earlier interval is greater than the current
            if current[0] <= previous[1]:
                previous[1] = max(previous[1], current[1])
            else:
                merged.append(current)
        
        return merged
    
solution = Solution()

# test cases
interOne = [[1,3],[2,6],[8,10],[15,18]]
interTwo = [[1,4],[4,5]]

resultOne = solution.mergeIntervals(interOne)
resultTwo = solution.mergeIntervals(interTwo)

print( f"Result One: ${resultOne}\nResult Two: ${resultTwo}")