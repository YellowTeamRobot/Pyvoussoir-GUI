import os
import subprocess
import tkinter as tk
from tkinter import filedialog

def process_images():
    try:
        error.pack_forget()
        input_folder = input_folder_var.get()
        output_folder = output_folder_var.get()
        file_type = file_type_var.get()
        page_height = page_height_var.get()
        page_width = page_width_var.get()
        dpi = dpi_var.get()

        LL = LL_var.get()
        LR = LR_var.get()
        LT = LT_var.get()
        LB = LB_var.get()
        RL = RL_var.get()
        RR = RR_var.get()
        RT = RT_var.get()
        RB = RB_var.get()

        # List all files in the input folder
        input_files = os.listdir(input_folder)

        # Iterate through the input files
        for input_file in input_files:
            if input_file.endswith(f'.{file_type}'):
                # Generate output file names based on the input file name
                base_name = os.path.splitext(input_file)[0]
                output_left = os.path.join(output_folder, base_name + '_left.' + file_type)
                output_right = os.path.join(output_folder, base_name + '_right.' + file_type)

                # Construct the full command
                command = f'pyvoussoir --page-height {page_height} --page-width {page_width} -d {dpi} {noLeft} {noRight} --offset-left-page-left-side {LL} --offset-left-page-right-side {LR} --offset-left-page-top-side {LT} --offset-left-page-bottom-side {LB} --offset-right-page-left-side {RL} --offset-right-page-right-side {RR} --offset-right-page-top-side {RT} --offset-right-page-bottom-side {RB}  --input-image "{os.path.join(input_folder, input_file)}" "{output_left}" "{output_right}"'

                # Execute the command using subprocess
                subprocess.call(command, shell=True)
    except:
        error.pack()


            
def toggle_advanced_options():
    if advance_options_var.get():
        # Show the widgets by packing them
        offsets.pack()
        LL_label.pack()
        LL_entry.pack()
        LR_label.pack()
        LR_entry.pack()
        LT_label.pack()
        LT_entry.pack()
        LB_label.pack()
        LB_entry.pack()        
        
        RL_label.pack()
        RL_entry.pack()
        RR_label.pack()
        RR_entry.pack()
        RT_label.pack()
        RT_entry.pack()
        RB_label.pack()
        RB_entry.pack()  
        
        spacer.pack(pady=1)
        
        no_left_checkbox.pack()
        no_right_checkbox.pack()
    else:
        # Hide the widgets by removing them from the packing
        offsets.pack_forget()
        LL_label.pack_forget()
        LL_entry.pack_forget()
        LR_label.pack_forget()
        LR_entry.pack_forget()
        LT_label.pack_forget()
        LT_entry.pack_forget()
        LB_label.pack_forget()
        LB_entry.pack_forget()        
        
        RL_label.pack_forget()
        RL_entry.pack_forget()
        RR_label.pack_forget()
        RR_entry.pack_forget()
        RT_label.pack_forget()
        RT_entry.pack_forget()
        RB_label.pack_forget()
        RB_entry.pack_forget()  
        
        spacer.pack_forget()
        
        no_left_checkbox.pack_forget()
        no_right_checkbox.pack_forget()
        
def NoLeftToggle(): 
    global noLeft
    if no_left_var.get():
        noLeft = "--no-left-page"
    else:
        noLeft = ""
        
def NoRightToggle():
    global noRight
    if no_right_var.get():
        noRight = "--no-right-page"
    else:
        noRight = ""
        

        
# Create a tkinter window
root = tk.Tk()
root.title("Pyvoussoir GUI")

# Set the default window width and height
root.geometry("350x850")  # Width x Height

# Customize the appearance (font, background, foreground)
root.configure(bg="#f0f0f0")  # Background color

# Create and pack widgets for choosing input folder, output folder, file type, page height, and page width
input_folder_var = tk.StringVar()
output_folder_var = tk.StringVar()
file_type_var = tk.StringVar(value="jpg")
page_height_var = tk.StringVar(value="10")
page_width_var = tk.StringVar(value="6")
dpi_var = tk.StringVar(value="600")
LL_var = tk.StringVar(value="0")
LR_var = tk.StringVar(value="0.5")
LT_var = tk.StringVar(value="0.5")
LB_var = tk.StringVar(value="0")
RL_var = tk.StringVar(value="-0.5")
RR_var = tk.StringVar(value="0")
RT_var = tk.StringVar(value="0.5")
RB_var = tk.StringVar(value="0")

# Label and Entry widgets
tk.Label(root, text="", bg="#f0f0f0").pack(pady=5)

tk.Label(root, text="Input Folder:", bg="#f0f0f0").pack()
tk.Entry(root, textvariable=input_folder_var, width=45).pack()
tk.Button(root, text="Browse", command=lambda: input_folder_var.set(filedialog.askdirectory())).pack()

tk.Label(root, text="", bg="#f0f0f0").pack(pady=5)

tk.Label(root, text="Output Folder:", bg="#f0f0f0").pack()
tk.Entry(root, textvariable=output_folder_var, width=45).pack()
tk.Button(root, text="Browse", command=lambda: output_folder_var.set(filedialog.askdirectory())).pack()

tk.Label(root, text="", bg="#f0f0f0").pack(pady=5)

tk.Label(root, text="File Type (e.x. jpg or png):", bg="#f0f0f0").pack()
tk.Entry(root, textvariable=file_type_var).pack()

tk.Label(root, text="Output DPI:", bg="#f0f0f0").pack()
tk.Entry(root, textvariable=dpi_var).pack()

tk.Label(root, text="", bg="#f0f0f0").pack(pady=1)

tk.Label(root, text="Page Height:", bg="#f0f0f0").pack()
tk.Entry(root, textvariable=page_height_var).pack()

tk.Label(root, text="Page Width:", bg="#f0f0f0").pack()
tk.Entry(root, textvariable=page_width_var).pack()




# Advanced Options
no_left_var = tk.BooleanVar()
no_left_checkbox = tk.Checkbutton(root, text="No Left Page", bg="#f0f0f0", variable=no_left_var, command=NoLeftToggle)
no_right_var = tk.BooleanVar()
no_right_checkbox = tk.Checkbutton(root, text="No Right Page", bg="#f0f0f0", variable=no_right_var, command=NoRightToggle)

offsets = tk.Label(root, text="Offsets:", bg="#f0f0f0")
LL_label = tk.Label(root, text="Left Page Left Side:", bg="#f0f0f0")
LL_entry = tk.Entry(root, textvariable=LL_var)
LR_label = tk.Label(root, text="Left Page Right Side:", bg="#f0f0f0")
LR_entry = tk.Entry(root, textvariable=LR_var)
LT_label = tk.Label(root, text="Left Page Top Side:", bg="#f0f0f0")
LT_entry = tk.Entry(root, textvariable=LT_var)
LB_label = tk.Label(root, text="Left Page Bottom Side:", bg="#f0f0f0")
LB_entry = tk.Entry(root, textvariable=LB_var)

RL_label = tk.Label(root, text="Right Page Left Side:", bg="#f0f0f0")
RL_entry = tk.Entry(root, textvariable=RL_var)
RR_label = tk.Label(root, text="Right Page Right Side:", bg="#f0f0f0")
RR_entry = tk.Entry(root, textvariable=RR_var)
RT_label = tk.Label(root, text="Right Page Top Side:", bg="#f0f0f0")
RT_entry = tk.Entry(root, textvariable=RT_var)
RB_label = tk.Label(root, text="Right Page Bottom Side:", bg="#f0f0f0")
RB_entry = tk.Entry(root, textvariable=RB_var)
spacer = tk.Label(root, text="", bg="#f0f0f0")
NoLeftToggle()
NoRightToggle()

# Create and pack a button to start image processing
process_button = tk.Button(root, text="Process Images",bg="#b3d3ad", command=process_images)
process_button.pack(pady=20)

# Error Texts
error = tk.Label(root, text="An error has occurred. Possible remedies include:\n Make sure input and output folders are selected and valid\n Make sure the output folder is empty\n Make sure your images are in correct format", bg="#F58588")

# Create a Checkbutton for "Advance Options"
advance_options_var = tk.BooleanVar()
advance_options_checkbox = tk.Checkbutton(root, text="Advance Options", bg="#f0f0f0", variable=advance_options_var, command=toggle_advanced_options)
advance_options_checkbox.pack()

root.mainloop()
