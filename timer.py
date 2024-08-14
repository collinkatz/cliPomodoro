import os
import time
import config
from plyer import notification

wait_sequence = [int(config.time_on_minutes*60), int(config.time_off_minutes*60)]

def seconds_to_timer(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f"{int(minutes):02d}:{int(seconds):02d}"


def print_7_seg_time(time_str):
    dict = {
        "0":('▓▓▓','▓ ▓','▓ ▓','▓ ▓','▓▓▓'),
        "1":('  ▓','  ▓','  ▓','  ▓','  ▓'),
        "2":('▓▓▓','  ▓','▓▓▓','▓  ','▓▓▓'),
        "3":('▓▓▓','  ▓','▓▓▓','  ▓','▓▓▓'),
        "4":('▓ ▓','▓ ▓','▓▓▓','  ▓','  ▓'),
        "5":('▓▓▓','▓  ','▓▓▓','  ▓','▓▓▓'),
        "6":('▓▓▓','▓  ','▓▓▓','▓ ▓','▓▓▓'),
        "7":('▓▓▓','  ▓','  ▓','  ▓','  ▓'),
        "8":('▓▓▓','▓ ▓','▓▓▓','▓ ▓','▓▓▓'),
        "9":('▓▓▓','▓ ▓','▓▓▓','  ▓','▓▓▓'),
        ":":('   ',' ▓ ','   ',' ▓ ','   '),
    }

    time_list = list(time_str)
    for seg in range(5):
        print(' '.join([dict.get(value)[seg] for value in time_list]))
    print("Pomodoro Timer...")
    print()


def print_time_up():
    print()
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓TIME▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓UP▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print()
    notification.notify(  
        title = "Pomodoro",  
        message = "Time is up...",  
        app_icon = None,  
        timeout = 10,  
        toast = False  
    )  

try:
    # Shrink the CLI to just fit the timer so it doesn't take up so much space
    os.system('mode con: cols=20 lines=9')

    while True:
        for wait_time in wait_sequence:
            for i in range(wait_time):
                time.sleep(1)
                print_7_seg_time(seconds_to_timer(wait_time - i))
            print_time_up()
            time.sleep(5)
except KeyboardInterrupt:
    print("Pomodoro Timer Stopped...")
