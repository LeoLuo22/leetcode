class Solution:
    def removeElement(self, nums, val):
        if val not in nums:
            return len(nums)
        nums.remove(val)
        return self.removeElement(nums, val)
