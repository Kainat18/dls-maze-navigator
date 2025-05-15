import streamlit as st
import pandas as pd

# ---- Maze Logic ----

def read_maze_from_text(maze_text):
    return [list(line.strip()) for line in maze_text.strip().split("\n") if line.strip()]

def find_start_goal(maze):
    start = goal = None
    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if val == 'S':
                start = (i, j)
            elif val == 'G':
                goal = (i, j)
    return start, goal

def depth_limited_search(maze, start, goal, limit):
    rows, cols = len(maze), len(maze[0])
    visited = set()

    def dfs(position, depth):
        if depth > limit:
            return None
        if position == goal:
            return [position]

        visited.add(position)
        r, c = position
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            next_pos = (nr, nc)
            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] in ['.', 'G'] and next_pos not in visited:
                    path = dfs(next_pos, depth + 1)
                    if path:
                        return [position] + path
        return None

    return dfs(start, 0)

def mark_path_on_maze(maze, path):
    for r, c in path[1:-1]:  # Skip start and goal
        maze[r][c] = '*'
    return maze

# ---- UI Logic ----

def display_maze(maze):
    df = pd.DataFrame(maze)
    cell_colors = {
        'S': 'lightgreen',
        'G': 'salmon',
        '#': 'black',
        '.': 'white',
        '*': 'gold'
    }
    styled_df = df.style.applymap(lambda val: f'background-color: {cell_colors.get(val, "white")}; color: black')
    st.write("### 🧭 Rescue Path Visualization")
    st.dataframe(styled_df, use_container_width=True)

# ---- Streamlit UI ----

st.set_page_config(page_title="Rescue Robot Path Finder", layout="wide")
st.title("🤖 Rescue Robot Navigation using Depth-Limited Search")
st.markdown("""
Simulate a rescue robot navigating through a collapsed building to reach a trapped survivor.  
The robot uses **Depth-Limited Search (DFS)** to explore the building based on limited battery/time.

- `S` = Robot Start
- `G` = Survivor (Goal)
- `#` = Collapsed debris (cannot pass)
- `.` = Safe path
- `*` = Found path
""")

default_maze = """\
S.#....
.#.#..#
.#....#
###.#.G
"""

maze_input = st.text_area("🏚️ Enter Building Layout (Maze)", default_maze, height=200)
depth_limit = st.slider("🔋 Set Exploration Limit (Depth)", min_value=1, max_value=50, value=15)

if st.button("🚀 Start Rescue"):
    try:
        maze = read_maze_from_text(maze_input)
        start, goal = find_start_goal(maze)

        if not start or not goal:
            st.error("Start ('S') or Goal ('G') not found in the maze.")
        else:
            path = depth_limited_search(maze, start, goal, depth_limit)

            if path:
                maze_with_path = mark_path_on_maze(maze, path)
                st.success("✅ Survivor reached! Path found.")
                display_maze(maze_with_path)
            else:
                st.warning("⚠️ No path found within the robot’s exploration limit.")
    except Exception as e:
        st.error(f" An error occurred: {e}")
