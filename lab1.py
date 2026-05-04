def sorted_squares_optimal(nums):
    n = len(nums)
    # Create an array of the required size, filled with zeros
    result = [0] * n 
    
    left = 0
    right = n - 1
    
    # Fill the new array from the end to the beginning
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] ** 2
            left += 1
        else:
            result[i] = nums[right] ** 2
            right -= 1
            
    return result

# Example usage:
nums = [-4, -1, 0, 3, 10]
print(sorted_squares_optimal(nums)) 
# Output: [0, 1, 9, 16, 100]