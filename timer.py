import time


def countdown_timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    print(f"Timer set to: {hours:02d}:{minutes:02d}:{seconds:02d}\n")

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


countdown_timer(0, 0, 15)