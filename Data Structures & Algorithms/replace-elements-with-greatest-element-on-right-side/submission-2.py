class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = 0
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
                break
            else:
                for j in range(i + 1, len(arr)):
                    if max_num <= arr[j]:
                        max_num = arr[j]

            arr[i] = max_num
            max_num = 0

        return arr


        
            

                    
        