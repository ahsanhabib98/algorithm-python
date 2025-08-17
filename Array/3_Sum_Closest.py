class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float("inf")
        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == num:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if abs(threeSum - target) < abs(closest - target):
                    closest = threeSum
                if threeSum == target:
                    return threeSum
                if threeSum < target:
                    l += 1
                else:
                    r -= 1
        return closest