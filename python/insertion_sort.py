nums = [1, 4, 2, 9, 3, 7, 5, 8, 6]

def insertion_sort(nums):
    for i in range(1, len(nums)):
        currentItem = nums[i]
        maxSortedIndex = i - 1
        while maxSortedIndex >= 0 and nums[maxSortedIndex] > currentItem:
            nums[maxSortedIndex + 1] = nums[maxSortedIndex]
            maxSortedIndex -= 1
        nums[maxSortedIndex + 1] = currentItem


print("Before sorting: ", nums)
insertion_sort(nums)
print("After sorting: ", nums)
