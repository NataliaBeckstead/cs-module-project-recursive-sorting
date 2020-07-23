# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    left = 0
    right = len(arr)-1
    ascending_order = arr[0] < arr[right]

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if ascending_order:
            if target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target > arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

    return -1

print(agnostic_binary_search([1, 2, 3, 4, 5], 4))
print(agnostic_binary_search([5, 4, 3, 2, 1], 4))