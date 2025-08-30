my_list = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

# 2. Searching algorithm choice: Linear Search (because the list is unsorted)


def linear_search(arr, target):
    # Linear Search checks each element from start to end
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Search for 9 using linear search
index_found = linear_search(my_list, 9)
print(f"Linear Search: Number 9 found at index {index_found}")
# Reason: Linear search is simple and works well on unsorted lists because no prior order is needed

# 3. Insertion Sort Implementation


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements that are greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


sorted_list = insertion_sort(my_list.copy())
print("List after Insertion Sort:", sorted_list)

# 4. Searching algorithm not tried yet: Binary Search


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    # Works only on sorted lists
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


index_found_binary = binary_search(sorted_list, 9)
print(f"Binary Search: Number 9 found at index {index_found_binary}")
# Reason: Binary search is efficient for sorted lists and quickly narrows down search space
