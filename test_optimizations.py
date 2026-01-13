"""
Unit tests to verify that optimized versions produce the same results as slow versions.
This ensures correctness while improving performance.
"""

import unittest
import tempfile
import os
import random

import slow_code_examples as slow
import optimized_code as fast


class TestOptimizationCorrectness(unittest.TestCase):
    """Test that optimized code produces same results as slow code."""
    
    def test_string_concat(self):
        """Test string concatenation produces same result."""
        n = 100
        slow_result = slow.inefficient_string_concat(n)
        fast_result = fast.optimized_string_concat(n)
        self.assertEqual(slow_result, fast_result)
    
    def test_membership_check(self):
        """Test membership check finds same items."""
        items = list(range(100))
        search_items = [10, 20, 30, 150, 200]
        
        slow_result = slow.inefficient_membership_check(items, search_items)
        fast_result = fast.optimized_membership_check(items, search_items)
        
        self.assertEqual(sorted(slow_result), sorted(fast_result))
    
    def test_loop_condition(self):
        """Test loop condition optimization produces same result."""
        data = [1, 2, 3, 4, 5]
        
        slow_result = slow.inefficient_loop_condition(data)
        fast_result = fast.optimized_loop_condition(data)
        
        self.assertEqual(slow_result, fast_result)
    
    def test_list_processing(self):
        """Test list processing produces same sum."""
        n = 1000
        
        slow_result = slow.inefficient_list_processing(n)
        fast_result = fast.optimized_list_processing(n)
        
        self.assertEqual(slow_result, fast_result)
    
    def test_pair_finding(self):
        """Test pair finding finds same pairs."""
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target_sum = 10
        
        slow_result = slow.inefficient_pair_finding(numbers, target_sum)
        fast_result = fast.optimized_pair_finding(numbers, target_sum)
        
        # Convert to sets of tuples for comparison (order might differ)
        slow_set = set(slow_result)
        fast_set = set(fast_result)
        
        self.assertEqual(slow_set, fast_set)
    
    def test_file_reading(self):
        """Test file reading counts same occurrences."""
        # Create temp file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            temp_file = f.name
            f.write("test line with data\n")
            f.write("another line with keywords\n")
            f.write("test data keywords all together\n")
        
        try:
            search_terms = ["test", "data", "keywords"]
            
            slow_result = slow.inefficient_file_reading(temp_file, search_terms)
            fast_result = fast.optimized_file_reading(temp_file, search_terms)
            
            self.assertEqual(slow_result, fast_result)
        finally:
            os.unlink(temp_file)
    
    def test_max_finding(self):
        """Test max finding returns same max value."""
        numbers = [5, 2, 8, 1, 9, 3]
        
        slow_result = slow.inefficient_max_finding(numbers)
        fast_result = fast.optimized_max_finding(numbers)
        
        self.assertEqual(slow_result, fast_result)
    
    def test_max_finding_empty(self):
        """Test max finding handles empty list."""
        numbers = []
        
        slow_result = slow.inefficient_max_finding(numbers)
        fast_result = fast.optimized_max_finding(numbers)
        
        self.assertEqual(slow_result, fast_result)
    
    def test_dict_operations(self):
        """Test dictionary operations count same items."""
        items = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
        
        slow_result = slow.inefficient_dict_operations(items)
        fast_result = fast.optimized_dict_operations(items)
        
        self.assertEqual(slow_result, fast_result)
    
    def test_dict_operations_v2(self):
        """Test alternative dict operations implementation."""
        items = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
        
        slow_result = slow.inefficient_dict_operations(items)
        fast_result = fast.optimized_dict_operations_v2(items)
        
        self.assertEqual(slow_result, fast_result)
    
    def test_deep_copy(self):
        """Test deep copy avoidance produces same results."""
        data = [1, 2, 3, 4, 5]
        
        slow_result = slow.inefficient_deep_copy(data)
        fast_result = fast.optimized_deep_copy(data)
        
        self.assertEqual(slow_result, fast_result)
    
    def test_list_creation(self):
        """Test list creation produces same list."""
        n = 100
        
        slow_result = slow.inefficient_list_creation(n)
        fast_result = fast.optimized_list_creation(n)
        
        self.assertEqual(slow_result, fast_result)
    
    def test_sorting(self):
        """Test sorting optimization produces same results."""
        data = [5, 2, 8, 1, 9, 3, 7, 4, 6, 10]
        
        slow_result = slow.inefficient_sorting(data)
        fast_result = fast.optimized_sorting(data)
        
        self.assertEqual(slow_result, fast_result)
    
    def test_global_lookup(self):
        """Test global lookup optimization produces same result."""
        n = 1000
        
        slow_result = slow.inefficient_global_lookup(n)
        fast_result = fast.optimized_global_lookup(n)
        
        self.assertEqual(slow_result, fast_result)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases for optimizations."""
    
    def test_empty_inputs(self):
        """Test functions handle empty inputs."""
        self.assertEqual(fast.optimized_string_concat(0), "")
        self.assertEqual(fast.optimized_membership_check([], []), [])
        self.assertEqual(fast.optimized_loop_condition([]), [])
        self.assertEqual(fast.optimized_max_finding([]), None)
        self.assertEqual(fast.optimized_dict_operations([]), {})
    
    def test_single_element(self):
        """Test functions handle single element."""
        self.assertEqual(fast.optimized_max_finding([42]), 42)
        self.assertEqual(fast.optimized_dict_operations(['x']), {'x': 1})
        self.assertEqual(fast.optimized_loop_condition([1]), [])
    
    def test_large_inputs(self):
        """Test functions handle large inputs without crashing."""
        # These should complete without error
        result = fast.optimized_string_concat(1000)
        self.assertIsInstance(result, str)
        
        result = fast.optimized_list_processing(10000)
        self.assertIsInstance(result, int)
        
        result = fast.optimized_list_creation(10000)
        self.assertIsInstance(result, list)


class TestPerformanceImprovement(unittest.TestCase):
    """Test that optimized versions are actually faster."""
    
    def test_string_concat_faster(self):
        """Verify optimized string concat is faster."""
        import time
        
        n = 5000
        
        start = time.time()
        slow.inefficient_string_concat(n)
        slow_time = time.time() - start
        
        start = time.time()
        fast.optimized_string_concat(n)
        fast_time = time.time() - start
        
        # Optimized version should be significantly faster
        self.assertLess(fast_time, slow_time,
                       "Optimized version should be faster than slow version")
    
    def test_membership_check_faster(self):
        """Verify optimized membership check is faster."""
        import time
        
        items = list(range(5000))
        search_items = random.sample(range(7000), 500)
        
        start = time.time()
        slow.inefficient_membership_check(items, search_items)
        slow_time = time.time() - start
        
        start = time.time()
        fast.optimized_membership_check(items, search_items)
        fast_time = time.time() - start
        
        self.assertLess(fast_time, slow_time,
                       "Optimized version should be faster than slow version")


if __name__ == '__main__':
    unittest.main(verbosity=2)
