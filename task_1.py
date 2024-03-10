import timeit

# алгоритм сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# алгоритм сортування вставкою
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# зразки масивів для тестування
import random
sizes = [100, 1000, 10000]
arrays = {size: [random.randint(0, size) for _ in range(size)] for size in sizes}

# час виконання кожного алгоритму для кожного розміру масиву
times = {}

for size, arr in arrays.items():
    times[size] = {
        'Сортування злиттям': timeit.timeit('merge_sort(arr.copy())', globals=globals(), number=1),
        'Сортування вставкою': timeit.timeit('insertion_sort(arr.copy())', globals=globals(), number=1),
        'Timsort': timeit.timeit('sorted(arr.copy())', globals=globals(), number=1)
    }

print(times)