"""
This file contains optimized versions of the slow code examples.
Each function shows the improved implementation with better performance.
"""

import time
import random
from collections import defaultdict


# Fix 1: Use join() for string concatenation - O(n) instead of O(n^2)
def optimized_string_concat(n=10000):
    """
    Using join() with a list is much more efficient.
    Time complexity: O(n)
    """
    return ",".join(str(i) for i in range(n))


# Fix 2: Use set for membership checks - O(1) lookup instead of O(n)
def optimized_membership_check(items, search_items):
    """
    Convert list to set for O(1) average-case lookups.
    """
    items_set = set(items)  # O(n) conversion, done once
    found = []
    for item in search_items:
        if item in items_set:  # O(1) lookup
            found.append(item)
    return found


# Fix 3: Cache loop invariants
def optimized_loop_condition(data):
    """
    Cache the length calculation outside the loop.
    """
    result = []
    data_len = len(data)  # Calculate once
    for i in range(data_len):
        if i < data_len - 1:
            result.append(data[i] + data[i + 1])
    return result


# Fix 4: Use generator expressions to avoid intermediate lists
def optimized_list_processing(n=1000000):
    """
    Use generator expressions for memory efficiency and single pass.
    """
    # Single pass using generator - no intermediate lists
    return sum(x * 2 for x in (x * x for x in range(n)) if x % 2 == 0)


# Fix 5: Use hash map for O(n) pair finding instead of O(n^2)
def optimized_pair_finding(numbers, target_sum):
    """
    Use a set to find pairs in O(n) time.
    """
    pairs = []
    seen = set()
    for num in numbers:
        complement = target_sum - num
        if complement in seen:
            pairs.append((min(num, complement), max(num, complement)))
        seen.add(num)
    return pairs


# Fix 6: Read file only once
def optimized_file_reading(filename, search_terms):
    """
    Read the file once and count all terms in a single pass.
    """
    results = {term: 0 for term in search_terms}
    with open(filename, 'r') as f:
        for line in f:
            for term in search_terms:
                if term in line:
                    results[term] += 1
    return results


# Fix 7: Use built-in functions (they're optimized in C)
def optimized_max_finding(numbers):
    """
    Built-in max() is implemented in C and much faster.
    """
    return max(numbers) if numbers else None


# Fix 8: Use defaultdict or get() method
def optimized_dict_operations(items):
    """
    Use defaultdict to avoid repeated key checks.
    """
    counter = defaultdict(int)
    for item in items:
        counter[item] += 1
    return dict(counter)


# Alternative using get():
def optimized_dict_operations_v2(items):
    """
    Use dict.get() with default value.
    """
    counter = {}
    for item in items:
        counter[item] = counter.get(item, 0) + 1
    return counter


# Fix 9: Avoid unnecessary copying
def optimized_deep_copy(data):
    """
    Only work with what you need - avoid copying entire structures.
    """
    results = []
    for i in range(len(data)):
        results.append(data[i] * 2)
    return results


# Fix 10: Use list comprehension (faster than append loop)
def optimized_list_creation(n=10000):
    """
    List comprehensions are optimized in CPython.
    """
    return [i * i for i in range(n) if i % 2 == 0]


# Fix 11: Sort once, reuse results
def optimized_sorting(data):
    """
    Sort data once and reuse the sorted result.
    """
    sorted_data = sorted(data)
    results = []
    for i in range(10):
        results.append(sorted_data[i] if i < len(sorted_data) else None)
    return results


# Fix 12: Use local variable to cache global lookup
CONSTANT_VALUE = 42

def optimized_global_lookup(n=1000000):
    """
    Cache global variable in local scope for faster access.
    """
    result = 0
    constant = CONSTANT_VALUE  # Local lookup is faster
    for i in range(n):
        result += constant * i
    return result


if __name__ == "__main__":
    print("Running optimized code examples...")
    
    # Test optimized string concatenation
    start = time.time()
    result = optimized_string_concat(5000)
    print(f"String concat (5000 items): {time.time() - start:.4f}s")
    
    # Test optimized membership check
    items = list(range(10000))
    search_items = random.sample(range(15000), 1000)
    start = time.time()
    found = optimized_membership_check(items, search_items)
    print(f"Membership check (10000 items, 1000 searches): {time.time() - start:.4f}s")
    
    # Test optimized list processing
    start = time.time()
    result = optimized_list_processing(100000)
    print(f"List processing (100000 items): {time.time() - start:.4f}s")
    
    # Test optimized pair finding
    numbers = random.sample(range(1000), 500)
    start = time.time()
    pairs = optimized_pair_finding(numbers, 500)
    print(f"Pair finding (500 numbers): {time.time() - start:.4f}s")
    
    print("\nAll optimized examples completed!")
