def generate_odd_series(a):
    """
    Generate the first 'a' odd numbers
    
    Args:
        a (int): Number of odd numbers to generate
        
    Returns:
        list: List of first 'a' odd numbers
    """
    if a <= 0:
        return []
    
    odd_numbers = []
    current_odd = 1
    
    for i in range(a):
        odd_numbers.append(current_odd)
        current_odd += 2  # Next odd number
    
    return odd_numbers

def main():
    """Test the odd series generation"""
    print("Problem-2: Odd Numbers Series")
    print("-" * 35)
    
    # Test cases
    test_cases = [1, 2, 3, 4, 5, 6]
    
    for a in test_cases:
        result = generate_odd_series(a)
        result_str = ", ".join(map(str, result))
        print(f"input a = {a}, output: {result_str}")
    
    # Interactive input
    print("\n" + "-" * 35)
    try:
        user_input = int(input("Enter a number: "))
        result = generate_odd_series(user_input)
        result_str = ", ".join(map(str, result))
        print(f"input a = {user_input}, output: {result_str}")
    except ValueError:
        print("Please enter a valid integer")

if __name__ == "__main__":
    main()