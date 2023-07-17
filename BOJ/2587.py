# BOJ 2587번
nums = []
for i in range(5):
    num = int(input())
    nums.append(num)

nums.sort()

print(sum(nums)//5)
print(nums[2])
