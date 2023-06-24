# "First" is the first element to search from, "last" is the last...
# x = search value

def binary_search(arr, first, last, x, count=0):
    if last >= first:
        mid = (last + first) // 2
        if arr[mid] == x:
            return mid, count
        elif x < arr[mid]:
            count += 1
