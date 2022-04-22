import matplotlib.pyplot as plt
import numpy as np

def draw_chart_time(size, values):
    x = np.array(["BFS", "DFS", "A*"])
    y = np.array([values[0], values[1], values[2]])

    plt.title(f"Board {size}x{size}")
    plt.xlabel("Time Spent (s)")
    plt.ylabel("Search Methods")

    plt.barh(x, y, height = 0.1)

    for index, value in enumerate(values):
        plt.text(value, index, '{:.4f}'.format(value))
        
    plt.show()

def draw_chart_max(size, values):
    x = np.array(["BFS", "DFS", "A*"])
    y = np.array([values[0], values[1], values[2]])

    plt.title(f"Board {size}x{size}")
    plt.xlabel("Maximum Memory (KB)")
    plt.ylabel("Search Methods")

    plt.barh(x, y, height = 0.1)

    for index, value in enumerate(values): 
        plt.text(value, index, str(value))

    plt.show()

def draw_chart_expanded(size, values):
    x = np.array(["BFS", "DFS", "A*"])
    y = np.array([values[0], values[1], values[2]])

    plt.title(f"Board {size}x{size}")
    plt.xlabel("Number of Expanded Nodes")
    plt.ylabel("Search Methods")

    plt.barh(x, y, height = 0.1)

    for index, value in enumerate(values): 
        plt.text(value, index, str(value))

    plt.show()