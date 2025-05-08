import coordinates_code
import printed
import keyboard
from random import randint

def take_input():
    global real_input
    for keyboard_input in ("w", "a", "s", "d"):
        if keyboard.is_pressed(keyboard_input):
            real_input = keyboard_input
    if "real_input" not in globals():
        real_input = 0

snake_blocks = {}
snake_blocks_backup = {}
number_of_snake_blocks = 1
current_snake_block = 0     # The snake block currently being processed

snake_blocks["snake_block1"] = coordinates_code.ObjectCoordinates()

def move_snake_blocks():
    global snake_blocks
    global snake_blocks_backup
    global current_snake_block

    for i in range(1, number_of_snake_blocks + 1):      # Creates backups for all the snake blocks
        current_snake_block += 1
        key = f"snake_block{current_snake_block}"
        if key in snake_blocks:
            snake_blocks_backup[
                f"snake_block{current_snake_block}"
            ] = snake_blocks[
                f"snake_block{current_snake_block}"
            ].copy()
        if i == number_of_snake_blocks:
            current_snake_block = 0

    for i in range(1, number_of_snake_blocks +1):       # Moves the snake head based on the latest input
        current_snake_block += 1
        if current_snake_block == 1:
            if real_input == "w":
                snake_blocks["snake_block1"].y += 1
            elif real_input == "a":
                snake_blocks["snake_block1"].x -= 1        
            elif real_input == "s":
                snake_blocks["snake_block1"].y -= 1
            elif real_input == "d":
                snake_blocks["snake_block1"].x += 1

            printed.coordinates[
                f"{snake_blocks[f"snake_block{current_snake_block}"].x}.{snake_blocks[f"snake_block{current_snake_block}"].y}"
            ] = "■"
        elif current_snake_block != 1:
            snake_blocks[
                f"snake_block{current_snake_block}"
            ] = snake_blocks_backup[
                f"snake_block{current_snake_block - 1}"
            ].copy()    
            printed.coordinates[
                f"{snake_blocks[f"snake_block{current_snake_block}"].x}.{snake_blocks[f"snake_block{current_snake_block}"].y}"
            ] = "■"
        if i == number_of_snake_blocks:
            current_snake_block = 0        

food = coordinates_code.ObjectCoordinates(
    randint(1, 9), randint(1, 7)
)
while printed.coordinates.get(      # Makes sure the food doesn't spawn inside the snake
    f"{food.x}.{food.y}", None
 ) == "■":
    food = coordinates_code.ObjectCoordinates(
    randint(1, 9), randint(1, 7)
    )

def check_food():       # Checks whether the food is eaten
    global food
    global snake_blocks
    global snake_blocks_backup
    global number_of_snake_blocks
    printed.coordinates[
        f"{food.x}.{food.y}"
    ] = "▪"
    if (
        snake_blocks["snake_block1"].x == food.x and
        snake_blocks["snake_block1"].y == food.y
    ):
        number_of_snake_blocks += 1
        snake_blocks[
            f"snake_block{number_of_snake_blocks}"
        ] = snake_blocks_backup[
            f"snake_block{number_of_snake_blocks - 1}"
        ].copy()
        printed.coordinates[
            f"{food.x}.{food.y}"
        ] = "■"
        food = coordinates_code.ObjectCoordinates(
            randint(1, 9), randint(1, 7)
        )
        while printed.coordinates.get(
            f"{food.x}.{food.y}", None
         ) == "■":
            food = coordinates_code.ObjectCoordinates(
            randint(1, 9), randint(1, 7)
            )
        printed.coordinates[
            f"{food.x}.{food.y}"
        ] = "▪"

def check_collision():
    for i in range(2, number_of_snake_blocks + 1):
        if snake_blocks[
            "snake_block1"
        ].x == snake_blocks[
            f"snake_block{i}"
        ].x and snake_blocks[
            "snake_block1"
        ].y == snake_blocks[
            f"snake_block{i}"
        ].y:
            print("YOU COLLIDED WITH YOURSELF\nGAME OVER!")
            exit()

def check_borders():
    if snake_blocks[
        "snake_block1"
    ].x not in range(1, 10) or snake_blocks[
        "snake_block1"
    ].y not in range(1, 8):
        print("OUT OF BOUNDS\nGAME OVER!")
        exit()
    