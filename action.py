from tkinter import * 
from PIL import ImageTk
import tkinter.ttk as ttk 
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
import pymysql


root = Tk()
root.geometry("1280x720+0+0")
root.title("Super Admin Portal ")

def close():
	root.destroy()

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
				#close()
				AdminPortal()
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


def AdminPortal():


	def InsertUser():
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
			Messagebox.showinfo("Insert Status", "All fields are required")
		else:
			con = mysql.connect(host="localhost", user="root", password="", database="educationapp")
			cursor = con.cursor()
			cursor.execute("insert into user values ('"+ Serial +"', '"+ Name +"', '"+ UserName +"', '"+ UserType +"', '"+ Email +"', '"+ Mobile +"', '"+ Address +"', '"+ Gender +"', '"+ PassWord +"')")
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
			Messagebox.showinfo("Insert Status", "User Added Successfully!")
			con.close();

	def DeleteUser():
		if (e_UserName.get()==""):
			Messagebox.showinfo("Insert Status", "UserName Required!")
		else:
			con = mysql.connect(host="localhost", user="root", password="", database="educationapp")
			cursor = con.cursor()
			cursor.execute("delete from user where UserName = '"+ e_UserName.get() +"'")
			cursor.execute("commit"); 
			e_UserName.delete(0,'end')


			ShowUsersDetails()

			Messagebox.showinfo("Insert Status", "User Deleted Successfully!")
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

	SHeadingReg = Label(root, text='Super Admin Portal: User Control System', font=('bold', 15))
	SHeadingReg.place(x=20, y=20)

	SSerial = Label(root, text='Serial No.', font=('bold', 10))
	SSerial.place(x=20, y=60)

	e_Serial = Entry(width=30,font=('Arial 10'))
	e_Serial.place (x=150, y=60)


	SName = Label(root, text='Name', font=('bold', 10))
	SName.place(x=20, y=90)

	e_Name = Entry(width=30,font=('Arial 10'))
	e_Name.place (x=150, y=90)


	SUserName = Label(root, text='Username', font=('bold', 10))
	SUserName.place(x=20, y=120)

	e_UserName = Entry(width=30,font=('Arial 10'))
	e_UserName.place (x=150, y=120)


	SUserType = Label(root, text='UserType', font=('bold', 10))
	SUserType.place(x=20, y=150)

	# UserOptions = ["Student","Teacher","Parent","Staff","Admin"] 
	#variable = StringVar(root)
	#variable.set(UserOptions[0])

	#e_UserType= OptionMenu(root, variable, *UserOptions)
	e_UserType = Entry(width=30,font=('Arial 10'))
	e_UserType.place (x=150, y=150)

	SEmail = Label(root, text='Email', font=('bold', 10))
	SEmail.place(x=20, y=180)

	e_Email = Entry(width=30,font=('Arial 10'))
	e_Email.place (x=150, y=180)


	SMobile = Label(root, text='Mobile', font=('bold', 10))
	SMobile.place(x=20, y=210)

	e_Mobile = Entry(width=30,font=('Arial 10'))
	e_Mobile.place (x=150, y=210)

	SAddress = Label(root, text='Address', font=('bold', 10))
	SAddress.place(x=20, y=240)

	e_Address = Entry(width=30,font=('Arial 10'))
	e_Address.place (x=150, y=240)


	SGender = Label(root, text='Gender', font=('bold', 10))
	SGender.place(x=20, y=270)

	#vars = IntVar()  
	#Radiobutton(root, text="Male",padx = 5, variable=vars, value="Male").place(x=150,y=270)  
	#Radiobutton(root, text="Female",padx = 20, variable=vars, value="Female").place(x=250,y=270)  
	  
	#e_Gender = str(vars.get())
	e_Gender = Entry(width=30,font=('Arial 10'))
	e_Gender.place(x=150, y=270)

	SPassWord = Label(root, text='Password', font=('bold', 10))
	SPassWord.place(x=20, y=300)

	e_PassWord = Entry(width=30,font=('Arial 10'))
	e_PassWord.place(x=150, y=300)


	AddUser = Button(root, text="Add User", font=('Arial 12'), bg="white", command=InsertUser)
	AddUser.place(x=180, y=350)

	DeleteUser = Button(root, text="Delete User", font=('Arial 12'), bg="white", command=DeleteUser)
	DeleteUser.place(x=180, y=390)

	UpdateUser = Button(root, text="Update User", font=('Arial 12'), bg="white", command=UpdateUser)
	UpdateUser.place(x=180, y=430)

	SearchUser = Button(root, text="Search User", font=('Arial 12'), bg="white", command=SearchUser)
	SearchUser.place(x=180, y=470)

	LogOut = Button(root, text="Exit", font=('Arial 12'), bg="white", command=close)
	LogOut.place(x=180, y =520)

	list = Listbox(root)
	list.place(x=500, y= 100)
	list.configure(background="yellow", foreground="black", font=('Aerial 13'), width=80, height=30)
	ShowUsersDetails()






root.mainloop()