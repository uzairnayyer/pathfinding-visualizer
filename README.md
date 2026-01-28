# Pathfinding Visualizer (BFS & DFS) – DSA Semester Project

An interactive **Pathfinding Visualizer** built as a **Data Structures & Algorithms (DSA) semester project**.

This web app lets you:

- Draw a grid with **walls/obstacles**
- Place a **Start** and **End** node
- Choose between **BFS (Breadth-First Search)** and **DFS (Depth-First Search)**
- Visualize how the algorithm explores the grid and which path it finds (if any)

Backend is implemented in **pure Python (Flask)** with a strong focus on **DSA logic**, and the frontend uses only **HTML, CSS, and vanilla JavaScript** (no frameworks).

---

## Project Context

This is my **semester project for Data Structures and Algorithms (DSA)**.

Goals:

- Implement **BFS and DFS** from scratch on a 2D grid (graph).
- Use:
  - A **queue** for BFS
  - A **stack** for DFS
- Visualize:
  - Order of **visited nodes**
  - The **final path** from Start to End

---

## Features

- **Interactive grid**
  - Click to place:
    - Start node (S)
    - End node (E)
    - Walls (obstacles)
  - Click-and-drag to draw or erase walls

- **Algorithms implemented**
  - **BFS (Breadth-First Search)**
    - Uses a **queue**
    - Guarantees the **shortest path** (in number of steps) in an unweighted grid
  - **DFS (Depth-First Search)**
    - Uses a **stack**
    - Explores deep paths first
    - Does **not guarantee** the shortest path

- **Visualization**
  - Colored animation for:
    - **Visited nodes**
    - **Final path**
  - Adjustable **speed** slider

- **Extra utilities**
  - Generate a simple **random maze** (random walls)
  - Reset the entire grid
  - Clear just the path visualization

- **Tech stack**
  - Backend: **Python 3**, **Flask**
  - Frontend: **HTML**, **CSS (CSS Grid)**, **vanilla JavaScript**
  - No frontend frameworks, no AI/ML libraries

---

## Algorithms Overview

### Breadth-First Search (BFS)

- Treats the grid as a **graph**:
  - Each cell = node
  - Edges between adjacent (up/down/left/right) cells
- Uses a **queue**:
  - FIFO: First In, First Out
- Explores the grid **level by level**
- In an **unweighted grid**, BFS:
  - **Always finds the shortest path** (minimum steps) if one exists

### Depth-First Search (DFS)

- Also treats the grid as a **graph**
- Uses a **stack** or recursion:
  - LIFO: Last In, First Out
- Explores **deep** into one path before backtracking
- May find a path, but:
  - Does **not guarantee** the shortest path
- Good for understanding how deep search behaves visually

---

⚙️ Installation & Running Locally

Clone the repository
```bash

git clone https://github.com/uzairnayyer/pathfinding-visualizer.git
cd pathfinding-visualizer
```

Create and activate a virtual environment (optional, but recommended)
# On macOS / Linux
```bash
python -m venv venv
source venv/bin/activate
```

# On Windows
```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies
```bash
pip install -r requirements.txt
```

Run the Flask app
```
python app.py
```
By default, the app runs at:

http://127.0.0.1:5000
or
http://localhost:5000

## Project Structure

```text
pathfinder/
├── app.py              
├── templates/
│   └── index.html        
└── static/
    └── style.css        
```

