def getMiddle(nums, low, high)->int:
    temp = nums[low]
    while(low < high):
        while(nums[low] < temp):
            low+=1
        while(nums[high] > temp):
            high-=1
        nums[low], nums[high] = nums[high], nums[low]
    nums[low] = temp
    return low

def quickSort(nums, low, high):
    if(low < high):
        middle = getMiddle(nums, low, high)
        quickSort(nums, low, middle - 1)
        quickSort(nums, middle + 1,  high)

nums = [1,2,5,0,6,7]
quickSort(nums, 0, 5)
print("nums =",nums)