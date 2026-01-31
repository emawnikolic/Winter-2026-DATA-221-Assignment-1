# Question 6 | Distribution Analysis - Define a function that receives a list of numbers and returns a dictionary where:
# • Each key is a unique value from the list.
# • Each value is the percentage of elements in the list that are less than or equal to that key.
# The resulting dictionary should be sorted by key before being returned.

def distribution_analysis(nums):
    result = {}
    n = len(nums)

    for value in set(nums):
        count = 0
        for num in nums:
            if num <= value:
                count += 1
        result[value] = (count / n) * 100

    sorted_result = dict(sorted(result.items()))
    return sorted_result

numbers = [3, 1, 2, 3, 4, 2]
print(distribution_analysis(numbers))