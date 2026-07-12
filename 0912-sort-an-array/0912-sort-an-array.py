class Solution:
    def sortArray(self, nums):

        # Base Case
        if len(nums) <= 1:
            return nums

        # Find middle
        mid = len(nums) // 2

        # Divide into two halves
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        # Merge both sorted halves
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = 0
        j = 0

        # Compare elements and add the smaller one
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Add remaining elements
        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result