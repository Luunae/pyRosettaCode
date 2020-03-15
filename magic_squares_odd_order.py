from math import floor
from pprint import pprint

# Check N is odd
def check_odd():
    even = True
    while even:
        try:
            board_length = int(input("Enter an odd number above zero:"))
        except ValueError:
            continue
        if board_length > 0:
            if board_length % 2 == 1:
                even = False
    return board_length


# Define grid size
def define_size(size):
    magic_square = [[None for i in range(size)] for j in range(size)]
    return magic_square


# Find starting place
def starting_place(board_length):
    return floor(board_length / 2)


# Check/Place/Move
def move_place(board_length, magic_square, pointer):
    for i in range(board_length ** 2):
        # First Occupancy Check
        if magic_square[pointer[0]][pointer[1]] is not None:
            tmpptr = pointer
            # First In-Bounds Check (Move right)
            if pointer[1] + 1 <= board_length - 1:
                tmpptr[1] += 1
            else:
                tmpptr[1] = 0
            # Second In-Bounds Check (Move up)
            if pointer[0] - 1 >= 0:
                tmpptr[0] -= 1
            else:
                tmpptr[0] = board_length - 1
            # Second Occupancy Check
            if magic_square[tmpptr[0]][tmpptr[1]] is None:
                pointer = tmpptr
            else:
                pointer[0] += 1
        # Fill in
        magic_square[pointer[0]][pointer[1]] = i + 1
    return magic_square


# Display
def display(state):
    print("Your magic square:")
    pprint(state)


# Do the thing
def go():
    board_length = check_odd()
    magic_square = define_size(board_length)
    pointer = [0, 0]
    pointer[1] = starting_place(board_length)
    state = move_place(board_length, magic_square, pointer)
    display(state)


if __name__ == "__main__":
    go()
