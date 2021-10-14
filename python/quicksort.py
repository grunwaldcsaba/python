nums = [1, 4, 2, 9, 3, 7, 5, 8, 6]


def partition(nums, start, end):
    pivot = nums[start]
    low = start + 1
    high = end

    while True:

        # addig csökkentjük a felső indexet, amíg nem találunk olyan elemet, ami kisebb, mint a kulcselem (pivot) vagy nem érjük el az alsó indexet (ami azt jelenti, h mindex elem a jó oldalán van a kulcselemnek)
        while low <= high and nums[high] >= pivot:
            high -= 1

        # az ellenkezője a másiknak
        while low <= high and nums[low] <= pivot:
            low += 1

        if low < high:
            # találtunk kisebb v. nagyobb elemet, mint a pivot
            swap(nums, low, high)
        else:
            break

    swap(nums, start, high)

    return high


def quick_sort(nums, low, high):
    
    if len(nums) <= 1:
        return nums

    if low < high:
        pivot = partition(nums, low, high)

        quick_sort(nums, low, pivot - 1)
        quick_sort(nums, pivot + 1, high)
    

def swap(nums, index1, index2):
    temp = nums[index1]
    nums[index1] = nums[index2]
    nums[index2] = temp



print("Before sorting: ", nums)
quick_sort(nums, 0, len(nums)-1)
print("After sorting: ", nums)