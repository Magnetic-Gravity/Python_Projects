print("Welcome to Digital Clock Application!")

#Step 1: Import Libraries
import tkinter as tk
from time import strftime 

#Step 2: create window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x100") #size of window
root.configure(bg="black") #background color

#Step 3 : create clock Label
label = tk.Label(root, font=('Arial',50,'bold'), bg='black', fg='red')
label.pack(anchor='center', pady=20)

#Step 4 : function to update time
def update_clock_time():
    current_time = strftime("%H:%M:%S") #get current time
    label.config(text=current_time) #update label text)
    label.after(1000, update_clock_time) #call this function after 1 second 
    
#Step 5 : start the time update function
update_clock_time()

#Step 6 : run the main Loop
root.mainloop()

print("Have a nice day!")