import pygetwindow as gw
import subprocess
import time
import pyautogui

def run_application_with_credentials():
    # Path to the executable
    exe_path = r'D:\\Work\\Cshape\\backup_fitness_local_app-master\\VS12\\FP_CLOCK\\bin\\Release\\FP_CLOCK.exe'

    # Start the application
    subprocess.Popen([exe_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    # Get a list of all window titles
    window_titles = gw.getAllTitles()
    # FP_CLOCK - Microsoft Visual Studio (Administrator)
    # Print the list of window titles
    print("Window Titles:")
    for title in window_titles:
        print(title)
        if title == 'FP_CLOCK - Microsoft Visual Studio (Administrator)' or title == '24hr-fitness.eu':
            print(title)
            window = gw.getWindowsWithTitle(title)[0]
            window.activate()

    # Wait for the application to open (adjust the time based on your application's startup time)
    time.sleep(3)

    # Simulate typing the username
    try:
        pyautogui.typewrite('XXX', interval=0.1)
    except Exception as e:
        print(f"Error: {e}")

    # Simulate a Tab key press
    pyautogui.press('tab')

    try:
        pyautogui.write("XXX", interval=0.1)
    except Exception as e:
        print(f"Error: {e}")
    

    # Simulate a Tab key press
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write("1")
    pyautogui.press('tab')
    pyautogui.write("1")
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')

    time.sleep(1)
    pyautogui.press('enter')

    time.sleep(1)

if __name__ == "__main__":
    run_application_with_credentials()
