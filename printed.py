coordinates = {}
print_coordinate_x = 1    # The coordinate system starts at (1.1)
print_coordinate_y = 7    # The rows are read from bottom to top

def print_grid():
    print("\n" * 40)
    global print_coordinate_x
    global print_coordinate_y
    for i in range(1, 64):  # Goes over every 63 pixels and checks wether there is something to print
        if i % 9 == 0:
            print(
                coordinates.get(f"{print_coordinate_x}.{print_coordinate_y}", "▢")
            )
            print_coordinate_x = 1
            print_coordinate_y -= 1
        else:
            print(
                coordinates.get(f"{print_coordinate_x}.{print_coordinate_y}", "▢"), end = " "
            )
            print_coordinate_x += 1
        if i == 63:
            print_coordinate_x = 1
            print_coordinate_y = 7