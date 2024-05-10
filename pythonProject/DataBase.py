import pandas as pd
import time

# Defining the column names
column_names = ['id', 'name', 'nationality', 'city',
                'latitude', 'longitude', 'gender', 'ethnic.group', 'age',
                'english.grade', 'math.grade', 'sciences.grade', 'language.grade', 'portfolio.rating',
                'coverletter.rating', 'refletter.rating']


# Defining data filtering function
def data_filtering(file_location):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_location)
    return df


# Sorting algorithms
def quicksort(arr, key_func):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if key_func(x) < key_func(pivot)]
    middle = [x for x in arr if key_func(x) == key_func(pivot)]
    right = [x for x in arr if key_func(x) > key_func(pivot)]
    return quicksort(left, key_func) + middle + quicksort(right, key_func)


# def shell_sort(arr, key_func):
#     array_length = len(arr)
#     gap = array_length // 2
#     while gap > 0:
#         for i in range(gap, array_length):
#             temp = arr[i]
#             j = i
#             while j >= gap and key_func(arr[j - gap]) > key_func(temp):
#                 arr[j] = arr[j - gap]
#                 j -= gap
#             arr[j] = temp
#         gap //= 2
#     return arr


def merge(left, right, key_func):
    sorted_res = [None] * (len(left) + len(right))
    i = j = k = 0
    while i < len(left) and j < len(right):
        if key_func(left[i]) <= key_func(right[j]):
            sorted_res[k] = left[i]
            i += 1
        else:
            sorted_res[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        sorted_res[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        sorted_res[k] = right[j]
        j += 1
        k += 1

    return sorted_res


def merge_sort(data, key_func):
    if len(data) <= 1:
        return data
    mid = len(data) // 2  # Mid value
    left = merge_sort(data[:mid], key_func)
    right = merge_sort(data[mid:], key_func)
    return merge(left, right, key_func)


# Bubble sort algorithm
def bubble_sort(arr, key_func):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if key_func(arr[j]) > key_func(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# Sorting DataFrame function
# Sorting DataFrame function
def sort_dataframe(df, key_func, algorithms=('quicksort', 'shell_sort', 'merge_sort', 'bubble_sort')):
    # Convert DataFrame to list of dictionaries
    data = df.to_dict('records')

    sorted_dfs = {}  # Dictionary to store sorted DataFrames

    # Copying the original data to use in sorting algorithms
    data_copy = data.copy()

    # Apply each sorting algorithm
    for algorithm in algorithms:
        # Sorting the copied data
        if algorithm == 'quicksort':
            sorted_data = quicksort(data_copy, key_func)
        # elif algorithm == 'shell_sort':
        #     sorted_data = shell_sort(data_copy, key_func)
        elif algorithm == 'merge_sort':
            sorted_data = merge_sort(data_copy, key_func)
        else:
            sorted_data = bubble_sort(data_copy, key_func)

        # Convert sorted list of dictionaries back to DataFrame
        sorted_df = pd.DataFrame(sorted_data, columns=column_names)

        # Store sorted DataFrame in dictionary
        sorted_dfs[algorithm] = sorted_df

    return sorted_dfs


# Function to measure execution time
def timeit(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    return result, execution_time


# Main function
def main():
    # File location
    file_location = "student_db.csv"

    # Defining the key function for sorting by math.grade
    key_func_math_grade = lambda x: x['math.grade']

    # Filtering data
    df = data_filtering(file_location)

    # Sorting DataFrame using multiple algorithms
    algorithms = ('quicksort', 'shell_sort', 'merge_sort', 'bubble_sort')
    for algorithm in algorithms:
        sorted_df, execution_time = timeit(sort_dataframe, df, key_func_math_grade, (algorithm,))
        print(f"Sorted DataFrame using {algorithm}:")
        print(sorted_df)
        print(f"Time taken (milliseconds) for {algorithm}: {execution_time}")

if __name__ == "__main__":
    main()
