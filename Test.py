
# #Q no 01
# def added(nums,target):
# 	for i in range(len(nums)):
# 		for j in range(i+1,len(nums)):
# 			if nums[i] + nums[j] == target:
# 				return [i,j]
# nums=[2,7,11,15]
# target=9
# print(added(nums,target))


# #Q no 02
# def valid(s):
# 	while "()" in s or "[]" in s or "{}" in s:
# 		s=s.replace("()","").replace("[]","").replace("{}","")
# 	return s ==""
# s="("
# print(valid(s))


# #Q no 03

# def compare(a,b):
# 	Alice_score= sum(1 for x,y in zip(a,b) if x > y)
# 	Boob_score= sum(1 for x,y in zip(a,b) if x < y)
# 	return [Alice_score,Boob_score]

# a=[17,28,30]
# b=[99,16,8]
# print(compare(a,b))



# #Q no 04
# name="AB"
# result=0
# for i in name:
# 	result=result*26 + (ord(i) - ord("A")+1)
# print(result)


def total(nums):
    count = 0
    for i in range(len(nums)):
        even_count = 0
        odd_count = 0
        for j in range(i, len(nums)):
            if nums[j] % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
            
            if even_count == odd_count:
                count += 1
    
    return count

nums = [2, 2, 1, 1, 2, 1]
print(total(nums)) 