class Calculator:
    def __init__(self):
        """Initialize the Calculator class"""
        pass
    
    def calculate(self, a, b, operation):
        """
        Perform calculation based on the operation type
        
        Args:
            a (float): First number
            b (float): Second number  
            operation (str): Type of operation ('add', 'subtract', 'multiply', 'divide')
            
        Returns:
            float: Result of the calculation
        """
        # Convert inputs to float to ensure they're doubles
        a = float(a)
        b = float(b)
        operation = operation.lower().strip()
        
        if operation in ['add', 'addition', '+']:
            return self.add(a, b)
        elif operation in ['subtract', 'subtraction', '-']:
            return self.subtract(a, b)
        elif operation in ['multiply', 'multiplication', '*']:
            return self.multiply(a, b)
        elif operation in ['divide', 'division', '/']:
            return self.divide(a, b)
        else:
            raise ValueError(f"Unsupported operation: {operation}")
    
    def add(self, a, b):
        """Addition operation"""
        return a + b
    
    def subtract(self, a, b):
        """Subtraction operation"""
        return a - b
    
    def multiply(self, a, b):
        """Multiplication operation"""
        return a * b
    
    def divide(self, a, b):
        """Division operation"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


# Example usage and testing
def main():
    calc = Calculator()
    
    # Test cases
    print("Calculator Test Cases:")
    print("-" * 30)
    
    # Addition
    result = calc.calculate(10.5, 5.3, "add")
    print(f"10.5 + 5.3 = {result}")
    
    # Subtraction
    result = calc.calculate(15.7, 8.2, "subtract")
    print(f"15.7 - 8.2 = {result}")
    
    # Multiplication
    result = calc.calculate(4.5, 3.2, "multiply")
    print(f"4.5 * 3.2 = {result}")
    
    # Division
    result = calc.calculate(20.0, 4.0, "divide")
    print(f"20.0 / 4.0 = {result}")
    
    # Test with different operation formats
    print("\nTesting different operation formats:")
    print("-" * 40)
    result = calc.calculate(100, 25, "+")
    print(f"100 + 25 = {result}")
    
    result = calc.calculate(50, 30, "MULTIPLICATION")
    print(f"50 * 30 = {result}")
    
    # Error handling examples
    print("\nError Handling:")
    print("-" * 20)
    
    try:
        calc.calculate(10, 0, "divide")
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        calc.calculate(5, 3, "modulo")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Interactive example
    print("\nInteractive Calculator:")
    print("-" * 25)
    interactive_calculator()

def interactive_calculator():
    """Interactive calculator function for user input"""
    calc = Calculator()
    
    while True:
        try:
            print("\n--- Calculator Menu ---")
            print("Operations: add, subtract, multiply, divide")
            print("Type 'quit' to exit")
            
            # Get user input
            a = input("Enter first number (a): ")
            if a.lower() == 'quit':
                print("Goodbye!")
                break
                
            b = input("Enter second number (b): ")
            if b.lower() == 'quit':
                print("Goodbye!")
                break
                
            operation = input("Enter operation: ")
            if operation.lower() == 'quit':
                print("Goodbye!")
                break
            
            # Convert to float and calculate
            a = float(a)
            b = float(b)
            result = calc.calculate(a, b, operation)
            print(f"Result: {a} {operation} {b} = {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        # Ask if user wants to continue
        continue_calc = input("\nDo you want to perform another calculation? (y/n): ")
        if continue_calc.lower() not in ['y', 'yes']:
            print("Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main()