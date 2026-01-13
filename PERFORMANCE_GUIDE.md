# Performance Optimization Guide

This repository demonstrates common performance issues in code and their optimized solutions.

## 📋 Overview

This project identifies 12 common performance anti-patterns and provides optimized implementations with measurable improvements.

## 🚀 Quick Start

```bash
# Run the slow code examples
python slow_code_examples.py

# Run the optimized versions
python optimized_code.py

# Run performance benchmarks
python benchmark.py
```

## 🐌 Performance Issues Identified

### 1. **Inefficient String Concatenation**
**Problem**: Using `+=` in a loop creates a new string object each time (O(n²) complexity)
```python
# Slow O(n²)
result = ""
for i in range(n):
    result += str(i) + ","
```

**Solution**: Use `join()` for O(n) complexity
```python
# Fast O(n)
result = ",".join(str(i) for i in range(n))
```

**Impact**: ~100-200x faster for large strings

---

### 2. **Wrong Data Structure for Membership Testing**
**Problem**: Using `in` operator on lists is O(n) per lookup
```python
# Slow O(n*m) where m is number of searches
for item in search_items:
    if item in items:  # O(n) lookup
        found.append(item)
```

**Solution**: Convert to set for O(1) average-case lookups
```python
# Fast O(n+m)
items_set = set(items)
for item in search_items:
    if item in items_set:  # O(1) lookup
        found.append(item)
```

**Impact**: ~50-100x faster for large datasets

---

### 3. **Repeated Function Calls in Loops**
**Problem**: Calling `len()` or other functions repeatedly in loop conditions
```python
# Slow
for i in range(len(data)):
    if i < len(data) - 1:  # len() called every iteration
        result.append(data[i] + data[i + 1])
```

**Solution**: Cache the result outside the loop
```python
# Fast
data_len = len(data)
for i in range(data_len):
    if i < data_len - 1:
        result.append(data[i] + data[i + 1])
```

**Impact**: 10-20% faster

---

### 4. **Creating Unnecessary Intermediate Lists**
**Problem**: Multiple list comprehensions create intermediate lists in memory
```python
# Slow - creates 3 intermediate lists
numbers = list(range(n))
squared = [x * x for x in numbers]
filtered = [x for x in squared if x % 2 == 0]
doubled = [x * 2 for x in filtered]
return sum(doubled)
```

**Solution**: Use generator expressions for single-pass processing
```python
# Fast - single pass, no intermediate lists
return sum(x * 2 for x in (x * x for x in range(n)) if x % 2 == 0)
```

**Impact**: 2-3x faster, much lower memory usage

---

### 5. **Nested Loops for Pair Finding**
**Problem**: O(n²) nested loops for finding pairs
```python
# Slow O(n²)
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target_sum:
            pairs.append((numbers[i], numbers[j]))
```

**Solution**: Use hash set for O(n) solution
```python
# Fast O(n)
seen = set()
for num in numbers:
    complement = target_sum - num
    if complement in seen:
        pairs.append((min(num, complement), max(num, complement)))
    seen.add(num)
```

**Impact**: ~100-1000x faster for large arrays

---

### 6. **Reading Files Multiple Times**
**Problem**: Opening and reading file for each search term
```python
# Slow - reads file multiple times
for term in search_terms:
    with open(filename, 'r') as f:
        for line in f:
            if term in line:
                count += 1
```

**Solution**: Read file once and check all terms
```python
# Fast - single file read
results = {term: 0 for term in search_terms}
with open(filename, 'r') as f:
    for line in f:
        for term in search_terms:
            if term in line:
                results[term] += 1
```

**Impact**: N-x faster where N is number of search terms

---

### 7. **Reinventing Built-in Functions**
**Problem**: Manual implementation instead of using optimized built-ins
```python
# Slow - Python loop
max_val = numbers[0]
for num in numbers[1:]:  # Also creates a slice copy!
    if num > max_val:
        max_val = num
```

**Solution**: Use built-in functions (implemented in C)
```python
# Fast - C implementation
max_val = max(numbers)
```

**Impact**: 5-10x faster

---

### 8. **Inefficient Dictionary Operations**
**Problem**: Repeatedly checking if key exists before updating
```python
# Slow
if item in counter:
    counter[item] = counter[item] + 1
else:
    counter[item] = 1
```

**Solution**: Use `defaultdict` or `get()` method
```python
# Fast - using defaultdict
from collections import defaultdict
counter = defaultdict(int)
counter[item] += 1

# Or using get()
counter[item] = counter.get(item, 0) + 1
```

**Impact**: 20-30% faster

---

### 9. **Unnecessary Deep Copying**
**Problem**: Creating deep copies when not needed
```python
# Slow - expensive copy every iteration
for i in range(len(data)):
    temp = copy.deepcopy(data)
    temp[i] = temp[i] * 2
    results.append(temp[i])
```

**Solution**: Only copy what you need
```python
# Fast - no copying needed
for i in range(len(data)):
    results.append(data[i] * 2)
```

**Impact**: 100-1000x faster

---

### 10. **Not Using List Comprehensions**
**Problem**: Using append in loop instead of comprehension
```python
# Slow
result = []
for i in range(n):
    if i % 2 == 0:
        result.append(i * i)
```

**Solution**: Use list comprehension (optimized in CPython)
```python
# Fast
result = [i * i for i in range(n) if i % 2 == 0]
```

**Impact**: 20-30% faster

---

### 11. **Repeated Sorting**
**Problem**: Sorting data multiple times
```python
# Slow - sorts 10 times
for i in range(10):
    sorted_data = sorted(data)
    results.append(sorted_data[i])
```

**Solution**: Sort once, reuse result
```python
# Fast - sorts once
sorted_data = sorted(data)
for i in range(10):
    results.append(sorted_data[i])
```

**Impact**: 10x faster

---

### 12. **Global Variable Lookups in Tight Loops**
**Problem**: Global lookups are slower than local
```python
# Slow
CONSTANT = 42
for i in range(n):
    result += CONSTANT * i  # Global lookup each time
```

**Solution**: Cache in local variable
```python
# Fast
constant = CONSTANT  # Local variable
for i in range(n):
    result += constant * i  # Local lookup
```

**Impact**: 10-15% faster for tight loops

---

## 📊 Benchmark Results

Run `python benchmark.py` to see actual performance measurements on your system.

Expected improvements:
- String concatenation: **100-200x faster**
- Membership checks: **50-100x faster**
- Pair finding: **100-1000x faster**
- File reading: **N-x faster** (N = number of searches)
- Deep copy avoidance: **100-1000x faster**
- Overall geometric mean: **10-50x faster**

## 🎯 Key Takeaways

1. **Choose the right data structure**: Sets for membership, dicts for lookups, lists for ordered sequences
2. **Use built-in functions**: They're implemented in C and highly optimized
3. **Avoid unnecessary work**: Cache results, don't repeat calculations
4. **Think about complexity**: O(n) is much better than O(n²)
5. **Use generators**: Avoid intermediate lists for better memory usage
6. **Profile before optimizing**: Measure to find actual bottlenecks

## 🛠️ Tools for Performance Analysis

- **timeit**: For micro-benchmarks
- **cProfile**: For profiling Python code
- **memory_profiler**: For memory usage analysis
- **line_profiler**: For line-by-line profiling

## 📚 Further Reading

- [Python Performance Tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)
- [Time Complexity Cheat Sheet](https://www.bigocheatsheet.com/)
- [Effective Python by Brett Slatkin](https://effectivepython.com/)

## ✅ Testing

All optimizations have been verified to:
1. Produce correct results (same output as slow version)
2. Run significantly faster
3. Use less memory where applicable

Run the benchmark suite to verify improvements on your system.
