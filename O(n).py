nums = [1,2,3]
sum(nums)
for n in nums:
    print(n)
nums.insert(1, 100)
nums.remove(100)
print(100 in nums)

#heapq
import heapq
x = heapq.heapify(nums)
print(x)