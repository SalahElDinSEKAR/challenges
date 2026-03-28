def max_joltage(bank: str) -> int:
    """Find the largest two-digit number by picking any two batteries in order"""
    length = len(bank)
    if length < 2:
        return 0
    
    max_val = 0
    for i in range(length):
        for j in range(i + 1, length):
            current = int(bank[i]) * 10 + int(bank[j])
            if current > max_val:
                max_val = current
    return max_val


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


# Main execution
file_name = "data_3.txt"
result = compute_total_joltage(file_name)
print("Total output joltage:", result)