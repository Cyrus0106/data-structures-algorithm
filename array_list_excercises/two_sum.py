def two_sums(array,target):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] == array[j]:
                continue
            elif array[i]+array[j] == target:
                return [i,j]
            

print(two_sums([0,1,2,3,4,5,6],6))

def two_sum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
 
nums = [2, 7, 11, 15]
target = 9
indices = two_sum(nums, target)
print(f"Indices of the two numbers are: {indices}")