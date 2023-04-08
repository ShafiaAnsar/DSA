# nums = [1,2,3]
# sum(nums)
# for n in nums:
#     print(n)
# nums.insert(1, 100)
# nums.remove(100)
# print(100 in nums)
def find_ave(K , arr):
    result=[]
    windowSum , windowStart = 0.0 ,0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >=K-1:
            result.append(windowSum/K)
            windowSum -=arr[windowStart]
            windowStart+=1
    return result
def main():
    result = find_ave(5, [1,3,2,6,-1,4,1,8,2])
    print("Ave of subarrays of size K:" + str(result))
main()