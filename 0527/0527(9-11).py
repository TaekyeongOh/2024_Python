nums1=[11,22,33]

nums2=nums1[:]
print(nums1==nums2)

nums2[1]=0
print(nums1==nums2)
print(nums1<nums2)
print(nums1>nums2)
