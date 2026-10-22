N = int(input())
M = 2026

# cnt[r] 表示 1~N 中除以 2026 餘數為 r 的數有幾個
cnt = [N // M] * M
for r in range(1, N % M + 1):
    cnt[r] += 1

ans = 0
if cnt[0] > 0:       # 餘數 0 的最多選 1 個
    ans += 1
if cnt[1013] > 0:    # 餘數 1013 的最多選 1 個
    ans += 1
for r in range(1, 1013):           # r 和 2026-r 兩組只能選一組，選多的
    ans += max(cnt[r], cnt[M - r])
print(ans)
