import time
import csv
from os.path import exists
import os
from tkinter import *

# Filename of the csv file
filename = "statistics.csv"

# Defines how long the loop of the program will be in seconds
loop_time = 5

def csv_write(filename, args):
    with open(filename, mode="a", newline='') as csvfile:
            csvwriter = csv.writer(
                csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONE
            )

            csvwriter.writerow(
                args
            )

# Defines the Headers
def init_csv(csv_writer):
    csv_writer.writerow(["Instance", "Index", "Keys_Pressed\n"])
# Read the CSV file and import the last line
def import_csv(file_name):
    data = []

    
    if exists(file_name) and os.stat(file_name).st_size != 0:
        with open(file_name, mode="r", newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                if row:
                    columns = [row[0], row[1]]
                    data.append(columns)
            return data
    else:
        csv_write(file_name, ["Instance", "Index", "Keys_Pressed"])
    return [[0, 0]]
        


if exists(filename):
    data = import_csv(filename)[-1]
    instance = int(data[0]) + 1
    index = int(data[1]) + 1
else:
    with open(filename, mode='w', newline='') as csv_file:
        init_csv(csv.writer(csv_file))
    instance = 1
    index = 1




# Defining the root window and its properties
root = Tk()
root.title("Text Editor Function")
root.geometry("500x500")
root.minsize(height=250, width=250)
root.maxsize(height=800, width=800)

# implementing scrollbar functionality
scrollbar = Scrollbar(root)

# packing the scrollbar function
scrollbar.pack(side=RIGHT, fill=Y)

# Defines the use of the text box, and its link to the scrollbar
text = Text(root, yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)

# Prints the length of the entire document so far.
# Replacing print with return gives good output.
# Should be placed inside of a class. This is just
# a working prototype.
def getText():
    return len(text.get("1.0", "end-1c"))

keys_pressed = 0

def key_pressed(event):
    global keys_pressed 
    keys_pressed += 1
root.bind("<Key>", key_pressed)


previous_time = time.time()
start_time = previous_time

# Main Loop
while True:
    # Insert any necessary looped code here

    if time.time() - previous_time >= loop_time:
        previous_time += loop_time
        temp_keys_pressed, keys_pressed = keys_pressed, 0
        
        if index == 0:
            csv_write(filename, ["Instance", "Index", "Keys_Pressed"])
        csv_write(filename, [f"{instance}", f"{index}", f"{temp_keys_pressed}"])
        index += 1

    # Takes place of root.mainloop() so that code can be added
    root.update_idletasks()
    root.update()