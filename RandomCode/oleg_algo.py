n = int(input())
lst = list(map(int, input().split()))
length = len(lst)
lst = sum(lst)
ans = 0
cur = 1
for i in range(1, length):
    ans += cur
    cur *= (length - i)/i
print(int((ans + 1) * lst))
