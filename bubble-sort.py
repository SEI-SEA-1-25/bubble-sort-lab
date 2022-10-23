def bubble_sort(arr):
  for i in range(len(arr) - 1):
    for j in range(len(arr) - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

nums = [5, 3, 8, 6]
bubble_sort(nums)
print(f"nums should be [3, 5, 6, 8] and is, in fact: {nums}")
