
def eval():
    t = int(input())

    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        total_sum = 0
        current_max = nums[0]
        current_sign = 1 if nums[0] > 0 else -1

        for i in range(1, n):
            sign = 1 if nums[i] > 0 else -1

            if sign == current_sign:
                current_max = max(current_max, nums[i])
            else:
                total_sum += current_max
                current_max = nums[i]
                current_sign = sign
        
        total_sum += current_max  
        print(total_sum)

ans= eval()
