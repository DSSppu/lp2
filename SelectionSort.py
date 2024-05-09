#selection sort

nums = [12,55,6,20,77,4,21]

def selectionsort(arr):
    n=len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j]< arr[min_index]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
    print("After Search:",arr)
print("Before search:", nums)


selectionsort(nums)