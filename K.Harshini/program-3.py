def generate_fibonacci_like_series(a):
    """
    Generate fibonacci-like series based on the pattern
    
    Args:
        a (int): Position in the sequence
        
    Returns:
        list: List of numbers for position 'a'
    """
    if a <= 0:
        return []
    
    # Pattern: positions 1,2 -> 1 element; 3,4 -> 3 elements; 5,6 -> 5 elements
    # The number of elements follows: 1, 1, 3, 3, 5, 5, 7, 7, ...
    
    if a <= 2:
        count = 1
    else:
        # For a > 2, find the appropriate count
        # Pattern: positions 3,4 have 3 elements; 5,6 have 5 elements; etc.
        count = 2 * ((a - 1) // 2) + 1
    
    # Generate first 'count' odd numbers
    result = []
    current_odd = 1
    
    for i in range(count):
        result.append(current_odd)
        current_odd += 2
    
    return result

def main():
    """Test the fibonacci-like series generation"""
    print("Problem-3: Fibonacci-like Series")
    print("-" * 38)
    
    # Test cases from the problem
    test_cases = [1, 2, 3, 4, 5, 6, 7, 8]
    
    for a in test_cases:
        result = generate_fibonacci_like_series(a)
        result_str = ", ".join(map(str, result))
        print(f"input a = {a}, output: {result_str}")
    
    # Interactive input
    print("\n" + "-" * 38)
    try:
        user_input = int(input("Enter a number: "))
        result = generate_fibonacci_like_series(user_input)
        result_str = ", ".join(map(str, result))
        print(f"input a = {user_input}, output: {result_str}")
    except ValueError:
        print("Please enter a valid integer")

if __name__ == "__main__":
    main()