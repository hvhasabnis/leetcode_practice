class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)

        left: list[int] = [1] * length
        right: list[int] = [1] * length

        for index in range(1, length):
            left[index] = left[index - 1] * nums[index - 1]

        for index in range(1, length):
            right[index] = right[index - 1] * nums[length - index]

        for index in range(0, length):
            left[index] = left[index] * right[length - index - 1]

        return left

def main():
   s = Solution()
   answerList = s.productExceptSelf([1,2,3,4])

   for answer in answerList:
       print(answer, end = " ")

main()