import pyautogui
import time

# Delay between each click (in seconds)
click_delay = 0.05

# Coordinates of the click position on the screen
click_x = 500
click_y = 500

# Duration of the auto clicker (in seconds)
duration = 6 * 60 * 60  # 8 hours

# Calculate the number of clicks based on the duration and delay
click_count = int(duration // click_delay)

# Pause before starting (in seconds)
initial_pause = 3

print("Auto Clicker will start in", initial_pause, "seconds...")
time.sleep(initial_pause)

print("Auto Clicker started!")

start_time = time.time()

for _ in range(click_count):
    pyautogui.click(click_x, click_y)
    time.sleep(click_delay)

    elapsed_time = time.time() - start_time
    if elapsed_time >= duration:
        break

print("Auto Clicker finished!")
