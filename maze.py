import streamlit as st
import time

# Color settings for visualization
color_map = {
    'S': 'green',   # Start
    'G': 'red',     # Goal
    '#': 'black',   # Wall
    '.': 'white',   # Open path
}

# Draw the maze with visited and final path cells highlighted
def draw_maze(maze, visited=set(), path=set()):
    html = "<div style='font-family: monospace;'>"
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            pos = (i, j)
            if pos in path:
                color = 'yellow'        # Final path
            elif pos in visited:
                color = 'lightblue'     # Visited during search
            elif cell in color_map:
                color = color_map[cell]
            else:
                color = 'white'
            html += f"<span style='display: inline-block; width: 20px; height: 20px; background: {color}; border: 1px solid #ccc;'>{cell}</span>"
        html += "<br>"
    html += "</div>"
    return html

# Depth-Limited Search algorithm
def depth_limited_search(maze, start, goal, max_depth, placeholder):
    stack = [(start, [start])]
    visited = set()

    while stack:
        current_node, path = stack.pop()
        visited.add(current_node)

        # Animate step
        placeholder.markdown(draw_maze(maze, visited, set(path)), unsafe_allow_html=True)
        time.sleep(0.05)

        if current_node == goal:
            return path, visited

        if len(path) >= max_depth:
            continue

        x, y = current_node
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            next_node = (nx, ny)
            if (0 <= nx < len(maze) and 0 <= ny < len(maze[0])
                and maze[nx][ny] != '#' and next_node not in visited):
                stack.append((next_node, path + [next_node]))

    return None, visited

# Streamlit App
def main():
    st.title("RescueBot Search (DLS)")
    st.markdown("""
    **Legend**  
    🟩 Start &nbsp;&nbsp;&nbsp; 🟥 Goal &nbsp;&nbsp;&nbsp; ⬛ Wall &nbsp;&nbsp;&nbsp; ⬜ Open Path  
    🟦 Visited &nbsp;&nbsp;&nbsp; 🟨 Final Path  
    """)

    # Define a simple maze
    maze = [
        ['S', '.', '.', '#', '.', '.', '.'],
        ['.', '#', '.', '.', '.', '#', '.'],
        ['.', '#', '.', '.', '.', '.', '.'],
        ['.', '.', '#', '#', '.', '.', '.'],
        ['#', '.', '#', 'G', '.', '#', '.']
    ]

    start = goal = None
    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if val == 'S':
                start = (i, j)
            elif val == 'G':
                goal = (i, j)

    max_depth = st.slider("Set max depth for DLS", 1, 50, 15)
    placeholder = st.empty()
    run_search = st.button("Run Depth-Limited Search")

    if run_search:
        path, visited = depth_limited_search(maze, start, goal, max_depth, placeholder)

        if path:
            st.success(f"Goal found at depth {len(path)}")
            for i in range(1, len(path) + 1):
                placeholder.markdown(draw_maze(maze, visited, set(path[:i])), unsafe_allow_html=True)
                time.sleep(0.1)
        else:
            st.error(f"No path found within max depth of {max_depth}")
            placeholder.markdown(draw_maze(maze, visited, set()), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
