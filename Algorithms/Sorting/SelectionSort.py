def selectSort(arr):
    for i in range(len(arr) - 1, 0, -1):
        j = i
        for k in range(i):
            if arr[j] < arr[k]:
                j = k
        arr[j], arr[i] = arr[i], arr[j]
arr = [45,2,10,0,-5]
selectSort(arr)
print(arr)