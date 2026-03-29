def count_accessible_rolls(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    directions = [
        (-1,-1), (-1,0), (-1,1),
        (0,-1),          (0,1),
        (1,-1),  (1,0),  (1,1)
    ]
    
    accessible = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                neighbor_count = 0
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                        neighbor_count += 1
                
                if neighbor_count < 4:
                    accessible.append((r, c))
    return accessible


def total_removable_rolls(filename="data_4.txt"):
    # Read the grid
    with open(filename, "r") as f:
        grid = [list(line.strip()) for line in f if line.strip()]
    
    if not grid:
        return 0
    
    total_removed = 0
    
    while True:
        to_remove = count_accessible_rolls(grid)
        
        if not to_remove:
            break  
        
        for r, c in to_remove:
            grid[r][c] = '.'
        
        total_removed += len(to_remove)
    
    return total_removed


file_name = "data_4.txt"
result = total_removable_rolls(file_name)
print("Total rolls of paper that can be removed:", result)