class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        a, b, i = m-1, n-1, m + n - 1

        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[i] = nums1[a]
                a -= 1
            else:
                nums1[i] = nums2[b]
                b -= 1

            i -= 1

