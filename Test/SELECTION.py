def sort(nums):

    for i in range(5):
        minpos = i
        for j in range(i,6):
            if nums[j] < nums[minpos]:
               minpos = j

        temp = nums[i] #prej qituhit
        nums[i] = nums[minpos]         #PYETJE
        nums[minpos] = temp #Deri qitu
        print(nums)

nums = [8,6,5,3,1,2]
sort(nums)

print(nums)