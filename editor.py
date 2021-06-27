import time
import csv
from tkinter import *

filename = "statistics.csv"

# Read the CSV file and import the last line for
def import_csv(file_name):
    data = []
    with open(file_name, mode="r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        global line_count
        for row in csv_reader:
            if row:
                columns = [row[0], row[1]]
                data.append(columns)
    return data

data = import_csv(filename)[-1]

instance = int(data[0]) + 1
index = int(data[1]) + 1

# Defines how long the loop of the program will be in seconds
loop_time = 5


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
        with open(filename, mode="a", newline='') as csvfile:
            csvwriter = csv.writer(
                csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )

            csvwriter.writerow(
                [f"{instance}", f"{index}", f"{temp_keys_pressed}"]
            )
        index += 1

    # Takes place of root.mainloop() so that code can be added
    root.update_idletasks()
    root.update()