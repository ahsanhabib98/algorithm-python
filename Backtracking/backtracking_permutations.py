class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        perm = self.permute(nums[1:])
        res = []
        for p in perm:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res

# Alternate approach
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            return [nums[:]]
        for i in range(len(nums)):
            num = nums.pop(0)
            perms = self.permute(nums)
            for p in perms:
                p.append(num)
            res.extend(perms)
            nums.append(num)
        return res