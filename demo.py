#!/usr/bin/env python3
"""
Quick demo showing the most dramatic performance improvements
"""
import time
import slow_code_examples as slow
import optimized_code as fast

print("=" * 70)
print("PERFORMANCE OPTIMIZATION DEMO")
print("=" * 70)

# Demo 1: Deep Copy Avoidance (Most dramatic improvement)
print("\n1. Deep Copy Avoidance")
print("-" * 70)
data = list(range(1000))

start = time.time()
slow_result = slow.inefficient_deep_copy(data)
slow_time = time.time() - start

start = time.time()
fast_result = fast.optimized_deep_copy(data)
fast_time = time.time() - start

print(f"Slow (with deep copy):     {slow_time*1000:.2f}ms")
print(f"Fast (no deep copy):       {fast_time*1000:.2f}ms")
print(f"Speedup:                   {slow_time/fast_time:.0f}x faster! 🚀")

# Demo 2: Membership Checks
print("\n2. Membership Checks (Set vs List)")
print("-" * 70)
items = list(range(10000))
search_items = list(range(5000, 6000))

start = time.time()
slow_result = slow.inefficient_membership_check(items, search_items)
slow_time = time.time() - start

start = time.time()
fast_result = fast.optimized_membership_check(items, search_items)
fast_time = time.time() - start

print(f"Slow (list lookup):        {slow_time*1000:.2f}ms")
print(f"Fast (set lookup):         {fast_time*1000:.2f}ms")
print(f"Speedup:                   {slow_time/fast_time:.0f}x faster! 🚀")

# Demo 3: Pair Finding
print("\n3. Pair Finding (Hash Map vs Nested Loops)")
print("-" * 70)
import random
numbers = random.sample(range(1000), 500)
target = 500

start = time.time()
slow_result = slow.inefficient_pair_finding(numbers, target)
slow_time = time.time() - start

start = time.time()
fast_result = fast.optimized_pair_finding(numbers, target)
fast_time = time.time() - start

print(f"Slow (nested loops):       {slow_time*1000:.2f}ms")
print(f"Fast (hash map):           {fast_time*1000:.2f}ms")
print(f"Speedup:                   {slow_time/fast_time:.0f}x faster! 🚀")

print("\n" + "=" * 70)
print("✅ Demo complete! See SUMMARY.md for full results.")
print("=" * 70)
