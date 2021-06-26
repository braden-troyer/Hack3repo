import time
import csv
from tkinter import *

# Defines how long the loop of the program will be
loop_time = 60


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
    print(len(text.get("1.0", "end-1c")))


previous_time = time.time()


# Main Loop
while True:
    # Insert any necessary looped code here

    if time.time() - previous_time >= loop_time:
        previous_time += loop_time
        getText()

    # Takes place of root.mainloop() so that code can be added
    root.update_idletasks()
    root.update()