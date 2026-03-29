def count_accessible_rolls(filename="data_4.txt"):
    with open(filename, "r") as f:
        grid = []
        for line in f:
            cleaned = line.strip()
            if cleaned:
                grid.append(cleaned)
    
    if not grid:
        print("Error: Grid is empty!")
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    directions = [
        (-1,-1), (-1,0), (-1,1),
        (0,-1),          (0,1),
        (1,-1),  (1,0),  (1,1)
    ]
    
    accessible = 0
    
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
                    accessible += 1
    
    return accessible


file_name = "data_4.txt"
result = count_accessible_rolls(file_name)
print("Number of accessible paper rolls:", result)