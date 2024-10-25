import os #For looping through directories
import pandas #for handling csv conversion

#Alternate solution, not currently used
""" filecount = 0
print("Listing txt files:")
for dirpath, dirnames, filenames in os.walk("."):
   for filename in filenames:
      if filename.endswith(".txt"):
         print(filename)
         filecount += 1
print("Number of files converted: ",filecount) """

for root, dirs, files in os.walk(os.path.abspath("../Midterm/data")):
    for file in files:
        print(os.path.join(root, file))