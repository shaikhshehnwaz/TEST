
#Q no 01
nums=[0,1,0,3,12]
nums.sort()

for i in nums:
	if i==0:
		n=nums.pop(i)
		nums.append(n)
print(nums)

#Q no 02
from itertools import permutations
name='abc'
n=permutations(name)
lst=[]
for i in n:
	s=''.join(i)
	lst.append(s)
print(lst)

#Q no 04

arr=[3,5,1]
arr.sort()
dif=arr[1] - arr[0]
print(dif)

for i in range(2,len(arr)):
	if arr[i] + arr[i-1] != dif:
		print(True)
	else:
		print(False)


#Q no 05

matrix=[
[1,5,9],[10,11,13],[12,13,15]
]
k=8 
result=[]
for i in range(len(matrix)):
	   result.extend(matrix[i])


result.sort()
print(result[k-1])

#Q no 03

nums=[
[1,2,3,4],
[5,1,2,3],
[9,5,1,2]
]


	



	