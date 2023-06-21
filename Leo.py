import sys
import time

sleep_time = 3
flowers = [
    "Sunflower",
    "Whisper",
    "Meadow",
    "Cascade",
    "Serendipity",
    "Harmony",
    "Twilight",
    "Enchant",
    "Radiant",
    "Tranquil"
]

picked_flowers = []
def print_picked_flowers(additional_text = "", sleep = 0):
    print(f"{additional_text}These are the flowers that you picked:")
    picked_names = [flowers[flower_index] for flower_index in picked_flowers]
    print(*picked_names, sep=',\n')
    time.sleep(sleep)

while True:
    if len(picked_flowers) == len(flowers):
        print("Congrats, you picked all the flowers!")
        print_picked_flowers()
        print(f"It took you {round(time.perf_counter() / 1000, 1)} seconds to pick all of the flowers!")
        time.sleep(sleep_time)
        sys.exit()

    choice = input("Choose a flower! (Input 0-9) or enter 'N' to exit: ")

    if choice.lower() == 'n':
        print_picked_flowers("You stopped picking flowers. ", sleep_time)
        sys.exit()
    elif choice.isdigit():
        choice = int(choice)
        if 0 <= choice < len(flowers):
            if choice in picked_flowers:
                print("You have already picked that flower. Choose a different one.")
            else:
                picked_flowers.append(choice)
                print(f"You picked the {flowers[choice]}!")
        else:
            print("Invalid input. Please choose a digit between 0 and 10.")
    else:
        print("Invalid input. Please enter a digit or 'N'.")