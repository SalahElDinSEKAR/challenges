def compute_password_from_file(filename):
    pos = 50          
    count = 0         
    
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
                
            direction = line[0]
            value = int(line[1:])
            
            step = -1 if direction == 'L' else 1
            
            for _ in range(value):
                pos = (pos + step) % 100
                if pos == 0:
                    count += 1   
    
    return count


file_name = "data_1.txt"
result = compute_password_from_file(file_name)
print("Password:", result)