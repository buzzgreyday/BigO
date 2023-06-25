# "First" is the first element to search from, "last" is the last...
# x = search value

def binary_search(arr, first, last, x, count=0):
    if last >= first:
        mid = (last + first) // 2
        if arr[mid] == x:
            return mid, count
        elif x < arr[mid]:
            # If in the lower half
            count += 1
            return binary_search(arr, first, mid-1, x, count)
        else:
            # If arr[mid] == 30 and x == 60, x > arr[mid], in the upper half
            count += 1
            return binary_search(arr, mid+1, last, x, count)
    else:
        # If we have exhausted out indexes, return a nonsensical value
        return -1, count
