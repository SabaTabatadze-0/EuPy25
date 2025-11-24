# bubble sort

 arr = [1, 2, 3, 4, 5, 6]

 i = 0
 while i < len(arr):
  j = i + 1
  while j < len(arr):
        if arr[i] < arr[j]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
        j += 1
     i += 1

print(arr)
