class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        target = 0
        for i in range(len(nums)):
            if nums[i] == val:
                target += 1
                nums[i] = "_"

        nums.sort(key=lambda x: x == "_")

        k = len(nums) - target 
        return k
                