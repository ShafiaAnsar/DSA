def max_subarr(k,arr):
    max_Sum ,window_sum =0,0 
    window_start=0

    for window_end in range(len(arr)):
        window_sum +=arr[window_end]
        if window_end >= k-1:
            max_Sum= max(max_Sum, window_sum)
            window_sum -= arr[window_start]
            window_start +=1
    return max_Sum

def main():
    print("Max sum  of subarrays of size K:" + str(max_subarr(3, [2,1,5,1,3,2])))
    print("Max sum subarrays of size K:"+ str(max_subarr(2, [2,3,4,1,5])))
main()
