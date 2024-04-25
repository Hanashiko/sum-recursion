def summ(arr, index):
    if index <= 0:
        return 0
    else:
        return summ(arr, index-1) + arr[index-1]
        
array = [1,2,3,4]
print(summ(array, len(array)))
