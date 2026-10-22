T = int(input())
ans = []
for _ in range(T):
	n,t1,d1,t2,d2 = map(int,input().split())
	total1 = n*t1 + d1*n*(n-1)//2
	total2 = n*t2 + d2*n*(n-1)//2
	if(total1 < total2):
		# print("RED")
		ans.append("BLUE")
	elif(total1>total2):
		# print("RED")
		ans.append("RED")
	else:
		# print("DRAW")
		ans.append("DRAW")
for i in range(T):
	print(ans[i])