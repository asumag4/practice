class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        
        i = 0
        j = 1
        k = 2
        arr_len = len(arr)
        longest_peak_len = 0

        while (
            i <= (arr_len - 3) and
            j <= (arr_len - 2) and
            k <= (arr_len - 1)):

            # print(f"{arr[i]}, {arr[j]}, {arr[k]}")
            
            if (
                (arr[i]) < arr[j] and
                (arr[j]) > arr[k]
            ):
                # print("Peak found!")
                placeholder = i

                peak = []
                peak.extend([arr[i], arr[j], arr[k]])

                # Traverse Back 
                while (i >= 0):
                    if (
                        (i - 1) >= 0 and
                        arr[i-1] < arr[i]
                        ):
                        # print("Going backwards..")
                        i -= 1
                        peak.insert(0, arr[i])
                    else:
                        break
                
                # Traverse Right
                while (k <= (arr_len)):
                    if (
                        (k + 1) <= (arr_len - 1) and
                        arr[k+1] < arr[k]
                        ):
                        # print("Going forwards..")
                        k += 1
                        peak.append(arr[k])
                    else:
                        break

                # print(f"Mountain: {peak}, length of {len(peak)}")
                
                if (longest_peak_len < len(peak)):
                    longest_peak_len = len(peak)

                # Iterate
                i = placeholder + 1
                j = i + 1
                k = j + 1
                
            i += 1
            j = i + 1
            k = j + 1

        return longest_peak_len
        
sol = Solution()
print(sol.longestMountain([0,1,2,3,4,5,4,3,2,1,0])) # 11
# print(sol.longestMountain([2,1,4,7,3,2,5])) # 5
# print(sol.longestMountain([2,2,2])) # 0