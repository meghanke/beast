# Homework 2

# 1
def computePower(x, y):
    result = 1
    for _ in range(y):  
        result *= x
    return result

x = 2
y = 3
computePower(x, y)

# 2
def temperatureRange(readings):
    return (min(readings), max(readings))

readings = [15, 13, 17, 19, 20, 28, 23, 20]
temperatureRange(readings)

# 3
def isWeekend(day):
    return day in [6.7]

day = 6
print(isWeekend(day)) # output: true


# 4 
def fuel_efficiency(distance, fuel):
        if fuel == 0:
            return float('inf')
        
        efficiency = distance / fuel

        result = efficiency
        for i in range(1):
             result = efficiency
        
        return result

# example
distance = 70 #miles
fuel = 21.5 #gallons
print(fuel_efficiency(distance, fuel)) #output: 3.26


# 5
def decodeNumbers(n):
    if n < 10: 
        return n

    last_digit = n % 10  
    remaining_part = n // 10  

    
    num_digits = 0
    temp = remaining_part
    while temp > 0:
        temp //= 10
        num_digits += 1

    
    new_number = last_digit * (10 ** num_digits) + remaining_part
    return new_number

# example
n = 12345
print(decodeNumbers(n))  # Output: 51234

# 6.1

# find minimum with a for loop
def find_min_with_for_loop(nums):
    if not nums:  
        return None

    min_value = nums[0]  
    for num in nums:
        if num < min_value:
            min_value = num 
    return min_value

# find max with a for loop
def find_max_with_for_loops(nums):
    if not nums:  
        return None

    max_value = nums[0] 
    for num in nums:
        if num > max_value:
            max_value = num 
    return max_value

nums = [2024, 98, 131, 2, 3, 72]
print(find_min_with_for_loop(nums))  # output: 2
print(find_max_with_for_loops(nums))  # output: 2024

#6.2 using while loops

# find minimum with a while loop
def find_min_with_while_loop(nums):
    if not nums:
        return None

    min_value = nums[0]
    i = 1  
    while i < len(nums):
        if nums[i] < min_value:
            min_value = nums[i]  
        i += 1  
    return min_value

# find max with a while loop
def find_max_with_while_loops(nums):
    if not nums:
        return None

    max_value = nums[0]
    i = 1  
    while i < len(nums):
        if nums[i] > max_value:
            max_value = nums[i] 
        i += 1  
    return max_value

nums = [2024, 98, 131, 2, 3, 72]
print(find_min_with_while_loop(nums))  # output: 2
print(find_max_with_while_loops(nums))  # output: 2024


# 7
def vowel_and_consonant_count(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char.isalpha():  
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return (vowel_count, consonant_count)

# example
text = "UC Berkeley, founded in 1868!"
print(vowel_and_consonant_count(text))  # output: (4, 11)

# 8
def digital_root(num):
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10  # Extract last digit
        num //= 10  # Remove last digit
    return digit_sum

# example
num = 2468
print(digital_root(num))  # output: 20


