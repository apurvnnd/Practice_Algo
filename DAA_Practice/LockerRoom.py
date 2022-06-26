def LockerRoom(n):
	l = {}
	for i in range(1,n+1):
		if i%2 == 0:
			l[i] = 0
		l[i] = 1
	count = 0
	for i in range(1,n+1):
		if i%3 == 0:
			count+=1
			if count%2 == 0:
				l[i]=1
			else:
				l[i]=0
	open = sum(l.values())
	return {'open':open,'closed':n-open}


print(LockerRoom(70000))
