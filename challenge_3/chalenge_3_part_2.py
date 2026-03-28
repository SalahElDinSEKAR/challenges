def max_joltage(bank: str) -> int:
    length = len(bank)
    if length < 12:
        return 0

    to_remove = length - 12
    
    stack = []
    for digit in bank:
        while stack and stack[-1] < digit and to_remove > 0:
            stack.pop()
            to_remove -= 1
        stack.append(digit)
    
    while to_remove > 0:
        stack.pop()
        to_remove -= 1
    
    result = ''.join(stack)
    return int(result) if result else 0


def compute_total_joltage(filename="data_3.txt"):
    total = 0
    try:
        with open(filename, "r") as f:
            content = f.read()
        
        for line in content.splitlines():
            bank = line.strip()
            if bank:  
                total += max_joltage(bank)
        
        return total
        
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return 0
    except Exception as e:
        print(f"Something went wrong: {e}")
        return 0


file_name = "data_3.txt"
result = compute_total_joltage(file_name)
print("Total output joltage:", result)