import tkinter as tk
import winsound
import datetime
import time

def show_alarm_clock():
    
    print("Enter alarm time(in 12 hour format): %s\n AM/PM: %s Reminder message:%s\n" % (e1.get(), e2.get()),e3.get())

master = tk.Tk()
master.title("Google Alarm")
master.geometry("500x400")

#Getting the time and am/pm from user through entry
tk.Label(master, 
         text="Alarm time :").grid(row=0)
tk.Label(master, 
         text="AM/PM :").grid(row=1)
tk.Label(master, 
         text="Label:").grid(row=2)


e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
#e3 is just a label to show task for the day 
e3.grid(row=2, column=1)

#Displaying snooze and dismiss buttons

tk.Button(master, 
          text='SNOOZE', command=show_alarm_clock).grid(row=3, 
                                                       column=0, 
                                                       sticky=tk.W, 
                                                       pady=4)
tk.Button(master, 
          text='DISMISS', 
          command=master.quit).grid(row=3, 
                                    column=1, 
                                    sticky=tk.W, 
                                    pady=4)

#If system time is equal to alarm time,then play beep sound from winsound package until snooze is pressed
current_time = datetime.datetime.now()
now = current_time.strftime("%H:%M:%S")
date = current_time.strftime("%d/%m/%Y")
print("The Set Date is:",date)
print(now)
if now == e1:
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 2000  # Set Duration To 1000 ms == 2 second
    print("Wake up !!!!")
    winsound.Beep(frequency, duration) 


tk.mainloop()
