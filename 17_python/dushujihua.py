count = 0
day = 0
while(count<2026):
	day+=1
	if day%7==6 or day% 7==0:
		count += 15
	else:
		count += 5
print(day)