def containsDuplicate(nums):
    return len(nums) != len(set(nums))

if __name__ == "__main__":
    print("Q9 - Contains Duplicate Output:", containsDuplicate([1, 2, 3, 1]))