cnt = [[0, 0], [0, 0]]  # cnt[x奇偶][y奇偶]
for x in range(2027):
    for y in range(2027):
        if x == 0 and y == 0:
            continue
        cnt[x % 2][y % 2] += 1

keys = [(0, 0), (0, 1), (1, 0), (1, 1)]
ans = 0
for i in range(4):
    for j in range(i, 4):
        a, b = keys[i]
        c, d = keys[j]
        if (a * d - b * c) % 2 == 0:
            if i == j:
                k = cnt[a][b]
                ans += k * (k - 1) // 2
            else:
                ans += cnt[a][b] * cnt[c][d]
print(ans)  # 5277593321988
