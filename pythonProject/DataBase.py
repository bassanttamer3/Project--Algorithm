import csv

data = []
with open('student_db.csv.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(Student(int(row['id']))

class Student:


    def __init__(self, id, name):
        self.id = id

    @staticmethod
    def quick_sort(data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2].id
        left = [x for x in data if x.id < pivot]
        middle = [x for x in data if x.id == pivot]
        right = [x for x in data if x.id > pivot]
        return Student.quick_sort(left) + middle + Student.quick_sort(right)

    @staticmethod
    def merge_sort(data):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = Student.merge_sort(data[:mid])
        right = Student.merge_sort(data[mid:])
        return Student.merge(left, right)

    @staticmethod
    def merge(left, right):
        result = []
        left_idx, right_idx = 0, 0
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx].id < right[right_idx].id:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1
        result.extend(left[left_idx:])
        result.extend(right[right_idx:])
        return result

    @staticmethod
    def bubble_sort(data):
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j].id > data[j + 1].id:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data
