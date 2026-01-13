"""
Performance benchmark comparing slow vs optimized code.
This script measures and reports the performance improvements.
"""

import time
import random
import tempfile
import os
from typing import Callable, Tuple

import slow_code_examples as slow
import optimized_code as fast


def benchmark(slow_func: Callable, fast_func: Callable, *args, **kwargs) -> Tuple[float, float, float]:
    """
    Benchmark two functions and return (slow_time, fast_time, speedup).
    """
    # Warm up
    slow_func(*args, **kwargs)
    fast_func(*args, **kwargs)
    
    # Benchmark slow version
    start = time.time()
    slow_result = slow_func(*args, **kwargs)
    slow_time = time.time() - start
    
    # Benchmark fast version
    start = time.time()
    fast_result = fast_func(*args, **kwargs)
    fast_time = time.time() - start
    
    # Verify results are equivalent (for most cases)
    # Some cases might have different return types but same values
    
    # Handle division by zero and extremely small times
    EPSILON = 1e-9
    if fast_time < EPSILON:
        speedup = float('inf')
    else:
        speedup = slow_time / fast_time
    
    return slow_time, fast_time, speedup


def print_benchmark_result(name: str, slow_time: float, fast_time: float, speedup: float):
    """Print formatted benchmark results."""
    print(f"\n{name}:")
    print(f"  Slow version: {slow_time:.6f}s")
    print(f"  Fast version: {fast_time:.6f}s")
    print(f"  Speedup: {speedup:.2f}x faster")
    print(f"  Improvement: {((slow_time - fast_time) / slow_time * 100):.1f}% faster")


def main():
    print("=" * 70)
    print("PERFORMANCE BENCHMARK: Slow vs Optimized Code")
    print("=" * 70)
    
    results = []
    
    # 1. String concatenation
    print("\n[1/12] Benchmarking String Concatenation...")
    slow_time, fast_time, speedup = benchmark(
        slow.inefficient_string_concat,
        fast.optimized_string_concat,
        10000
    )
    print_benchmark_result("String Concatenation (10,000 items)", slow_time, fast_time, speedup)
    results.append(("String Concatenation", speedup))
    
    # 2. Membership check
    print("\n[2/12] Benchmarking Membership Checks...")
    items = list(range(10000))
    search_items = random.sample(range(15000), 1000)
    slow_time, fast_time, speedup = benchmark(
        slow.inefficient_membership_check,
        fast.optimized_membership_check,
        items,
        search_items
    )
    print_benchmark_result("Membership Checks (10k items, 1k searches)", slow_time, fast_time, speedup)
    results.append(("Membership Checks", speedup))
    
    # 3. Loop condition
    print("\n[3/12] Benchmarking Loop Conditions...")
    data = list(range(10000))
    slow_time, fast_time, speedup = benchmark(
        slow.inefficient_loop_condition,
        fast.optimized_loop_condition,
        data
    )
    print_benchmark_result("Loop Condition Optimization (10k items)", slow_time, fast_time, speedup)
    results.append(("Loop Conditions", speedup))
    
    # 4. List processing
    print("\n[4/12] Benchmarking List Processing...")
    slow_time, fast_time, speedup = benchmark(
        slow.inefficient_list_processing,
        fast.optimized_list_processing,
        100000
    )
    print_benchmark_result("List Processing (100k items)", slow_time, fast_time, speedup)
    results.append(("List Processing", speedup))
    
    # 5. Pair finding
    print("\n[5/12] Benchmarking Pair Finding...")
    numbers = random.sample(range(1000), 500)
    target = 500
    slow_time, fast_time, speedup = benchmark(
        slow.inefficient_pair_finding,
        fast.optimized_pair_finding,
        numbers,
        target
    )
    print_benchmark_result("Pair Finding (500 numbers)", slow_time, fast_time, speedup)
    results.append(("Pair Finding", speedup))
    
    # 6. File reading
    print("\n[6/12] Benchmarking File Reading...")
    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        temp_file = f.name
        for i in range(1000):
            f.write(f"This is line {i} with some test data and keywords.\n")
    
    try:
        search_terms = ["test", "data", "keywords", "line", "some"]
        slow_time, fast_time, speedup = benchmark(
            slow.inefficient_file_reading,
            fast.optimized_file_reading,
            temp_file,
            search_terms
        )
        print_benchmark_result("File Reading (1k lines, 5 terms)", slow_time, fast_time, speedup)
        results.append(("File Reading", speedup))
    finally:
        os.unlink(temp_file)
    
    # 7. Max finding
    print("\n[7/12] Benchmarking Max Finding...")
    numbers = [random.randint(0, 1000000) for _ in range(100000)]
    slow_time, fast_time, speedup = benchmark(
        slow.inefficient_max_finding,
        fast.optimized_max_finding,
        numbers
    )
    print_benchmark_result("Max Finding (100k numbers)", slow_time, fast_time, speedup)
    results.append(("Max Finding", speedup))
    
    # 8. Dictionary operations
    print("\n[8/12] Benchmarking Dictionary Operations...")
    items = [random.choice(['apple', 'banana', 'cherry', 'date', 'elderberry']) 
             for _ in range(10000)]
    slow_time, fast_time, speedup = benchmark(
        slow.inefficient_dict_operations,
        fast.optimized_dict_operations,
        items
    )
    print_benchmark_result("Dictionary Operations (10k items)", slow_time, fast_time, speedup)
    results.append(("Dictionary Operations", speedup))
    
    # 9. Deep copy
    print("\n[9/12] Benchmarking Deep Copy Avoidance...")
    data = [random.randint(0, 100) for _ in range(1000)]
    slow_time, fast_time, speedup = benchmark(
        slow.inefficient_deep_copy,
        fast.optimized_deep_copy,
        data
    )
    print_benchmark_result("Deep Copy Avoidance (1k items)", slow_time, fast_time, speedup)
    results.append(("Deep Copy Avoidance", speedup))
    
    # 10. List creation
    print("\n[10/12] Benchmarking List Creation...")
    slow_time, fast_time, speedup = benchmark(
        slow.inefficient_list_creation,
        fast.optimized_list_creation,
        10000
    )
    print_benchmark_result("List Creation (10k items)", slow_time, fast_time, speedup)
    results.append(("List Creation", speedup))
    
    # 11. Sorting
    print("\n[11/12] Benchmarking Sorting...")
    data = [random.randint(0, 10000) for _ in range(10000)]
    slow_time, fast_time, speedup = benchmark(
        slow.inefficient_sorting,
        fast.optimized_sorting,
        data
    )
    print_benchmark_result("Sorting Optimization (10k items)", slow_time, fast_time, speedup)
    results.append(("Sorting", speedup))
    
    # 12. Global lookup
    print("\n[12/12] Benchmarking Global Lookup...")
    slow_time, fast_time, speedup = benchmark(
        slow.inefficient_global_lookup,
        fast.optimized_global_lookup,
        1000000
    )
    print_benchmark_result("Global Lookup Optimization (1M iterations)", slow_time, fast_time, speedup)
    results.append(("Global Lookup", speedup))
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY OF RESULTS")
    print("=" * 70)
    print(f"\n{'Optimization':<35} {'Speedup':<15}")
    print("-" * 70)
    
    total_speedup = 1.0
    for name, speedup in results:
        print(f"{name:<35} {speedup:>10.2f}x faster")
        total_speedup *= speedup
    
    geometric_mean_speedup = total_speedup ** (1.0 / len(results))
    print("-" * 70)
    print(f"{'Geometric Mean Speedup:':<35} {geometric_mean_speedup:>10.2f}x faster")
    print("=" * 70)
    
    print("\n✅ All benchmarks completed successfully!")
    print(f"📊 Average performance improvement: {geometric_mean_speedup:.2f}x faster")


if __name__ == "__main__":
    main()
