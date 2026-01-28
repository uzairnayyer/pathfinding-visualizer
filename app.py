from flask import Flask, render_template, request, jsonify
from collections import deque

app = Flask(__name__)

class PathfindingGrid:
    def __init__(self, rows=20, cols=30):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.start = None
        self.end = None
    
    def set_start(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            if self.start:
                self.grid[self.start[0]][self.start[1]] = 0
            self.start = (row, col)
            self.grid[row][col] = 2
            return True
        return False
    
    def set_end(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            if self.end:
                self.grid[self.end[0]][self.end[1]] = 0
            self.end = (row, col)
            self.grid[row][col] = 3
            return True
        return False
    
    def set_wall(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            if (row, col) != self.start and (row, col) != self.end:
                self.grid[row][col] = 1
                return True
        return False
    
    def clear_cell(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            if self.grid[row][col] == 1:
                self.grid[row][col] = 0
                return True
        return False
    
    def get_neighbors(self, row, col):
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                if self.grid[new_row][new_col] != 1:
                    neighbors.append((new_row, new_col))
        
        return neighbors
    
    def bfs(self):
        if not self.start or not self.end:
            return None, []
        
        queue = deque()
        queue.append(self.start)
        visited = {self.start}
        parent = {self.start: None}
        visited_order = []
        
        while queue:
            current = queue.popleft()
            visited_order.append({"row": current[0], "col": current[1]})
            
            if current == self.end:
                path = self.reconstruct_path(parent)
                return path, visited_order
            
            neighbors = self.get_neighbors(current[0], current[1])
            
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)
        
        return None, visited_order
    
    def dfs(self):
        if not self.start or not self.end:
            return None, []
        
        stack = [self.start]
        visited = {self.start}
        parent = {self.start: None}
        visited_order = []
        
        while stack:
            current = stack.pop()
            visited_order.append({"row": current[0], "col": current[1]})
            
            if current == self.end:
                path = self.reconstruct_path(parent)
                return path, visited_order
            
            neighbors = self.get_neighbors(current[0], current[1])
            
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    stack.append(neighbor)
        
        return None, visited_order
    
    def reconstruct_path(self, parent):
        path = []
        current = self.end
        
        while current is not None:
            path.append({"row": current[0], "col": current[1]})
            current = parent[current]
        
        path.reverse()
        return path
    
    def solve(self, algorithm):
        if algorithm == "bfs":
            path, visited = self.bfs()
        elif algorithm == "dfs":
            path, visited = self.dfs()
        else:
            return {"error": "Invalid algorithm"}
        
        return {
            "success": path is not None,
            "path": path if path else [],
            "visited": visited,
            "path_length": len(path) if path else 0,
            "nodes_explored": len(visited),
            "algorithm": algorithm
        }
    
    def reset(self):
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.start = None
        self.end = None
    
    def get_state(self):
        return {
            "grid": self.grid,
            "rows": self.rows,
            "cols": self.cols,
            "start": {"row": self.start[0], "col": self.start[1]} if self.start else None,
            "end": {"row": self.end[0], "col": self.end[1]} if self.end else None
        }
    
    def generate_maze(self, density=0.3):
        import random
        self.reset()
        
        for row in range(self.rows):
            for col in range(self.cols):
                if random.random() < density:
                    self.grid[row][col] = 1
        
        start_row = random.randint(0, self.rows - 1)
        start_col = random.randint(0, self.cols // 4)
        self.set_start(start_row, start_col)
        
        end_row = random.randint(0, self.rows - 1)
        end_col = random.randint(3 * self.cols // 4, self.cols - 1)
        self.set_end(end_row, end_col)
        
        return self.get_state()

grid = PathfindingGrid(15, 25)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/grid', methods=['GET'])
def get_grid():
    return jsonify(grid.get_state())

@app.route('/api/cell', methods=['POST'])
def set_cell():
    data = request.get_json()
    row = data.get('row')
    col = data.get('col')
    cell_type = data.get('type')
    
    if cell_type == 'start':
        grid.set_start(row, col)
    elif cell_type == 'end':
        grid.set_end(row, col)
    elif cell_type == 'wall':
        grid.set_wall(row, col)
    elif cell_type == 'clear':
        grid.clear_cell(row, col)
    
    return jsonify({"success": True, "state": grid.get_state()})

@app.route('/api/solve', methods=['POST'])
def solve():
    data = request.get_json()
    algorithm = data.get('algorithm', 'bfs')
    result = grid.solve(algorithm)
    return jsonify(result)

@app.route('/api/reset', methods=['POST'])
def reset():
    grid.reset()
    return jsonify(grid.get_state())

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json()
    density = data.get('density', 0.3)
    state = grid.generate_maze(density)
    return jsonify(state)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
