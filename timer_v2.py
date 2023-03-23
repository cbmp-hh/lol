import time
import winsound
import datetime
import msvcrt

def clear_screen():
    print("\033c", end="")

def convert_time(time_str):
    time_obj = datetime.datetime.strptime(time_str, "%H:%M:%S")
    return time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second

def convert_seconds_to_hms(t):
    hours = t // 3600
    minutes = (t % 3600) // 60
    seconds = t % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

while True:
    mode = input("Stopwatch(1) or timer(2)? ")
    clear_screen()
    
    if mode == "1":
        input("Press enter to start")
        clear_screen()
        t = 0
        stopwatch_loop = True
        while stopwatch_loop:
            print(convert_seconds_to_hms(t))
            print("Press enter to stop the stopwatch.")
            
            if msvcrt.kbhit() and msvcrt.getch() == b"\r":
                determine_stop = input("Press enter to continue, enter 1 to clear")
                
                if determine_stop == "":
                    clear_screen()
                    continue
                
                elif determine_stop == "1":
                    clear_screen()
                    break
                
                else:
                    print("Invalid input. End in 3 seconds")
                    time.sleep(3)
                    clear_screen()
                    break
            t += 1
            time.sleep(1)
            clear_screen()
    
    elif mode == "2":
        time_str = input("Enter the time (HH:MM:SS)(23:59:59 max): ")
        time_int = convert_time(time_str)
        clear_screen()
        timer_loop = True
        while timer_loop:
            if time_int == 0:
                print("Time's up!")
                winsound.Beep(440, 5000)
                clear_screen()
                break
            print(convert_seconds_to_hms(time_int))
            print("Press enter to stop the timer.")
            
            if msvcrt.kbhit() and msvcrt.getch() == b"\r":
                determine_stop = input("Press enter to continue, enter 1 to clear")
                
                if determine_stop == "":
                    clear_screen()
                    continue
                
                elif determine_stop == "1":
                    clear_screen()
                    break
                
                else:
                    print("Invalid input. End in 3 seconds")
                    time.sleep(3)
                    break
            time_int -= 1
            time.sleep(1)
            clear_screen()
    
    else:
        clear_screen()
        print("Invalid input. Please enter 1 or 2.")