from win32gui import GetForegroundWindow
import psutil
import time
import json
import win32process
from datetime import date, datetime, timedelta
import smtplib

process_time= {}
timestamp = {}
output = []



# yesterday = today - timedelta(days = 1)
with open('output.txt') as f:
    text = f.read()

new_text = text.split('\n')
for line in new_text:
    entry = line.split()
    try:
        # print (entry[0] + " " + entry[1].strip('im') + " " + entry[2])
        print(entry)
    except:
        pass


try:
    while True:
        today = date.today()        
        today = today.strftime("%B %d, %Y")
        current_time = datetime.now()
        current_time = current_time.strftime("%B %d, %Y %H:%M:%S")
        current_app = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")
        timestamp[current_app] = int(time.time())
        time.sleep(1)

        if current_app not in process_time.keys():
            process_time[current_app] = 0

        print(process_time[current_app])
        print(timestamp[current_app])
            
        process_time[current_app] = process_time[current_app] + int(time.time())-timestamp[current_app]
        
        output = today, process_time
        print(output)

finally:
    with open('output.txt', 'a') as file:
        json.dump(output, file)
    print("Done!")

