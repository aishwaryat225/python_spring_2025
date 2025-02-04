list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

# Merge two sorted lists into one
merged_list = []
i, j = 0, 0

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merged_list.append(list1[i])
        i += 1
    else:
        merged_list.append(list2[j])
        j += 1

# Add remaining elements
merged_list.extend(list1[i:])
merged_list.extend(list2[j:])

print("Merged List:", merged_list)
