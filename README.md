🤖 Rescue Robot Path Finder using Depth-Limited Search (DLS)
📌 Overview
This is an interactive web application that simulates a rescue robot navigating a maze-like building to reach a trapped survivor. The robot uses Depth-Limited Search (DLS) — a variant of DFS — to explore the maze within a limited depth.

The app is built with Python and Streamlit.

⚙️ Features
Interactive maze input using text

Adjustable search depth limit

Visual display of the maze and found path (if any)

Color-coded cells for intuitive understanding:

🟩 S (Start)

🟥 G (Goal)

⬛ # (Wall/Obstacle)

⚪ . (Free Path)

⭐ * (Final path)

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Kainat18/dls-maze-navigator
cd dls-maze-solver

pip install streamlit pandas

streamlit run app.py

🧱 Maze Format
The maze is provided as plain text. Each line represents a row in the grid.

S: Start position (Robot)

G: Goal position (Survivor)

#: Wall (Impassable)

.: Open Path
📸 Interface Preview
![img_1.png](img_1.png)

🧑‍💻 Author
Name: Kainat Farooq Munara
