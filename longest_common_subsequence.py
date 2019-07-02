def longest_common_subsequence(s1:str , s2: str) ->int:
	m=len(s1)
	n=len(s2)
	L=[[None]*(n+1) for i in range(m+1)]

	for i in range(m+1):
		for j in range(n+1):
			if i==0 or j==0:
				L[i][j]=0
			elif s1[i-1]==s2[j-1]:
				L[i][j]=1+L[i-1][j-1]
			else:
				L[i][j]=max(L[i-1][j],L[i][j-1])
	print (L[m][n])
	print ("subsequence")
	index=L[m][n]
	lcs=[""]*(index+1)
	lcs[index]=""
	i=m
	j=n
	
	while i>0 and j>0:
		if s1[i-1]==s2[j-1]:
			lcs[index-1]=s1[i-1]
			i-=1
			j-=1
			index-=1
			
		elif L[i-1][j]>L[i][j-1]:
			i-=1
		else:
			j-=1
	return ("".join(lcs))
			

s1="AGGTAB"
s2="GXTXAYB"
#s1="AB"
#s2="BC"
print (longest_common_subsequence(s1,s2))
