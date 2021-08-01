import numpy as np
import math


if __name__ == "__main__":

    input_data = np.loadtxt("board.0.1000.txt").reshape(-1, 32)
    print("board ", input_data.shape)
    print(input_data)
    input_data = np.loadtxt("piece.0.1000.txt")
    print("piece ", input_data.shape)
    print(input_data)
    input_data = np.loadtxt("move.0.1000.txt")
    print("move ", input_data.shape)
    print(input_data)

    print()

    input_data = np.loadtxt("board.1.1000.txt").reshape(-1, 32)
    print("board ", input_data.shape)
    print(input_data)
    input_data = np.loadtxt("piece.1.1000.txt")
    print("piece ", input_data.shape)
    print(input_data)
    input_data = np.loadtxt("move.1.1000.txt")
    print("move ", input_data.shape)
    print(input_data)

    print()

    input_data = np.loadtxt("board.15.1000.txt").reshape(-1, 32)
    print("board ", input_data.shape)
    print(input_data)
    input_data = np.loadtxt("piece.15.1000.txt")
    print("piece ", input_data.shape)
    print(input_data)
    input_data = np.loadtxt("move.15.1000.txt")
    print("move ", input_data.shape)
    print(input_data)

