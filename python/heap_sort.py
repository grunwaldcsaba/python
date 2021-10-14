from heapq import heappop, heappush

def heap_sort(nums):
    heap = []
    for element in nums:
        # hozzáad egy elemet kupachoz és újrarendezi a kupacot
        heappush(heap, element)

    ordered = []

    while heap:
        # kiveszi az első vagyis legkisebb elemet a kupacból és beteszi a rendezett tömbbe
        elem = heappop(heap)
        ordered.append(elem)

    return ordered


nums = [1, 4, 2, 9, 3, 7, 5, 8, 6]
print(heap_sort(nums))