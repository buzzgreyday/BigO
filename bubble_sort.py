def bubble_sort(arr, count=0):
    # Outer "for" loop
    for i in range(len(arr)):
        count+=1
        # Inner "for" loop
        for j in range(len(arr)-1):
            count+=1
            # -1 above because we go +1 below
            if arr[j] > arr[j+1]:
                # Swap them
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, count
