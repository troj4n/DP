
arr = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60] 
arr= [0,4,12,2,10,6,9,13,3,11,7,15]
 
n = len(arr)
length=[1]*(n)
subsequence=[0]*(n)
for i in range(1,n):
    for j in range(0,i):
        if arr[j]<arr[i]:
            if length[j]+1>=length[i]:
                length[i]=length[j]+1
                subsequence[i]=j
print max(length)
print length

print subsequence
