
from tkinter import * 
from PIL import ImageTk
import tkinter.ttk as ttk 
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
import pymysql


root = Tk()
root.geometry("1280x720+0+0")
root.title("Staff Portal ")
root.tk.call('tk', 'scaling', 1.5)

def close():
	root.destroy()


def StudentPortal():


	def AddDeliverable():
		Ref= e_Ref.get()
		CourseID = e_CourseID.get();
		Details = e_Details.get();
		StudentID = e_StudentID.get();
		DeliverableLink= e_NoteLink.get();
		
		if (Ref =="" or CourseID =="" or Details =="" or StudentID =="" or DeliverableLink =="" ):
			Messagebox.showerror("Alert", "All fields are required")
		else:
			con = mysql.connect(host="localhost", user="root", password="", database="educationapp")
			cursor = con.cursor()
			cursor.execute("insert into deliverable values ('"+ Ref +"', '"+ CourseID +"', '"+ Details +"', '"+ StudentID +"', '"+ DeliverableLink +"')")
			cursor.execute("commit"); 
			
			e_Ref.delete(0,'end')
			e_CourseID.delete(0,'end')
			e_Details.delete(0,'end')
			e_StudentID.delete(0,'end')
			e_NoteLink.delete(0,'end')

			#ShowUsersDetails()
			Messagebox.showinfo("Deliverable Submission", "Deliverable Added Successfully")
			con.close();



	SHeadingCourse = Label(root, text=' Student Portal', font=('bold', 14))
	SHeadingCourse.place(x=550, y=20)


	#Delete a student 


	#Deliverables Link Note Link (All Link)


	FNo = Label(root, text='Ref No.', font=('bold', 10))
	FNo.place(x=450, y=50)

	e_Ref= Entry(width=30,font=('Arial 10'))
	e_Ref.place (x=580, y=50)


	FCourseID= Label(root, text='CourseID', font=('bold', 10))
	FCourseID.place(x=450, y=80)

	e_CourseID = Entry(width=30,font=('Arial 10'))
	e_CourseID.place (x=580, y=80)


	F_Details = Label(root, text='Details', font=('bold', 10))
	F_Details.place(x=450, y=110)
	
	e_Details = Entry(width=30,font=('Arial 10'))
	e_Details.place (x=580, y=110)

	ClassNoteLink = Label(root, text='Deliverable Link', font=('bold', 10))
	ClassNoteLink.place(x=450, y=140)
	
	e_NoteLink = Entry(width=30,font=('Arial 10'))
	e_NoteLink.place (x=580, y=140)

	StudentID = Label(root, text='StudentID', font=('bold', 10))
	StudentID.place(x=450, y=170)
	
	e_StudentID = Entry(width=30,font=('Arial 10'))
	e_StudentID.place (x=580, y=170)


	NoteAdding = Button(root, text="Submit Deliverable", font=('Arial 10'), bg="white", command=AddDeliverable)
	NoteAdding.place(x=580, y=220)



StudentPortal()
root.mainloop()












