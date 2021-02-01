
# importing tkinter
from tkinter import * 
from tkinter.ttk import * 
from time import strftime 
  
# creating tkinter window 
root = Tk() 
root.title('Resizable') 
root.geometry('250x100') 
  
Label(root, text = 'It\'s resizable').pack(side = TOP, pady = 10) 
  
# allowing root window to change its size 
root.resizable(True, True) 
  
mainloop() 
