

nums = [1, 4, 2, 9, 3, 7, 5, 8, 6]

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n-1):
            if (nums[j] > nums[j+1]):
                nums[j], nums[j+1] = nums[j + 1], nums[j]


def swap(nums, index1, index2):
    temp = nums[index1]
    nums[index1] = nums[index2]
    nums[index2] = temp

print("Before sorting: ", nums)
bubble_sort(nums)
print("After sorting: ", nums)