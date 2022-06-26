def SOE(n):
	if n>2:
		l = {}
		for i in range(2,n):
			l[i] = i 

		for j in range(2, round(n**(0.5))):
			if l[j]!=0:
				k = j*j
				while k <= n:
					l[k]=0
					k = k + j
		new_l = []
		for m in range(2,n):
			if l[m]!=0: 
				new_l.append(m)
		return new_l

print(SOE(50))