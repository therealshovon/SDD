from tkinter import * 
from PIL import ImageTk


window=Tk() 

window.geometry('1280x720+0+0')
window.resizable(False, False)

backgroundImage= ImageTk.PhotoImage(file='login_background.jpg')

bgLabel= Label(window, image=backgroundImage)
bgLabel.place(x=0, y=0)

#login frame 
loginFrame=Frame(window)
loginFrame.place(x=900, y=200)
iconImage= PhotoImage(file='login_frame_user.png')
UserIconLabel=Label(loginFrame, image= iconImage)
UserIconLabel.grid(row=0, column=0)








window.mainloop()
