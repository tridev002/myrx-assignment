def find_min_platforms(arr, dep):
    n = len(arr)
    
    
    arr = sorted([int(t.split(":")[0]) * 60 + int(t.split(":")[1]) for t in arr])
    dep = sorted([int(t.split(":")[0]) * 60 + int(t.split(":")[1]) for t in dep])
    
    i, j = 0, 0  
    platforms_needed = 0
    max_platforms = 0

    while i < n and j < n:
        if arr[i] <= dep[j]:  
            platforms_needed += 1
            max_platforms = max(max_platforms, platforms_needed)
            i += 1
        else:  
            platforms_needed -= 1
            j += 1

    return max_platforms

arr = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
dep = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]
print(find_min_platforms(arr, dep))  

arr2 = ["9:00", "9:40"]
dep2 = ["9:10", "12:00"]
print(find_min_platforms(arr2, dep2))  
