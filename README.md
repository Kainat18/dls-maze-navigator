🧠 Maze Solver using Depth-Limited Search (DLS)
A visual maze pathfinding application built with Streamlit using the Depth-Limited Search (DLS) algorithm.

📌 Project Overview
This project simulates a robot navigating through a grid-based maze to reach a target destination using Depth-Limited Search. It visually demonstrates how search algorithms work by animating the robot's path, visited nodes, and the decision process. It represents real-world scenarios like robotic pathfinding, AI navigation, and search space pruning.

🛠️ Tools & Technologies
Python

Streamlit – for interactive UI and animation

HTML/CSS (inline) – for grid visualization

Depth-Limited Search (DLS) algorithm

🔍 What is Depth-Limited Search?
A variation of Depth-First Search (DFS)

Restricts the search to a predefined maximum depth

Avoids infinite loops in cyclic or infinite graphs

Suitable for bounded search spaces where depth limits are known

🎮 How It Works
A grid maze is generated using a 2D array

'S' = Start, 'G' = Goal, '#' = Wall, '.' = Free path

DLS searches for a path from Start to Goal without exceeding the depth limit

The maze is animated in real-time using color-coded cells:

🟩 Start

🟥 Goal

🟦 Visited

🟨 Final Path

⬛ Wall

🚀 Getting Started

pip install streamlit
streamlit run maze_dls.py
Adjust the maximum search depth using the slider and press "Run DLS" to visualize the algorithm.

📂 Real-World Applications
Robot path planning

Game AI (e.g. NPC movement in bounded environments)

Search-limited AI systems

Autonomous vehicle navigation


