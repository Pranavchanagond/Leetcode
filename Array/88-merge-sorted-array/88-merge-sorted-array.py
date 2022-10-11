class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=j=k=0
        nums=nums1[::1]
        print(nums)
        nums1.clear()
        while i < m:
            nums1.append(nums[i])
            i+=1
            k+=1  
        while j<n:
            nums1.append(nums2[j])
            j+=1
        nums1.sort()
        
        