class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Set base cases

        nums1 = nums1[:m]

        if (len(nums1) == 0):
            return nums2

        if (len(nums2) == 0):
            return nums1

        i = 0 # nums1 counter
        j = 0 # nums2 counter

        while ((i < len(nums2)) and (j < len(nums2))):
            print("nums1: ", nums1)
            print("i: ",i)
            print("j: ",j)
            if ((nums2[j] > nums1[i]) and (nums2[j] <= nums1[i + 1])):
                nums1.insert(i+1, nums2[j])
                i += 1
                j += 1
            else:  
                i += 1

        nums1.extend(nums2[j:])
        


sol = Solution()
print(sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3))


        