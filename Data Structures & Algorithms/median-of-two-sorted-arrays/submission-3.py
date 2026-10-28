class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total_len = len(A) + len(B)
        half = total_len // 2

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        # median is guaranteed.
        while True:
            i = (l + r) // 2 # A
            j = half - i - 2 # B

            A_left = A[i] if i >= 0 else float("-inf")
            A_right = A[i + 1] if i + 1 < len(A) else float("inf")
            B_left = B[j] if j >= 0 else float("-inf")
            B_right = B[j + 1] if j + 1 < len(B) else float("inf")

            # correct partition
            if A_left <= B_right and B_left <= A_right:
                #odd case
                if total_len % 2 != 0:
                    return min(A_right, B_right)
                # even
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1
