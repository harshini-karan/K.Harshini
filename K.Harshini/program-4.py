def count_multiples(numbers):
    """
    Count how many numbers in the list are multiples of each digit 1-9
    
    Args:
        numbers (list): List of integers
        
    Returns:
        dict: Dictionary with counts of multiples for each digit 1-9
    """
    result = {}
    
    # Initialize result dictionary for digits 1-9
    for i in range(1, 10):
        result[i] = 0
    
    # Count multiples for each number in the list
    for num in numbers:
        for divisor in range(1, 10):
            if num % divisor == 0:
                result[divisor] += 1
    
    return result

def main():
    """Test the count multiples function"""
    print("Problem-4: Count Multiples")
    print("-" * 30)
    
    # Test case from the problem
    test_input = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
    result = count_multiples(test_input)
    
    print(f"Input: {test_input}")
    print(f"Output: {result}")
    
    # Detailed breakdown
    print("\nDetailed breakdown:")
    print("-" * 20)
    for divisor in range(1, 9):
        multiples = [num for num in test_input if num % divisor == 0]
        print(f"Multiples of {divisor}: {multiples} (count: {result[divisor]})")
    
    # Additional test cases
    print("\n" + "=" * 50)
    print("Additional Test Cases:")
    print("=" * 50)
    
    additional_tests = [
        [10, 20, 30, 40, 50],
        [3, 6, 9, 12, 15, 18],
        [7, 14, 21, 28, 35]
    ]
    
    for i, test_list in enumerate(additional_tests, 1):
        result = count_multiples(test_list)
        print(f"\nTest {i}:")
        print(f"Input: {test_list}")
        print(f"Output: {result}")

if __name__ == "__main__":
    main()