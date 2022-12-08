from tkinter import * 
from PIL import ImageTk
import tkinter.ttk as ttk 
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
import pymysql


root = Tk()
root.geometry("1280x720+0+0")
root.title("Super Admin Portal ")



def UserLogin():
	
	if e_UserName.get()=="" or e_PassWord.get()=="":
		Messagebox.showerror("Error","Enter Username And Password",parent=root)	
	else:
		try:
			con = pymysql.connect(host="localhost",user="root",password="",database="educationapp")
			cur = con.cursor()

			cur.execute("select * from user where UserName=%s and PassWord = %s",(e_UserName.get(), e_PassWord.get()))
			row = cur.fetchone()

			if row==None:
				Messagebox.showerror("Error" , "Invalid User Name And Password", parent = root)

			else:
				Messagebox.showinfo("Success" , "Successful Login" , parent = root)
		
				StudentPortal()
			con.close()
		except Exception as es:
			Messagebox.showerror("Error" , f"Error due to : {str(es)}", parent = root)


backgroundImage= ImageTk.PhotoImage(file='login_background.jpg')

bgLabel= Label(root, image=backgroundImage)
bgLabel.place(x=0, y=0)

#login frame 
LoginFrame=Frame(root)
LoginFrame.place(x=600, y=200, width=300, height=300)
iconImage= PhotoImage(file='login_frame_user.png')
UserIconLabel=Label(LoginFrame, image= iconImage)
UserIconLabel.grid(row=0, column=1)

SUserName = Label(LoginFrame, text='Username', font=('bold', 10))
SUserName.grid(row=1, column=0)

e_UserName = Entry(LoginFrame, width=30,font=('Arial 10'))
e_UserName.grid(row=1, column=1)

SPassWord = Label(LoginFrame, text='Password', font=('bold', 10))
SPassWord.grid(row=2, column=0)

e_PassWord = Entry(LoginFrame, width=30,font=('Arial 10'))
e_PassWord.grid(row=2, column=1)

UserLoginButton = Button(LoginFrame, text=" Login ", font=('Arial 10'), bg="yellow", command=UserLogin)
UserLoginButton.grid(row=3, column=1)



def close():
	root.destroy()


def StudentPortal():

	root = Tk()
	root.geometry("1280x720+0+0")
	root.title("Student ")
	root.ttk.call('tk', 'scaling', 1.5)
	def GradeStudent():
		CourseID = e_CourseID.get();
		StudentID = e_StudentID.get();
		Grade = e_Grade.get();
				
		if (CourseID =="" or StudentID =="" or Grade ==""):
			Messagebox.showerror("Grade Warning", "All fields are required")
		else:
			con = mysql.connect(host="localhost", user="root", password="", database="educationapp")
			cursor = con.cursor()
			cursor.execute("insert into studentgrade values ('"+ CourseID +"', '"+ StudentID +"', '"+ Grade +"')")
			cursor.execute("commit"); 

			e_CourseID.delete(0,'end')
			e_StudentID.delete(0,'end')
			e_Grade.delete(0,'end')
			
		
			#ShowUsersDetails()
			Messagebox.showinfo("Insert Status", "Grading Successful!")
			con.close();

	def DeleteCourse():
		if (e_DelCourseID.get()==""):
			Messagebox.showinfo("Insert Status", "CourseID Required!")
		else:
			con = mysql.connect(host="localhost", user="root", password="", database="educationapp")
			cursor = con.cursor()
			cursor.execute("delete from createcourse where CourseID = '"+ e_DelCourseID.get() +"'")
			cursor.execute("commit"); 
			e_DelCourseID.delete(0,'end')
			#ShowUsersDetails()

			Messagebox.showinfo("Drop Status", "Course Deleted Successfully!")
			con.close();



	def EnrollStudent():
		CourseID= e_SCourseID.get()
		StudentID = e_SStudentID.get();
		StudentUserName = e_SStudentUserName.get();
		"""
		MockScore="";
		WrittenExamScore="",
		AssignmentScore="",
		QuizzScore="",
		ProjectScore="",
		PresentationScore="",
		HomeWorkScore="",
		ClassWorkScore="",
		OverallGrade="",
		TeacherRemarks="", """

		if (CourseID =="" or StudentID =="" or StudentUserName ==""):
			Messagebox.showerror("Enroll Status", "All fields are required")
		else:
			con = mysql.connect(host="localhost", user="root", password="", database="educationapp")
			cursor = con.cursor()
			cursor.execute("insert into coursestudents values ('"+ CourseID +"', '"+ StudentID +"', '"+ StudentUserName +"')")
			cursor.execute("commit"); 

			e_SCourseID.delete(0,'end')
			e_SStudentID.delete(0,'end')
			
			e_SStudentUserName.delete(0,'end')
		
			#ShowUsersDetails()
			Messagebox.showinfo("Insert Status", "Student Enrolled Successfully!")
			con.close();

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
	SHeadingCourse.place(x=20, y=20)


	CourseID = Label(root, text='CourseID', font=('bold', 10))
	CourseID.place(x=20, y=60)

	e_CourseID = Entry(width=30,font=('Arial 10'))
	e_CourseID.place (x=150, y=60)


	StudentID = Label(root, text='Student ID', font=('bold', 10))
	StudentID.place(x=20, y=90)

	e_StudentID = Entry(width=30,font=('Arial 10'))
	e_StudentID.place (x=150, y=90)


	Grade = Label(root, text='Grade', font=('bold', 10))
	Grade.place(x=20, y=120)

	e_Grade = Entry(width=30,font=('Arial 10'))
	e_Grade.place (x=150, y=120)


	Grade = Button(root, text="Give Grade", font=('Arial 10'), bg="white", command=GradeStudent)
	Grade.place(x=180, y=160)


	#Drop a course 
	SCourseID = Label(root, text='Course ID', font=('bold', 10))
	SCourseID.place(x=20, y=250)
	
	e_DelCourseID = Entry(width=20,font=('Arial 10'))
	e_DelCourseID.place (x=100, y=250)

	DropCourse = Button(root, text="Drop Course", font=('Arial 10'), bg="white", command=DeleteCourse)
	DropCourse.place(x=270, y=247)



	#Enroll a student 


	SCourseID = Label(root, text='CourseID', font=('bold', 10))
	SCourseID.place(x=20, y=300)

	e_SCourseID = Entry(width=30,font=('Arial 10'))
	e_SCourseID.place (x=150, y=300)


	SStudentID = Label(root, text='Student ID', font=('bold', 10))
	SStudentID.place(x=20, y=330)

	e_SStudentID = Entry(width=30,font=('Arial 10'))
	e_SStudentID.place (x=150, y=330)


	SStudentUserName = Label(root, text='Student User Name', font=('bold', 10))
	SStudentUserName.place(x=20, y=360)
	
	e_SStudentUserName = Entry(width=30,font=('Arial 10'))
	e_SStudentUserName.place (x=150, y=360)

	AdmitStudent = Button(root, text="Enrol Student", font=('Arial 10'), bg="white", command=EnrollStudent)
	AdmitStudent.place(x=220, y=390)

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











root.mainloop()