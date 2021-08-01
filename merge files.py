from Savery import *

import math


def merge():

    # Creating a list of filenames
    filenames = ["board.16.500.txt", "board.17.1000.txt", "board.18.500.txt", "board.0.1000.txt", "board.0.55869.txt", "board.1.1000.txt", "board.15.1000.txt"]

    # Open file3 in write mode
    with open('board.1.1.txt', 'w') as outfile:
        # Iterate through list
        for names in filenames:
            # Open each file in read mode
            with open(names) as infile:
                # read the data from file1 and
                # file2 and write it in file3
                outfile.write(infile.read())

            # Add '\n' to enter data of file2
            # from next line


if __name__ == "__main__":

    input_data = np.loadtxt("board.1.1.txt").reshape(-1, 32)
    print("input_data ", input_data.shape)
    print(input_data)



    merge()

    input_data = np.loadtxt("board.1.1.txt").reshape(-1, 32)
    print("input_data ", input_data.shape)
    print(input_data)


    #
    # i =0
    # input_data = np.loadtxt("board.1.17.txt")
    # print("1 ", input_data.shape)
    # i += len(input_data)
    # input_data = np.loadtxt("board.2.100.txt")
    # print("2 ", input_data.shape)
    # i += len(input_data)
    # input_data = np.loadtxt("board.4.100.txt")
    # print("4 ", input_data.shape)
    # i += len(input_data)
    # input_data = np.loadtxt("board.5.100.txt")
    # print("5 ", input_data.shape)
    # i += len(input_data)
    # input_data = np.loadtxt("board.6.100.txt")
    # print("6 ", input_data.shape)
    # i += len(input_data)
    # input_data = np.loadtxt("board.7.200.txt")
    # print("7 ", input_data.shape)
    # i += len(input_data)
    # input_data = np.loadtxt("board.8.500.txt")
    # print("8 ", input_data.shape)
    # i += len(input_data)
    # input_data = np.loadtxt("board.9.100.txt")
    # print("9 ", input_data.shape)
    # i += len(input_data)
    # input_data = np.loadtxt("board.10.250.txt")
    # print("10 ", input_data.shape)
    # i += len(input_data)
    # input_data = np.loadtxt("board.11.250.txt")
    # print("11 ", input_data.shape)
    # i += len(input_data)
    # print("i ", i)

    # input_data = np.loadtxt("board.0.55869.txt").reshape(-1, 32)
    # print("input_data ", input_data.shape)
    # print(input_data)
    #
    # train_input = input_data.astype('float32') / 5
    # print("train_input ", train_input)
    # print("shape ", train_input.shape)
    # print()