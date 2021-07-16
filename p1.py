from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import matplotlib.pyplot as plt
import bs4
import requests



def f1():
	add_window.deiconify()
	main_window.withdraw()
def f2():
	main_window.deiconify()
	add_window.withdraw()

def f3():
	con = None
	try:
		con = connect("stu.db")
		cursor = con.cursor()
		sql = "insert into student values('%d', '%s', '%d')"
		rno = int(add_window_ent_rno.get())
		if (rno <= 0):
			raise Exception("Enter Positive Integers Only")
		name = add_window_ent_name.get()
		if (len(name) < 2) or (not name.isalpha()):
			raise Exception("invalid name ")
		marks = int(add_window_ent_marks.get())
		if (marks < 0) or (marks > 100):
			raise Exception("invalid marks ")
		cursor.execute(sql % (rno, name, marks))
		con.commit()
		showinfo('success', 'record added')
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
		add_window_ent_rno.focus()

	except ValueError:
		showerror("Failure","rno and marks should be positive integer only ")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
		add_window_ent_rno.focus()

	except Exception as e:
		showerror('Failure', e)
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
		add_window_ent_rno.focus()
		con.rollback()
	finally:
		if con is not None:
			con.close()

def f4():
	view_window.deiconify()
	main_window.withdraw()
	view_window_st_data.delete(1.0, END)
	info = ""
	con = None
	try:	
		con = connect("stu.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		for d in data:	
			info = info + "rno: " + str(d[0]) + " name: "  + str(d[1]) + " marks: " + str(d[2]) + "\n\n"
		print(info)
		view_window_st_data.insert(INSERT, info)
	except Exception as e:
		showerror("Failure", e)
	finally: 
		if con is not None:
			con.close()

def f5():
	main_window.deiconify()
	view_window.withdraw()

def f6():
	update_window.deiconify()
	main_window.withdraw()

def f7():
	main_window.deiconify()
	update_window.withdraw()
def f8():
	con = None
	try:
		con = connect("stu.db")
		cursor = con.cursor()
		sql = "update student set name='%s', marks='%d' where rno='%d'"
		rno = int(update_window_ent_rno.get())
		if (rno <= 0):
			raise Exception("rno should be positive integer only")
		name = update_window_ent_name.get()
		if (len(name) < 2) or (not name.isalpha()):
			raise Exception("invalid name ")
		marks = int(update_window_ent_marks.get())
		if (marks < 0) or (marks > 100):
			raise Exception("invalid marks ")
		cursor.execute(sql % (name, marks, rno))
		if cursor.rowcount > 0:
			showinfo("success record updated")
			con.commit()
		else:
			showinfo("record does not exists")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
		update_window_ent_rno.focus()

	except ValueError:
		showerror("Failure","rno and marks should be positive integer only ")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
		update_window_ent_rno.focus()
		
		
	except Exception as e:
		showerror("Failure", e)
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
		update_window_ent_rno.focus()
		
		con.rollback()
	finally:
		if con is not None:
			con.close()
			

def f9():
	delete_window.deiconify()
	main_window.withdraw()

def f10():
	main_window.deiconify()
	delete_window.withdraw()

def f11():
	con = None
	try:
		con = connect("stu.db")
		cursor = con.cursor()
		sql = "delete from student where rno='%d'"
		rno = int(delete_window_ent_rno.get())
		if (rno <= 0):
			raise Exception("rno should be positive integer only")
		cursor.execute(sql % (rno))
		if cursor.rowcount > 0:
			showinfo("record deleted ")
			con.commit()
		else:
			showerror("record does not exists")
		delete_window_ent_rno.delete(0, END)
		delete_window_ent_rno.focus()

	except ValueError:
		showerror("Failure","rno should be postive integer only ")
		delete_window_ent_rno.delete(0, END)
		delete_window_ent_rno.focus()
	except Exception as e:
		showerror("Failure ", e)
		delete_window_ent_rno.delete(0, END)
		delete_window_ent_rno.focus()
		con.rollback()
	finally:
		if con is not None:
			con.close()

def f12():
	
	con = None
	try:	
		con = connect("stu.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchone()
		name = []
		marks = []
		while data:
			marks.append(data[2])
			name.append(data[1])
			data=cursor.fetchone()
		color_list=["red","green","blue","orange","pink","purple"]
		plt.bar(name,marks,color=color_list)
		plt.title("Batch Information!")
		plt.xlabel("Name")
		plt.ylabel("Marks")
		plt.show()
			
	
		
	except Exception as e:
		print("issue", e)
	finally:
		if con is not None:
			con.close()


def f13():
	try:
		wa = "https://ipinfo.io/"
		res = requests.get(wa)

		data = res.json()
		city_name = data['city']
		
	
		loc = data['loc']
		
	
		a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
		a2 = "&q=" + city_name
		a3 = "&appid=" +  "c6e315d09197cec231495138183954bd"

		wa = a1 + a2 + a3
		res = requests.get(wa)
	

		data = res.json()
		

		main = data['main']
		temp = main['temp']
	

		wa = "https://www.brainyquote.com/quote_of_the_day"
		res = requests.get(wa)
	
		
		data = bs4.BeautifulSoup(res.text, 'html.parser')

		info = data.find('img', {'class':'p-qotd'})	

		
		msg = info['alt']
		
		
		main_window_lbl1['text'] = 'Location:', city_name,   'Temp:'   , temp
		main_window_lbl2['text'] = 'QOTD:' +  str(msg)	
		
	except Exception as e:
		print("issue ", e)






main_window = Tk()
main_window.title("S.M.S")
main_window.geometry("430x500+450+100")


main_window_btn_add = Button(main_window, text="Add", font=('Arial', 20, 'bold'), width=10, command=f1)
main_window_btn_view = Button(main_window, text="View", font=('Arial', 20, 'bold'), width=10, command=f4)
main_window_btn_update = Button(main_window, text="Update", font=('Arial', 20, 'bold'), width=10, command=f6)
main_window_btn_delete = Button(main_window, text="Delete", font=('Arial', 20, 'bold'), width=10, command=f9)
main_window_btn_charts = Button(main_window, text="Charts", font=('Arial', 20, 'bold'), width=10, command=f12)
main_window_lbl1 = Label(main_window, font=('Arial', 20, 'bold' ), bd=2, relief='solid' )
main_window_lbl2 = Label(main_window, font=('Arial', 20, 'bold' ), bd=2, relief='solid')


main_window_btn_add.pack(pady=10)
main_window_btn_view.pack(pady=10)
main_window_btn_update.pack(pady=10)
main_window_btn_delete.pack(pady=10)
main_window_btn_charts.pack(pady=10)
main_window_lbl1.pack(padx=5, pady=10)
main_window_lbl2.pack(padx=10, pady=10)
f13()


	



add_window = Toplevel(main_window)
add_window.title("Add St.")
add_window.geometry("500x500+400+100")

add_window_lbl_rno = Label(add_window, text="enter rno:", font=('Arial', 20, 'bold'))
add_window_ent_rno = Entry(add_window, bd=5, font=('Arial', 20, 'bold'))
add_window_lbl_name = Label(add_window, text="enter name:", font=('Arial', 20, 'bold'))
add_window_ent_name = Entry(add_window, bd=5, font=('Arial', 20, 'bold'))
add_window_lbl_marks = Label(add_window, text="enter marks:", font=('Arial', 20, 'bold'))
add_window_ent_marks = Entry(add_window, bd=5, font=('Arial', 20, 'bold'))
add_window_btn_save = Button(add_window, text="Save", width=10, font=('Arial', 20, 'bold'),command=f3)
add_window_btn_back = Button(add_window, text="Back", width=10, font=('Arial', 20, 'bold'), command=f2)

add_window_lbl_rno.pack(pady=10)
add_window_ent_rno.pack(pady=10)
add_window_lbl_name.pack(pady=10)
add_window_ent_name.pack(pady=10)
add_window_lbl_marks.pack(pady=10)
add_window_ent_marks.pack(pady=10)
add_window_btn_save.pack(pady=10)
add_window_btn_back.pack(pady=10)
add_window.withdraw()

view_window = Toplevel(main_window)
view_window.title("View St.")
view_window.geometry("500x500+400+100")

view_window_st_data = ScrolledText(view_window, width=30, height=10, font=('Arial', 20, 'bold'))
view_window_btn_back = Button(view_window, text="Back", font=('Arial', 20, 'bold'), command=f5)
view_window_st_data.pack(pady=10)
view_window_btn_back.pack(pady=10)
view_window.withdraw()

update_window = Toplevel(main_window)
update_window.title("Update St.")
update_window.geometry("500x500+400+100")

update_window_lbl_rno = Label(update_window, text="enter rno:", font=('Arial',20,'bold'))
update_window_ent_rno = Entry(update_window, bd=5, font=('Arial',20,'bold'))
update_window_lbl_name = Label(update_window, text="enter name:", font=('Arial',20,'bold'))
update_window_ent_name = Entry(update_window, bd=5, font=('Arial',20,'bold'))
update_window_lbl_marks = Label(update_window, text="enter marks:", font=('Arial',20,'bold'))
update_window_ent_marks = Entry(update_window, bd=5, font=('Arial',20,'bold'))
update_window_btn_save = Button(update_window, text="Save", font=('Arial', 20, 'bold'), width=10, command=f8)
update_window_btn_back = Button(update_window, text="Back", font=('Arial', 20, 'bold'), width=10, command=f7) 


update_window_lbl_rno.pack(pady=10)
update_window_ent_rno.pack(pady=10)
update_window_lbl_name.pack(pady=10)
update_window_ent_name.pack(pady=10)
update_window_lbl_marks.pack(pady=10)
update_window_ent_marks.pack(pady=10)
update_window_btn_save.pack(pady=10)
update_window_btn_back.pack(pady=10)
update_window.withdraw()

delete_window = Toplevel(main_window)
delete_window.title("Delete St.")
delete_window.geometry("500x500+400+100")

delete_window_lbl_rno = Label(delete_window, text="enter rno:", font=('Arial', 20, 'bold'))
delete_window_ent_rno = Entry(delete_window, bd=5, font=('Arial', 20, 'bold'))
delete_window_btn_save = Button(delete_window, text="Save", font=('Arial', 20, 'bold'), width=10, command=f11)
delete_window_btn_back = Button(delete_window, text="Back", font=('Arial', 20, 'bold'), width=10, command=f10)

delete_window_lbl_rno.pack(pady=10)
delete_window_ent_rno.pack(pady=10)
delete_window_btn_save.pack(pady=10)
delete_window_btn_back.pack(pady=10)
delete_window.withdraw()



main_window.mainloop()