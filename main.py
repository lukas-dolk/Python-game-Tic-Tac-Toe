
def user_input(matrix):
    acceptable_numbers = ["1", "2", "3"]
    while True:
        try:
            coordinates = input(" ").split()
            map(int, coordinates)
        except TypeError:
            print("You should enter numbers!")
            continue
        if coordinates[0] not in acceptable_numbers or coordinates[1] not in acceptable_numbers:
            print("Coordinates should be from 1 to 3!")
            continue
        coordinates = [int(x) for x in coordinates]
        if matrix[coordinates[0] - 1][coordinates[1] - 1] != "_":
            print("This cell is occupied! Choose another one!")
            continue
        return coordinates


def tic_tac_toe_logic(matrix):
    x = False
    o = False

    # check rows
    for i in range(3):
        if matrix[i][0] == "X" \
                and matrix[i][1] == "X" \
                and matrix[i][2] == "X":
            x = True
        if matrix[i][0] == "O" \
                and matrix[i][1] == "O" \
                and matrix[i][2] == "O":
            o = True

    # check columns
    for i in range(3):
        if matrix[0][i] == "X" \
                and matrix[1][i] == "X" \
                and matrix[2][i] == "X":
            x = True
        if matrix[0][i] == "O" \
                and matrix[1][i] == "O" \
                and matrix[2][i] == "O":
            o = True

    # check diagonals
    if matrix[0][0] == "X" \
            and matrix[1][1] == "X" \
            and matrix[2][2] == "X" \
            or matrix[0][2] == "X" \
            and matrix[1][1] == "X" \
            and matrix[2][0] == "X":
        x = True
    if matrix[0][0] == "O" \
            and matrix[1][1] == "O" \
            and matrix[2][2] == "O" \
            or matrix[0][2] == "O" \
            and matrix[1][1] == "O" \
            and matrix[2][0] == "O":
        o = True

    # check variables
    if x:
        return "X wins"
    if o:
        return "O wins"
    if "_" not in matrix[0] and "_" not in matrix[1] and "_" not in matrix[2]:
        return "Draw"
    return None


def board_printer(matrix):
    print("---------")
    for i in range(3):
        print(f"| {matrix[i][0]} {matrix[i][1]} {matrix[i][2]} |")
    print("---------")


def matrix_maker(game_grid_string):
    matrix = []
    for i in range(0, 9, 3):
        matrix.append([game_grid_string[i], game_grid_string[i + 1], game_grid_string[i + 2]])
    return matrix


def main():
    game_grid_string = "_" * 9
    matrix = matrix_maker(game_grid_string)
    board_printer(matrix)
    counter = 0

    while True:

        if counter % 2 == 0:
            coordinates_choice = user_input(matrix)
            matrix[int(coordinates_choice[0] - 1)][int(coordinates_choice[1] - 1)] = "X"
            board_printer(matrix)
            counter += 1
        else:
            coordinates_choice = user_input(matrix)
            matrix[int(coordinates_choice[0] - 1)][int(coordinates_choice[1] - 1)] = "O"
            board_printer(matrix)
            counter += 1

        if tic_tac_toe_logic(matrix) is not None:
            print(tic_tac_toe_logic(matrix))
            break


main()
