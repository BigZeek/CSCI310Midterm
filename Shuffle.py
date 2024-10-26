import os #For looping through directories
import pandas as pd #for handling csv conversion
import sched #for scheduling repeated run
import time

scheduler = sched.scheduler(time.time, time.sleep)

def shuffle_files():
   for root, dirs, files in os.walk(os.path.abspath("../Midterm/data")):
       for dir in dirs:
         count = 0 #used to count files in each directory
         current_dir = os.path.join(root, dir)
         print(current_dir) #for troubleshooting, remove when finished
         
         file_list = next(os.walk(current_dir))[2] #count only files and ignore subdirectories
         count += len(file_list)
         for file in file_list:
            int_rename = 0
            print(file) #for troubleshooting, remove when finished
            
            #Below code will need testing.
            df = pd.read_csv(file)
            df.to_csv(int_rename + '.csv') #rename and convert to csv 
   print("Shuffle complete!")
   


#set to run every 5 seconds, set larger gap for video recording.
def repeat_shuffle():
   scheduler.enter(1,1,shuffle_files,())
   scheduler.enter(5,1,repeat_shuffle, ())
   
repeat_shuffle()
scheduler.run() 