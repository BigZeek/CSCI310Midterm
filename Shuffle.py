"""CSCI310 Midterm
Authors: Samuel Arne, Zak Groenewold, Dinesh Seveti
Date: 10/26/2024"""

"""
TODO: 
Set up deletion of old subdirectories or files
Test everything
"""


import os #For looping through directories
import pandas as pd #for handling csv conversion
import sched, time #for scheduling repeated run
import shutil, datetime #For changing file creation dates

scheduler = sched.scheduler(time.time, time.sleep) #init scheduler object

def shuffle_files():
   #loop through files and directories
   for root, dirs, files in os.walk(os.path.abspath("../Midterm/data")):
       for dir in dirs:
         current_dir = os.path.join(root, dir)
         print(current_dir) #for troubleshooting, remove when finished
         
         file_list = next(os.walk(current_dir))[2] #count only files and ignore subdirectories
         
         #loop through files in subdirectories
         for file in file_list:
            current_file = os.path.join(root, file)
            int_rename = 0 #for renaming files in sequence
            
            """All below code will need testing."""
            file_birth = os.path.getctime(current_file)
            birth_timestamp = time.ctime(file_birth)
            #Print current filename and creation time
            print("Current working file: ", file) 
            print("File created at: ", birth_timestamp)
            #print(file) #for troubleshooting, remove when finished
            """Backdate file within the last 10 days"""
            new_creation_datetime = datetime.datetime(2024, 10, 15)
            shutil.cmp(file, new_creation_datetime)
            
            """Convert file to CSV not tested, remove comments to test"""
            #df = pd.read_csv(file)
            #file = df.to_csv(int_rename + '.csv') #rename and convert to csv 
            
            """Display new file name and creation date"""
            print("New file name is: ", file)
            print("New file creation date is: ", new_creation_datetime)
            
            """Unify in parent directory"""
            source = current_file
            destination = os.path.join(root, current_dir) #Destination should be parent directory, ie takeoff, landing, etc.
            os.rename(source,destination)
            
            """Delete any remaining subdirectories/files"""
            
               
   print("Shuffle complete!")

#set to run every 5 seconds, set larger gap for video recording.
def repeat_shuffle():
   scheduler.enter(1,1,shuffle_files,())
   scheduler.enter(5,1,repeat_shuffle, ())
   
   
#Run shuffler program
repeat_shuffle()
scheduler.run() 