"""
This file contains examples of slow and inefficient code patterns.
Each function demonstrates a common performance anti-pattern.
"""

import time
import random


# Issue 1: Inefficient string concatenation in a loop
def inefficient_string_concat(n=10000):
    """
    String concatenation using += in a loop is O(n^2) in Python
    because strings are immutable.
    """
    result = ""
    for i in range(n):
        result += str(i)
        if i < n - 1:
            result += ","
    return result


# Issue 2: Using list when set would be more appropriate
def inefficient_membership_check(items, search_items):
    """
    Using 'in' operator with list is O(n) for each lookup.
    With many lookups, this becomes very slow.
    """
    found = []
    for item in search_items:
        if item in items:  # O(n) lookup in list
            found.append(item)
    return found


# Issue 3: Repeated function calls in loop condition
def inefficient_loop_condition(data):
    """
    Calling len() in each iteration is wasteful.
    """
    result = []
    for i in range(len(data)):
        if i < len(data) - 1:  # len() called every iteration
            result.append(data[i] + data[i + 1])
    return result


# Issue 4: Creating unnecessary intermediate lists
def inefficient_list_processing(n=1000000):
    """
    Creating intermediate lists wastes memory and time.
    """
    # Multiple passes through data with intermediate lists
    numbers = list(range(n))
    squared = [x * x for x in numbers]
    filtered = [x for x in squared if x % 2 == 0]
    doubled = [x * 2 for x in filtered]
    return sum(doubled)


# Issue 5: Inefficient nested loops for finding pairs
def inefficient_pair_finding(numbers, target_sum):
    """
    Nested loops to find pairs is O(n^2).
    """
    pairs = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                pairs.append((numbers[i], numbers[j]))
    return pairs


# Issue 6: Reading file multiple times
def inefficient_file_reading(filename, search_terms):
    """
    Opening and reading the file multiple times is wasteful.
    """
    results = {}
    for term in search_terms:
        count = 0
        with open(filename, 'r') as f:
            for line in f:
                if term in line:
                    count += 1
        results[term] = count
    return results


# Issue 7: Not using built-in functions
def inefficient_max_finding(numbers):
    """
    Manual implementation when built-in exists.
    """
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers[1:]:  # Creates a slice copy
        if num > max_val:
            max_val = num
    return max_val


# Issue 8: Inefficient dictionary operations
def inefficient_dict_operations(items):
    """
    Repeatedly checking if key exists before assignment.
    """
    counter = {}
    for item in items:
        if item in counter:
            counter[item] = counter[item] + 1
        else:
            counter[item] = 1
    return counter


# Issue 9: Deep copying when not necessary
def inefficient_deep_copy(data):
    """
    Creating deep copies unnecessarily.
    """
    import copy
    results = []
    for i in range(len(data)):
        temp = copy.deepcopy(data)  # Expensive operation every iteration
        temp[i] = temp[i] * 2
        results.append(temp[i])
    return results


# Issue 10: Not using list comprehension
def inefficient_list_creation(n=10000):
    """
    Using append in loop instead of list comprehension.
    """
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i * i)
    return result


# Issue 11: Inefficient sorting
def inefficient_sorting(data):
    """
    Sorting multiple times instead of sorting once.
    """
    # Sort for each query - wasteful
    results = []
    for i in range(10):
        sorted_data = sorted(data)
        results.append(sorted_data[i] if i < len(sorted_data) else None)
    return results


# Issue 12: Global variable lookup in tight loop
CONSTANT_VALUE = 42

def inefficient_global_lookup(n=1000000):
    """
    Global lookups are slower than local lookups.
    """
    result = 0
    for i in range(n):
        result += CONSTANT_VALUE * i  # Global lookup each iteration
    return result


if __name__ == "__main__":
    print("Running slow code examples...")
    print("Note: These are intentionally inefficient!")
    
    # Test inefficient string concatenation
    start = time.time()
    result = inefficient_string_concat(5000)
    print(f"String concat (5000 items): {time.time() - start:.4f}s")
    
    # Test inefficient membership check
    items = list(range(10000))
    search_items = random.sample(range(15000), 1000)
    start = time.time()
    found = inefficient_membership_check(items, search_items)
    print(f"Membership check (10000 items, 1000 searches): {time.time() - start:.4f}s")
    
    # Test inefficient list processing
    start = time.time()
    result = inefficient_list_processing(100000)
    print(f"List processing (100000 items): {time.time() - start:.4f}s")
    
    # Test inefficient pair finding
    numbers = random.sample(range(1000), 500)
    start = time.time()
    pairs = inefficient_pair_finding(numbers, 500)
    print(f"Pair finding (500 numbers): {time.time() - start:.4f}s")
    
    print("\nAll slow examples completed!")
