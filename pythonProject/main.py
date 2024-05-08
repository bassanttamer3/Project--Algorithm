import DataBase

db = DataBase.Student()
print("Quick Sort:")
sorted_data_quick = Student.quick_sort(data.copy())
for item in sorted_data_quick:
    print(item.id, item.name)

print("\nMerge Sort:")
sorted_data_merge = Student.merge_sort(data.copy())
for item in sorted_data_merge:
    print(item.id, item.name)

print("\nBubble Sort:")
sorted_data_bubble = Student.bubble_sort(data.copy())
for item in sorted_data_bubble:
    print(item.id, item.name)


