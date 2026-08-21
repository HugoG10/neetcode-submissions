class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count, ones_count = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ones_count += 1
                if max_count <= ones_count:
                    max_count = ones_count
            else:
                ones_count = 0
        
        return max_count
        
                

        
            