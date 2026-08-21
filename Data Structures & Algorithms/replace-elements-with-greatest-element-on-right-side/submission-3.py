class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_most = -1
        for i in range(len(arr) - 1, -1, -1):
            new_max = max(arr[i], right_most)
            arr[i] = right_most
            right_most = new_max
        return arr
        