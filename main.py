import tkinter as tk
from tkinter import END, PhotoImage, messagebox

# a function to check if the number is an Armstrong number
def is_armstrong(num):
    original_number = num

    # length of input number
    no_of_digits = len(str(num))

    # sum of cubes of each digit
    cube_sum = sum(int(digit) ** no_of_digits for digit in str(num))
    return cube_sum == original_number

# Function to check the user's input and display the result
def check_armstrong():
    try:

        # Attempt to convert the input to an integer
        num = int(entry.get())
        
        # Check if the number is within the valid range (100 to 999)
        if 999 >= num >= 100:
            if is_armstrong(num):
                # Display result in green, if the input number is an Armstrong number and hide the message icon
                result.config( text= f"{num} is an Armstrong number!", foreground="green" )
                message_icon.config( image="" )
            else:
                # Display result in red, if the input number is not an Armstrong number and hide the message icon
                result.config( text= f"{num} is not an Armstrong number!.", foreground="red" )
                message_icon.config( image="" )
        else:
            # warning message icon
            message_icon.config( image=warning_img )
            # Show a warning message if the number is not in the valid range
            result.config( text="Invalid Input!!\nPlease enter a 3-digit number between 100 and 999", foreground="#ffaa00" )
    except ValueError:
        # error image icon
        message_icon.config( image=error_img )
        # Show an error message if the input is not a valid number
        result.config( text="Invalid Input!!\nPlease enter a valid number.", foreground="#cc0000" )
    # delete input after checking the user's input    
    entry.delete(0, END)

# Function to exit the app
def exit_app():
        # create a dialog box to ask if the user wants to exit or not
        confirm_exit = messagebox.askyesno( title="Exit Confirmation?", message="Are you sure you want to exit?" )
        # if the user choose yes, exit the app
        if confirm_exit:
            # close app
            app.destroy()

# Function to clear result area
def clear_result():
    result.config( text="" )
    message_icon.config( image="" )

# Create the main window app
app = tk.Tk()

# app title
app.title("3-Digit Armstrong Number Checker")

# app size
app.geometry("500x400")

# app expansion set to (width=false, height=false)
app.resizable(False, False)

# app background color
app.configure(background="#f0f0f0")

# app icon
app_icon = PhotoImage(file='icon_images/app_icon.png')
app.iconphoto(False, app_icon)

# message_icon images
error_img = PhotoImage(file="icon_images/error.png")
warning_img = PhotoImage(file="icon_images/caution.png")

# Create and place widgets
# title label
title = tk.Label(app, text="3-Digit Armstrong Number Checker", font=("Verdana", 15, "bold"))
title.pack(pady=10)

# info label
info = tk.Label(app, text= "Enter a 3-digit number between 100 - 999:", font=("Verdana", 10))
info.pack()

# entry input field
entry = tk.Entry(app, width=25, font=("Arial", 12))
entry.pack(pady=5)

# message icon label
message_icon = tk.Label(app, image="")
message_icon.pack()

# result label
result = tk.Label(app, text="", font=("Arial", 12, "bold"))
result.pack()

# check or confirm button
check_button = tk.Button(app, text="Check", font=("Helvetica", 10), command=check_armstrong, relief="raised", bg="#4caf50", fg="white",)
check_button.pack(pady=10)

# clear result output button
clear_result_button = tk.Button(app, text="Clear Result", font=("Helvetica", 10), command=clear_result, relief="raised", bg="#4219cc", fg="white",)
clear_result_button.pack(pady=10)

# exit button
exit_button = tk.Button(app, text="Exit", font=("Helvetica", 12), command=exit_app, relief="sunken", bg="#cc0000", fg="black")
exit_button.pack(pady=10)

# Start the GUI event loop
app.mainloop()
