numbers = [2, 7, 11, 15]
target = 9

def two_sum(nums: list, target: int = 9) -> list[int]:
    seen = {}
    
    for index, number in enumerate(nums):
        rem = target - number
        
        if rem in seen:
            return [seen[rem], index]
        
        seen[number] = index
        
    return []
        

result = two_sum(numbers, target)
print(result)