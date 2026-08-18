import time


def countdown_timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds

    print(f"\nTimer set to: {hours:02d}:{minutes:02d}:{seconds:02d}\n")

    while total_seconds >= 0:
        h = total_seconds // 3600
        m = (total_seconds % 3600) // 60
        s = total_seconds % 60
        print(f"{h:02d}:{m:02d}:{s:02d}")

        if total_seconds == 0:
            break

        time.sleep(1)
        total_seconds -= 1

    print("\nTime's Up!!!")

try:
    time_input = input("Enter the timer (Like This HH:MM:SS): ").strip()

    parts = time_input.split(":")

    if len(parts) == 3:
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
        countdown_timer(hours, minutes, seconds)
    else:
        print("Invalid format. Please use HH:MM:SS (Like This 00:01:30).")
except ValueError:
    print("Enter valid numbers in the HH:MM:SS format.")
