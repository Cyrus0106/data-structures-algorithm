def twoSum(nums, target):
        # hash map
        seen = {}
        for index, numb in enumerate(nums):
            # find number that would add up to target
            look = target - numb
            # check if number is in hash map and return output
            if look in seen.keys():
                  return [index, seen[look]]
            else:
                  seen[numb] = index # or add the value to the hashmap
                  
                  
                  
                


num = [3,2,4]
target = 6
print(twoSum(num,target))