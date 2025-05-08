import movement, printed, time

while True:
    printed.coordinates.clear()
    movement.take_input()
    movement.move_snake_blocks()
    movement.check_food()
    movement.check_collision()
    movement.check_borders()
    printed.print_grid()
    time.sleep(0.5)