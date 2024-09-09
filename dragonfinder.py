import tkinter as tk
from tkinter import ttk
import datetime
import math

# Create the main application window
root = tk.Tk()
root.title("NeXXus Dragon Finder")

# Set a minimum window size and padding for a modern feel
root.geometry("400x600")
root.configure(padx=15, pady=15, bg="#f0f0f0")  # Light background for a modern look

# Initialize lists
xcoords = []
ycoords = []
times = []

# Flag to indicate if sorting is needed
sort_needed = False

def update_display():
    global sort_needed

    listbox.delete(0, tk.END)  # Clear current display

    if sort_needed:
        # Get sorted indices by countdown time
        sorted_indices = sorted(range(len(times)), key=lambda i: times[i])
        
        for i in sorted_indices:
            countdown_time = datetime.timedelta(seconds=times[i])
            dist = math.floor(math.sqrt((int(xcoords[i]) - int(x_entry.get()))**2 + (int(ycoords[i]) - int(y_entry.get()))**2))
            listbox.insert(tk.END, f"Fortress: {xcoords[i]}:{ycoords[i]} - {countdown_time} - Distance: {dist}")

        sort_needed = False
    else:
        # Just update distances without resorting
        for i in range(len(times)):
            countdown_time = datetime.timedelta(seconds=times[i])
            dist = math.floor(math.sqrt((int(xcoords[i]) - int(x_entry.get()))**2 + (int(ycoords[i]) - int(y_entry.get()))**2))
            listbox.insert(tk.END, f"Fortress: {xcoords[i]}:{ycoords[i]} - {countdown_time} - Distance: {dist}")

def add_item():
    global sort_needed

    entry_text = entry.get()
    if entry_text:
        try:
            # Split input into coordinates and time parts
            coords_part, time_part = entry_text.split(" ")
            x, y = coords_part.split(":")
            hours, minutes, seconds = map(int, time_part.split(":"))

            # Calculate total countdown time in seconds
            total_seconds = hours * 3600 + minutes * 60 + seconds

            # Update lists
            xcoords.append(x)
            ycoords.append(y)
            times.append(total_seconds)
            
            # Set flag to indicate that sorting is needed
            sort_needed = True

            # Refresh the list display
            update_display()
            entry.delete(0, tk.END)  # Clear the entry box
        except ValueError:
            # Handle invalid input
            print("Invalid input format. Please use 'xxx:yyy HH:MM:SS'.")

def update_timers():
    global times
    for i in range(len(times)):
        if times[i] > 0:
            times[i] -= 1
    update_display()
    root.after(1000, update_timers)  # Update every second

def delete_item():
    global sort_needed
    if len(xcoords) > 0:  # Ensure there's at least one item to delete
        # Delete the item at the end of the list (last index)
        index = len(xcoords) - 1
        del xcoords[index]
        del ycoords[index]
        del times[index]
        sort_needed = True  # Set flag to sort the list on the next update
        update_display()

# Apply a modern theme to ttk widgets
style = ttk.Style()
style.theme_use('clam')  # Use a cleaner 'clam' theme
style.configure("TButton", padding=6, relief="flat", background="#5a9")
style.configure("TEntry", padding=5)
style.configure("TLabel", font=("Helvetica", 12))

# Create a label for the list of fortresses
label = ttk.Label(root, text="Fortresses:", background="#f0f0f0")
label.pack(pady=(0, 0))

# Create a listbox to display the fortresses with no selection capability
listbox = tk.Listbox(root, width=50, height=20, relief="flat", font=("Courier", 10),
                     bg="#ffffff", bd=0, highlightthickness=0, selectbackground="#a0c4ff", selectforeground="black",
                     selectmode=tk.NONE)  # Disable selection
listbox.pack(pady=(10, 10), fill="x")

# Create an entry widget for input with a modern look
entry = ttk.Entry(root, width=56)
entry.pack(pady=(0, 10), fill="x")

# Create a button to add the input to the list and make it span the full width
button = ttk.Button(root, text="Add Fortress", command=add_item)
button.pack(pady=(0, 10), fill="x")

style.configure("RedButton.TButton", background="#f8d7da", foreground="black")

# Create a button to delete the item at the top
#delete_button = ttk.Button(root, text="Delete Top", command=delete_item, style="RedButton.TButton")
#delete_button.pack(pady=(0, 10), fill="x")

label = ttk.Label(root, text="Format: \"xxx:yyy HH:MM:SS\"", background="#f0f0f0", font=("Courier", 10))
label.pack(pady=(0, 0))

label = ttk.Label(root, text="Your Coordinates:", background="#f0f0f0")
label.pack(pady=(10, 10))

# Frame to hold the x and y coordinate entry boxes
coordinate_frame = ttk.Frame(root)
coordinate_frame.pack(pady=(0, 10), fill="x")

# Configure grid layout to make both columns (for x and y entries) take up 50% of the frame
coordinate_frame.columnconfigure(0, weight=1)
coordinate_frame.columnconfigure(1, weight=1)

# Create two entry widgets for x and y coordinates that span half the frame
x_entry = ttk.Entry(coordinate_frame)
x_entry.grid(row=0, column=0, padx=(0, 10), sticky="ew")

y_entry = ttk.Entry(coordinate_frame)
y_entry.grid(row=0, column=1, padx=(10, 0), sticky="ew")

# Initialize the list display and start the countdown timer update loop
update_display()
update_timers()

# Start the application loop
root.mainloop()
