def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0

    while left <= right:
        mid = left + (right - left) // 2
        iterations += 1

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] >= target:
            right = mid - 1

    upper_bound = arr[left] if left < len(arr) else None
    return iterations, upper_bound

# Приклад використання:
sorted_array = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
target_value = 5.5

iterations, upper_bound = binary_search(sorted_array, target_value)

print(f"Кількість ітерацій: {iterations}")
print(f"Верхня межа: {upper_bound}")
