def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1],nums[j]
                # temp = nums[j]
                # nums[j] = nums[j+1]
                # nums[j+1] = temp
                print(nums)


nums = [8,6,5,3,1,2]
sort(nums)
var = 2
print(str(nums) + "bla ballalv")
print(f"{nums} {var} bla bla")
