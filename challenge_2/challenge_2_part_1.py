def is_invalid_id(n_str: str) -> bool:
    length = len(n_str)
    if length % 2 != 0:
        return False
    half = length // 2
    return n_str[:half] == n_str[half:]


def compute_invalid_sum(filename="data_2.txt"):
    total = 0
    
    with open(filename, "r") as f:
        content = f.read()
    
    for part in content.replace('\n', '').split(','):
        if not part.strip():
            continue
        start_str, end_str = part.strip().split('-')
        start = int(start_str)
        end = int(end_str)
        
        for num in range(start, end + 1):
            if is_invalid_id(str(num)):
                total += num
    
    return total


result = compute_invalid_sum()
print("Sum of all invalid product IDs:", result)