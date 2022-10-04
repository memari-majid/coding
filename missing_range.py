nums = [1, 3, 50, 75]
lower, upper = 0, 99
result = []
nums = [lower-1] + nums + [upper+1]
for i in range(len(nums)-1):
    difference = nums[i+1] - nums[i]
    if difference == 2:
        result.append(str(nums[i]+1))
    if difference > 2:
        result.append(str(nums[i]+1) + '->' + str(nums[i+1]-1))
print(result)