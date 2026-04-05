class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        
        arr.sort()
        diffs = {}

        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i] 
            if diff not in diffs:
                diffs[diff] = [[arr[i], arr[i+1]]]
            else:
                diffs[diff].append([arr[i], arr[i+1]]) 
                
        return diffs[min(diffs.keys())]