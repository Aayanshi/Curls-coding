def binarysearch(arr,target):
    l = 0
    h = len(arr)-1
    while l<=h:
        mid = (l+h)//2
        if arr[mid] < target:
            l = mid + 1

        elif arr[mid] > target:
            h = mid + 1

        else :
            arr[mid] = target
            return mid 
    return -1        


if __name__ == "__main__":
    arr = [1, 14, 20, 30, 32, 37, 54, 56, 70, 78, 94]
    target = int(input(f"Enter your target from {arr} = "))

    vins = binarysearch(arr,target)
    print(vins)
