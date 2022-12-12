
from tkinter import * 
from PIL import ImageTk
import tkinter.ttk as ttk 
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
import pymysql


root = Tk()
root.geometry("1280x720+0+0")
root.title("Staff Portal ")

def close():
	root.destroy()


def StaffPortal():


	def CreateCourse():
		CourseID = e_CourseID.get();
		CourseName = e_CourseName.get();
		TeacherID = e_TeacherID.get();
		TeacherUserName = e_TeacherUserName.get();	
		
		if (CourseID =="" or CourseName =="" or TeacherID =="" or TeacherUserName ==""):
			Messagebox.showerror("Course Creation", "All fields are required")
		else:
			con = mysql.connect(host="localhost", user="root", password="", database="educationapp")
			cursor = con.cursor()
			cursor.execute("insert into createcourse values ('"+ CourseID +"', '"+ CourseName +"', '"+ TeacherID +"', '"+ TeacherUserName +"')")
			cursor.execute("commit"); 

			e_CourseID.delete(0,'end')
			e_CourseName.delete(0,'end')
			e_TeacherID.delete(0,'end')
			e_TeacherUserName.delete(0,'end')
		
			#ShowUsersDetails()
			Messagebox.showinfo("Insert Status", "Course Added Successfully!")
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

	def StudentDue():
		Ref= e_FRef.get()
		StudentUserName = e_FStudentUserName.get();
		StudentID = e_FStudentID.get();
		Description= e_FDescription.get();
		Ammount= e_FAmmount.get();
		Deadline= e_FDeadline.get();

		if (Ref =="" or StudentID =="" or StudentUserName =="" or Description =="" or Ammount =="" or Deadline ==""):
			Messagebox.showerror("Student Due", "All fields are required")
		else:
			con = mysql.connect(host="localhost", user="root", password="", database="educationapp")
			cursor = con.cursor()
			cursor.execute("insert into studentdues values ('"+ Ref +"', '"+ StudentUserName +"', '"+ StudentID +"', '"+ Description +"', '"+ Ammount +"', '"+ Deadline +"')")
			cursor.execute("commit"); 

			e_FRef.delete(0, 'end')
			e_FStudentUserName.delete(0, 'end')
			e_FStudentID.delete(0, 'end')
			e_FDescription.delete(0, 'end')
			e_FAmmount.delete(0, 'end')
			e_FDeadline.delete(0, 'end')

			#ShowUsersDetails()
			Messagebox.showinfo("Finance Status", "Student Due Successfully Placed!")
			con.close();

	def RemoveStudent():

		CourseID= e_SCourseID.get()
		StudentID = e_SStudentID.get();
		StudentUserName = e_SStudentUserName.get();

		if (CourseID =="" or StudentID =="" or StudentUserName ==""):
			Messagebox.showerror("Remove Status", "All fields are required")
		else:
			con = mysql.connect(host="localhost", user="root", password="", database="educationapp")
			cursor = con.cursor()
			cursor.execute("delete from coursestudents where CourseID=%s and StudentUserName = %s",(e_SCourseID.get(), e_SStudentUserName.get()))
			cursor.execute("commit"); 
			
			e_SCourseID.delete(0,'end')
			e_SStudentID.delete(0,'end')
			e_SStudentUserName.delete(0,'end')


			#ShowUsersDetails()

			Messagebox.showinfo("Insert Status", "Student dropped from the Course Successfully!")
			con.close();

	def UpdateUser():
		Serial = e_Serial.get();
		Name = e_Name.get();
		UserName = e_UserName.get();
		UserType = e_UserType.get()
		Email = e_Email.get();
		Mobile = e_Mobile.get();
		Address = e_Address.get();
		Gender = e_Gender.get();
		PassWord = e_PassWord.get();

		if (Serial =="" or Name =="" or UserName =="" or UserType =="" or Email=="" or Mobile =="" or Address =="" or Gender =="" or PassWord =="" ):
			Messagebox.showinfo("Update Status", "Complete the fields")
		else:
			con = mysql.connect(host="localhost", user="root", password="", database="educationapp")
			cursor = con.cursor()
			cursor.execute("update user set Serial= '"+ Serial +"', Name='"+ Name +"', UserType= '"+ UserType +"', Email= '"+ Email +"', Mobile= '"+ Mobile +"', Address = '"+ Address +"', Gender = '"+ Gender +"', PassWord= '"+ PassWord +"' where UserName= '"+ UserName +"'")
			cursor.execute("commit"); 

			e_Serial.delete(0,'end')
			e_Name.delete(0,'end')
			e_UserName.delete(0,'end')
			e_UserType.delete(0,'end')
			e_Email.delete(0,'end')
			e_Mobile.delete(0,'end')
			e_Address.delete(0,'end')
			e_Gender.delete(0,'end')
			e_PassWord.delete(0,'end')



			ShowUsersDetails()
			Messagebox.showinfo("Insert Status", "Updated Successfully!")
			con.close();

	def SearchUser():
		if (e_UserName.get()==""):
			Messagebox.showinfo("Search Status", "UserName Required!")
		else:
			con = mysql.connect(host="localhost", user="root", password="", database="educationapp")
			cursor = con.cursor()
			cursor.execute("select * from user where UserName = '"+ e_UserName.get() +"'")
			rows = cursor.fetchall()

			for row in rows:
				e_Serial.insert(0, row[0])
				e_Name.insert(0, row[1])
				e_UserName.insert(0,row[2])
				e_UserType.insert(0, row[3])
				e_Email.insert(0, row[4])
				e_Mobile.insert(0, row[5])
				e_Address.insert(0, row[6])
				e_Gender.insert(0, row[7])
				e_PassWord.insert(0, row[8])

			con.close();

	def ShowUsersDetails():
		con = mysql.connect(host="localhost", user="root", password="", database="educationapp")
		cursor = con.cursor()
		cursor.execute("select * from user")
		rows = cursor.fetchall()
		list.delete(0, list.size())

		for row in rows:
			insertData =str(row[0])+ '      '+ row[1] + '      '+ row[2]+ '      '+ row[3]
			list.insert(list.size()+1, insertData)
		con.close()



	SHeadingCourse = Label(root, text='	Course Control', font=('bold', 14))
	SHeadingCourse.place(x=20, y=20)


	SCourseID = Label(root, text='CourseID', font=('bold', 10))
	SCourseID.place(x=20, y=60)

	e_CourseID = Entry(width=30,font=('Arial 10'))
	e_CourseID.place (x=150, y=60)


	SCourseName = Label(root, text='Course Name', font=('bold', 10))
	SCourseName.place(x=20, y=90)

	e_CourseName = Entry(width=30,font=('Arial 10'))
	e_CourseName.place (x=150, y=90)


	STeacherID = Label(root, text='Teacher ID', font=('bold', 10))
	STeacherID.place(x=20, y=120)

	e_TeacherID = Entry(width=30,font=('Arial 10'))
	e_TeacherID.place (x=150, y=120)


	STeacherUserName = Label(root, text='Teacher User Name', font=('bold', 10))
	STeacherUserName.place(x=20, y=150)
	
	e_TeacherUserName = Entry(width=30,font=('Arial 10'))
	e_TeacherUserName.place (x=150, y=150)

	AddCourse = Button(root, text="Add Course", font=('Arial 10'), bg="white", command=CreateCourse)
	AddCourse.place(x=180, y=190)


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

	DropStudent = Button(root, text="Drop Student", font=('Arial 10'), bg="white", command=RemoveStudent)
	DropStudent.place(x=80, y=390)


	#Student Finance (Add Dues)


	FRef = Label(root, text='Reference No.', font=('bold', 10))
	FRef.place(x=450, y=50)

	e_FRef= Entry(width=30,font=('Arial 10'))
	e_FRef.place (x=580, y=50)


	FStudentUserName = Label(root, text='Student User Name', font=('bold', 10))
	FStudentUserName.place(x=450, y=80)

	e_FStudentUserName = Entry(width=30,font=('Arial 10'))
	e_FStudentUserName.place (x=580, y=80)


	FStudentID = Label(root, text='Student ID', font=('bold', 10))
	FStudentID.place(x=450, y=110)
	
	e_FStudentID = Entry(width=30,font=('Arial 10'))
	e_FStudentID.place (x=580, y=110)


	FDescription = Label(root, text='Description', font=('bold', 10))
	FDescription.place(x=450, y=140)
	
	e_FDescription = Entry(width=30,font=('Arial 10'))
	e_FDescription.place (x=580, y=140)


	FAmount = Label(root, text='Amount', font=('bold', 10))
	FAmount.place(x=450, y=170)
	
	e_FAmmount = Entry(width=30,font=('Arial 10'))
	e_FAmmount.place (x=580, y=170)


	FDeadline = Label(root, text='Deadline', font=('bold', 10))
	FDeadline.place(x=450, y=200)
	
	e_FDeadline = Entry(width=30,font=('Arial 10'))
	e_FDeadline.place (x=580, y=200)


	StudentFinance = Button(root, text="Student Finance", font=('Arial 10'), bg="white", command=StudentDue)
	StudentFinance.place(x=580, y=240)



StaffPortal()
root.mainloop()












