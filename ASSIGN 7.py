def product_of_array_elements(arr, n):
    if n == 0:
        return 1
    else:
        return arr[n - 1] * product_of_array_elements(arr, n - 1)

# Test cases
print(product_of_array_elements([1, 2, 3, 4, 5], 5))  # Output: 120
print(product_of_array_elements([1, 6, 3], 3))  # Output: 18
