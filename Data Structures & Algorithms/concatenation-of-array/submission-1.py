class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_length, ans_length = len(nums), 2 * len(nums)
        ans = nums + nums
        return ans


        