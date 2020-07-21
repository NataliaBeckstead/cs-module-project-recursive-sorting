# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    a_index, b_index = 0, 0
    for i in range(elements):
        if b_index == len(arrB):
            merged_arr[i] = arrA[a_index]
            a_index += 1
        elif a_index == len(arrA):
            merged_arr[i] = arrB[b_index]
            b_index += 1
        elif arrA[a_index] < arrB[b_index]:
            merged_arr[i] = arrA[a_index]
            a_index += 1
        else:
            merged_arr[i] = arrB[b_index]
            b_index += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    right = merge_sort(arr[mid:])
    left = merge_sort(arr[:mid])

    return merge(right, left)


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass

