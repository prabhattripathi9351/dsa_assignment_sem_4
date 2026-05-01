def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        if target - num in num_map:
            return [num_map[target - num], i]
        num_map[num] = i
    return []

if __name__ == "__main__":
    print("Q1 - Two Sum Output:", twoSum([2, 7, 11, 15], 9))