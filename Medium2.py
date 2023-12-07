def majorityElement(nums):
    if not nums:
        return []

    # Initialize candidates and their counters
    candidate1, candidate2, count1, count2 = 0, 1, 0, 0

    # Count occurrences of candidates
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # Reset counters to count occurrences of the candidates
    count1, count2 = 0, 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    # Check if candidates appear more than ⌊ n/3 ⌋ times
    result = []
    if count1 > len(nums) // 3:
        result.append(candidate1)
    if count2 > len(nums) // 3:
        result.append(candidate2)

    return result


# Example usage:
nums1 = [int(i) for i in input('Enter numbers').split()]
print(majorityElement(nums1))  # Output: [3]
