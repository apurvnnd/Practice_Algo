def SOE(n):
	if n>2:
		l = {}
		for p in range(2,n):
			l[p] = p
		for p in range(2,round(n**(0.5))):
			if l[p]!=0:
				k = p*p
				while k<n:
					l[k] = 0 
					k = k + p 
		new_l = []
		for p in range(2,n):
			if l[p]!= 0:
				new_l.append(p)
		return new_l


print(SOE(69))