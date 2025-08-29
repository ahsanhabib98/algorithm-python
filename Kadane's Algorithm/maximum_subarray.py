class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxArr = nums[0]
        currSum = 0
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxArr = max(maxArr, currSum)
        return maxArr