T = int(input())

for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    avg = round(sum(nums) / 10)
    print(f'#{test_case} {avg}')