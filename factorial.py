#factorial using dp
memo=[1]*10000
def factorial_dp(n):
	if n==0 or n==1:
		memo[n]=1
		return 1
	else:
		for i in range(2,n):
			memo[i]=i*memo[i-1]
	return n*memo[n-1]
			
print (factorial_dp(9912))
