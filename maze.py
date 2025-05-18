import streamlit as st
import time

# Color settings
color_map = {
    'S': 'green',
    'G': 'red',
    '#': 'black',
    '.': 'white',
}

def draw_maze(maze, visited=set(), path=set()):
    html = "<div style='font-family: monospace;'>"

    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            pos = (i, j)
            if pos in path:
                color = 'yellow'
            elif pos in visited:
                color = 'lightblue'
            elif cell in color_map:
                color = color_map[cell]
            else:
                color = 'white'

            html += f"<span style='display: inline-block; width: 20px; height: 20px; background: {color}; border: 1px solid #ccc;'>{cell}</span>"
        html += "<br>"
    html += "</div>"
    return html

# DFS with depth limit and animation support
def dfs(maze, start, goal, max_depth, placeholder):
    stack = [(start, [start])]
    visited = set()
    found_path = None
    current_depth = 0

    while stack:
        (node, path) = stack.pop()
        visited.add(node)

        # Animate current search step
        placeholder.markdown(draw_maze(maze, visited, set(path)), unsafe_allow_html=True)
        time.sleep(0.05)

        if node == goal:
            return path, visited

        if len(path) > max_depth:
            continue

        x, y = node
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and
                maze[nx][ny] != '#' and (nx, ny) not in visited):
                stack.append(((nx, ny), path + [(nx, ny)]))

    return None, visited

# Streamlit App
def main():
    st.title("DFS Pathfinding with Animation")

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

    max_depth = st.slider("Set max DFS depth", 1, 50, 15)

    placeholder = st.empty()
    result = st.button("Run DFS")

    if result:
        path, visited = dfs(maze, start, goal, max_depth, placeholder)

        if path:
            st.success(f"Goal found at depth {len(path)}")
            # Final path animation
            for i in range(1, len(path)+1):
                placeholder.markdown(draw_maze(maze, visited, set(path[:i])), unsafe_allow_html=True)
                time.sleep(0.1)
        else:
            st.error(f"No path found within max depth of {max_depth}")
            placeholder.markdown(draw_maze(maze, visited, set()), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
