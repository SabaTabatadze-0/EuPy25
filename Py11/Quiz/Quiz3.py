def binary_search(arr, num):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            low = mid + 1
        else:
            high = mid - 1


arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]

num1 = int(input())

print(binary_search(arr1, num1))
