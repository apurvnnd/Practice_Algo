#f(n) = 3*n + 1, when n is odd,
#f(n) = n/2, when n is even.
#
#Find the minimum number of steps to reach 1.
#Optimize when 1 to N is used for N>> values

class Solution:
	def minSteps(self,n:int,stored_val):
		i=0
		initial_val = n 
		while n != 1:
			if n in stored_val.keys():
				n = stored_val[n]
				i+=1
				break
			if n%2 != 0:
				n = (3*n) + 1
			else:
				n = n/2
			i+=1
		stored_val[initial_val] = 1
		return i

	def maxValN(self,N:int):
		stored_val = {}
		stored_steps = {}
		for idx in range(1,N+1):
			stored_steps[idx] = self.minSteps(idx, stored_val)
		return stored_steps

s = Solution()
print(s.maxValN(70000))