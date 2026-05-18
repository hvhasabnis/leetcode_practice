class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals.sort()

        merged: list[list[int]] = []

        if len(intervals) > 0:
            merged.append(intervals[0])

        mergedLength = 1

        for index in range(1, len(intervals)):
            if(merged[mergedLength - 1][0] <= intervals[index][0] and merged[mergedLength - 1][1] >= intervals[index][0]):
                finalElement = [
                    min(merged[mergedLength - 1][0], intervals[index][0]),
                    max(merged[mergedLength - 1][1], intervals[index][1])
                ]
                merged.pop()
                merged.append(finalElement)
            else:
                merged.append(intervals[index])
                mergedLength += 1

        return merged
        
def main():
    s = Solution()
    solution = s.merge([[1,3],[2,6],[8,10],[15,18]])

    print(solution, end=" ")

main()