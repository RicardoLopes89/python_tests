import numpy as np
import matplotlib.pyplot as plt


def main(filename):
    with open(filename, 'r') as f:
        maze_clean = []

        # Removes the \n from the line in .txt file
        for line in f:
            maze_clean.append(line[:-1])

        # Converts the data into 1 column x Rows
        maze_total = np.matrix(maze_clean)
        maze_total = maze_total.T
        maze_total = np.array(maze_total, dtype=object)

        # Replaces the # and spaces with 0's and 1's
    for k in range(len(maze_total)):
        maze_total[k, 0] = maze_total[k, 0].replace("#", "0")
        maze_total[k, 0] = maze_total[k, 0].replace(" ", "1")
        maze_total[k, 0] = maze_total[k, 0].replace("s", "2")
        maze_total[k, 0] = maze_total[k, 0].replace("f", "3")

    # Generates a matrix of zeros with the dimensions required
    maze_final = np.zeros((len(maze_total), len(maze_total[0, 0])))

    # Places each character from string into a different row
    for i in range(len(maze_total)):
        maze_final[i, :] = np.array(list(map(int, maze_total[i, 0])))

    # Plotting Section
    plt.imshow(maze_final, interpolation='none')
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    main('Maze.txt')