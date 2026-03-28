def is_invalid_id(n_str: str) -> bool:
    length = len(n_str)
    if length < 2:
        return False
    
    # Try every possible repeat length
    for period in range(1, length // 2 + 1):
        if length % period == 0:
            seq = n_str[:period]
            repeats = length // period
            if repeats >= 2 and seq * repeats == n_str:
                return True
    return False


def compute_invalid_sum(filename="data_2.txt"):
    total = 0
    
    with open(filename, "r") as f:
        content = f.read()
    
    # Parse the ranges
    for part in content.replace('\n', '').split(','):
        part = part.strip()
        if not part or '-' not in part:
            continue
        start_str, end_str = part.split('-')
        start = int(start_str)
        end = int(end_str)
        
        for num in range(start, end + 1):
            if is_invalid_id(str(num)):
                total += num
    
    return total


file_name = "data_2.txt"
result = compute_invalid_sum(file_name)
print("Password:", result)