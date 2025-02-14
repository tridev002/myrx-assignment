def square_and_sorted_arr(arr):
    squared_arr = []
    for i in range(len(arr)):
        squared_arr.append(arr[i]**2)

    return sorted(squared_arr)


arr = [-12, -8, -7, -5, 2, 4, 5, 11, 15]
print(square_and_sorted_arr(arr))
