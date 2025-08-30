def merge_sort(items):
    items_length = len(items)
    temporary_storage = [None] * items_length
    size_of_subsections = 1

    while size_of_subsections < items_length:
        for i in range(0, items_length, size_of_subsections * 2):
            first_section_start = i
            first_section_end = min(i + size_of_subsections, items_length)
            second_section_start = first_section_end
            second_section_end = min(first_section_end + size_of_subsections, items_length)

            sections = (first_section_start, first_section_end), (second_section_start, second_section_end)
            merge(items, sections, temporary_storage)

        size_of_subsections *= 2

    return items

def merge(items, sections, temporary_storage):
    (first_start, first_end), (second_start, second_end) = sections
    left_index = first_start
    right_index = second_start
    temp_index = 0

    while left_index < first_end and right_index < second_end:
        if len(items[left_index]) > len(items[right_index]):  # Descending by length
            temporary_storage[temp_index] = items[left_index]
            left_index += 1
        else:
            temporary_storage[temp_index] = items[right_index]
            right_index += 1
        temp_index += 1

    while left_index < first_end:
        temporary_storage[temp_index] = items[left_index]
        left_index += 1
        temp_index += 1

    while right_index < second_end:
        temporary_storage[temp_index] = items[right_index]
        right_index += 1
        temp_index += 1

    for i in range(temp_index):
        items[first_start + i] = temporary_storage[i]
list1 = [
    "banana", "apple", "cherry", "date", "elderberry",
    "fig", "grape", "honeydew", "jackfruit", "kiwi"
]

list2 = [
    "pineapple", "mango", "orange", "blueberry", "strawberry",
    "raspberry", "blackberry", "currant", "apple", "pear"
]

list3 = [
    "elephant", "dog", "cat", "alligator", "hippopotamus",
    "giraffe", "monkey", "bear", "zebra", "antelope"
]

sorted_list1 = merge_sort(list1)
sorted_list2 = merge_sort(list2)
sorted_list3 = merge_sort(list3)

print("Sorted list1:", sorted_list1)
print("Sorted list2:", sorted_list2)
print("Sorted list3:", sorted_list3)        