num = int(input())
nums = [0, 1, 1, 1, 2, 2]

for a in range (6,101):
    pattern = (nums[a-1]) + (nums[a-5])
    nums.append(pattern)

# print(nums)
for _ in range(num):
    j = int(input())
    print(nums[j])