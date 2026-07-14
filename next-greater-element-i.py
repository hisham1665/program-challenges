class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater = {}

        for num in nums2 :
            while stack and num > stack [-1]:
                greater[stack.pop()] = num
            stack.append(num)

        ans = []
        for num in nums1:
            ans.append(greater.get(num, -1))

        return ans
