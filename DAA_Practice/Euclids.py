def Euclid(m, n):
	if n == 0:
		return m 
	r = m%n 
	m = n 
	n = r 
	return Euclid(m, n)

print(Euclid(16000,4800))