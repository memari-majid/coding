nums = [4, 3, 1]
i = 0
n = len(nums)
while i < n:
    j = nums[i]
    if j < n and nums[i] != nums[j]:
        nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
        i += 1

l = []

for i in range(len(nums)):
    if nums[i] != i:
        l.append(i)

print(l)






