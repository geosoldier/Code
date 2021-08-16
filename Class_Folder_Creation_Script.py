#****************************
# Created by Eric Adams - Date: August 2 2021
# Purpose: To automatically create weekly folders for AMU or NCSU Classes
# Use Limitations: None
# Last Updated: 2 August, 2021
# I removed this first commit line and now have access to work with GITHUB
#****************************

#import modules
import os

#Set the New Class Variable - reaffirm that that is the new class by printing it.
newClassFolder = input("What is the new class..i.e., INTL504...?")
print ("\n\nThe new class is " + newClassFolder)


#Join the new class folder variable to the AMU directory
amuDIR = r"C:\Users\geoso\OneDrive\Katya\AMU"

newClassDir = os.path.join (amuDIR, newClassFolder)
os.mkdir (newClassDir)

print ("\nThe new class directory is " + newClassDir)

#create new weekly folders variable
newWeek1 = "Week 1"
newWeek2 = "Week 2"
newWeek3 = "Week 3"
newWeek4 = "Week 4"
newWeek5 = "Week 5"
newWeek6 = "Week 6"
newWeek7 = "Week 7"
newWeek8 = "Week 8"
newReference = "References"
newData = "Data"

#["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6",
#           "Week 7", "Week 8", "References", "Data"]

#creat the new folder for week 1
newWeekFolders = os.path.join (newClassDir, newWeek1)
if not os.path.exists(newWeekFolders):
    os.mkdir(newWeekFolders)

#creat the new folder for week 2
newWeekFolders = os.path.join (newClassDir, newWeek2)
if not os.path.exists(newWeekFolders):
    os.mkdir(newWeekFolders)

#creat the new folder for week 3
newWeekFolders = os.path.join (newClassDir, newWeek3)
if not os.path.exists(newWeekFolders):
    os.mkdir(newWeekFolders)

#creat the new folder for week 4
newWeekFolders = os.path.join (newClassDir, newWeek4)
if not os.path.exists(newWeekFolders):
    os.mkdir(newWeekFolders)

#creat the new folder for week 5
newWeekFolders = os.path.join (newClassDir, newWeek5)
if not os.path.exists(newWeekFolders):
    os.mkdir(newWeekFolders)

#creat the new folder for week 6
newWeekFolders = os.path.join (newClassDir, newWeek6)
if not os.path.exists(newWeekFolders):
    os.mkdir(newWeekFolders)

#creat the new folder for week 7
newWeekFolders = os.path.join (newClassDir, newWeek7)
if not os.path.exists(newWeekFolders):
    os.mkdir(newWeekFolders)

#creat the new folder for week 8
newWeekFolders = os.path.join (newClassDir, newWeek8)
if not os.path.exists(newWeekFolders):
    os.mkdir(newWeekFolders)

#creat the new folder for the references folder
newWeekFolders = os.path.join (newClassDir, newReference)
if not os.path.exists(newWeekFolders):
    os.mkdir(newWeekFolders)

#creat the new folder for the data folder
newWeekFolders = os.path.join (newClassDir, newData)
if not os.path.exists(newWeekFolders):
    os.mkdir(newWeekFolders)

print ("\nFolders for each week for class " + newClassFolder + "have been created. Thank you for using my tool.")
