from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas
#functionality Part

def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable1.get_children()
    newlist1=[]
    for index in indexing:
        content=studentTable1.item(index)
        datalist1=content['values']
        newlist1.append(datalist1)


    table1=pandas.DataFrame(newlist1,columns=['Id','Name','Mobile','Gpa','Internship','backlogs','Placements','Added Date','Added Time'])
    table1.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is saved succesfully')


def toplevel_data(title,button_text,command):
    global idEntry,phoneEntry,nameEntry,GpaEntry,InternshipEntry,backlogsEntry,PlacementsEntry,screen
    screen = Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(False, False)
    idLabel = Label(screen, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(screen, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(screen, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    GpaLabel = Label(screen, text='Gpa', font=('times new roman', 20, 'bold'))
    GpaLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    GpaEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    GpaEntry.grid(row=3, column=1, pady=15, padx=10)

    InternshipLabel = Label(screen, text='Internship', font=('times new roman', 20, 'bold'))
    InternshipLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    InternshipEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    InternshipEntry.grid(row=4,column=1,pady=15, padx=10)

    backlogsLabel = Label(screen, text='backlogs', font=('times new roman', 20, 'bold'))
    backlogsLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    backlogsEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    backlogsEntry.grid(row=5, column=1, pady=15, padx=10)

    PlacementsLabel = Label(screen, text='Placements', font=('times new roman', 20, 'bold'))
    PlacementsLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    PlacementsEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    PlacementsEntry.grid(row=6, column=1, pady=15, padx=10)

    student1_button = ttk.Button(screen, text=button_text, command=command)
    student1_button.grid(row=7, columnspan=2, pady=15)
    if title=='Update Student1':
        indexing = studentTable1.focus()

        content = studentTable1.item(indexing)
        listdata1 = content['values']
        idEntry.insert(0, listdata1[0])
        nameEntry.insert(0, listdata1[1])
        phoneEntry.insert(0, listdata1[2])
        Entry.insert(0, listdata1[3])
        InternshipEntry.insert(0, listdata1[4])
        backlogsEntry.insert(0, listdata1[5])
        PlacementsEntry.insert(0, listdata1[6])


def update_data():
    query='update student set name=%s,mobile=%s,Gpa=%s,Internship=%s,backlogs=%s,Placements=%s,date=%s,time=%s where id=%s'
    mycursor.execute(query,(nameEntry.get(),phoneEntry.get(),GpaEntry.get(),InternshipEntry.get(),
                            backlogsEntry.get(),PlacementsEntry.get(),date,currenttime,idEntry.get()))
    con.commit()
    messagebox.showinfo('Success',f'Id {idEntry.get()} is modified successfully',parent=screen)
    screen.destroy()
    show_student()



def show_student():
    query = 'select * from student1'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable1.delete(*studentTable1.get_children())
    for data in fetched_data:
        studentTable1.insert('', END, values=data)



def delete_student():
    indexing=studentTable1.focus()
    print(indexing)
    content=studentTable1.item(indexing)
    content_id=content['values'][0]
    query='delete from student1 where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted succesfully')
    query='select * from student1'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable1.delete(*studentTable1.get_children())
    for data in fetched_data:
        studentTable1.insert('',END,values=data)




def search_data():
    query='select * from student1 where id=%s or name=%s or Gpa=%s or mobile=%s or Internship=%s or backlogs=%s or Placements=%s'
    mycursor.execute(query,(idEntry.get(),nameEntry.get(),GpaEntry.get(),phoneEntry.get(),InternshipEntry.get(),backlogsEntry.get(),PlacementsEntry.get()))
    studentTable1.delete(*studentTable1.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        studentTable1.insert('',END,values=data)




def add_data():
    if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or GpaEntry.get()=='' or InternshipEntry.get()=='' or backlogsEntry.get()=='' or Placementsget()=='':
        messagebox.showerror('Error','All Feilds are required',parent=screen)

    else:
        try:
            query='insert into student1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),GpaEntry.get(),InternshipEntry.get(),
                                    backlogsEntry.get(),PlacementsEntry.get(),date,currenttime))
            con.commit()
            result=messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?',parent=screen)
            if result:
                idEntry.delete(0,END)
                nameEntry.delete(0,END)
                phoneEntry.delete(0,END)
                GpaEntry.delete(0,END)
                InternshipEntry.delete(0,END)
                backlogsEntry.delete(0,END)
                PlacementsEntry.delete(0,END)
            else:
                pass
        except:
            messagebox.showerror('Error','Id cannot be repeated',parent=screen)
            return


        query='select *from student1'
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        studentTable1.delete(*studentTable1.get_children())
        for data in fetched_data:
            studentTable1.insert('',END,values=data)


def connect_database():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host='localhost',user='root',password='1234')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return

        try:
            query='create database studentmanagementsystem1'
            mycursor.execute(query)
            query='use studentmanagementsystem1'
            mycursor.execute(query)
            query='create table student1(id int not null primary key, name varchar(30),mobile varchar(10),Gpa varchar(30),' \
                  'Internship varchar(100),backlogs varchar(20),Placements varchar(20),date varchar(50), time varchar(50))'
            mycursor.execute(query)
        except:
            query='use studentmanagementsystem1'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection is successful', parent=connectWindow)
        connectWindow.destroy()
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)


    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)

    usernameEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)

count=0
text=''
def slider():
    global text,count
    # if count==len(s):
    #     count=0
    #     text=''
    text=text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(300,slider)




def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000,clock)



#GUI Part
root=ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')

root.geometry('1174x680+0+0')
root.resizable(0,0)
root.title('Student Record System(Academic info)')

datetimeLabel=Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
s='Student Record System(Academic info)' #s[count]=t when count is 1
sliderLabel=Label(root,font=('arial',28,'italic bold'),width=30)
sliderLabel.place(x=200,y=0)
slider()

connectButton=ttk.Button(root,text='Connect database',command=connect_database)
connectButton.place(x=980,y=0)

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='student.png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=lambda :toplevel_data('Add Student','Add',add_data))
addstudentButton.grid(row=1,column=0,pady=20)

searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=25,state=DISABLED,command=lambda :toplevel_data('Search Student','Search',search_data))
searchstudentButton.grid(row=2,column=0,pady=20)

deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=25,state=DISABLED,command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=20)

updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=25,state=DISABLED,command=lambda :toplevel_data('Update Student','Update',update_data))
updatestudentButton.grid(row=4,column=0,pady=20)

showstudentButton=ttk.Button(leftFrame,text='Show Student',width=25,state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)

exportstudentButton=ttk.Button(leftFrame,text='Export data',width=25,state=DISABLED,command=export_data)
exportstudentButton.grid(row=6,column=0,pady=20)

exitButton=ttk.Button(leftFrame,text='Exit',width=25,command=iexit)
exitButton.grid(row=7,column=0,pady=20)

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable1=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile','Gpa','Internship','backlogs',
                                 'Placements','Added Date','Added Time'),
                          xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable1.xview)
scrollBarY.config(command=studentTable1.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

studentTable1.pack(expand=1,fill=BOTH)
studentTable1.heading('Id',text='Id')
studentTable1.heading('Name',text='Name')
studentTable1.heading('Mobile',text='Mobile No')
studentTable1.heading('Gpa',text='Gpa')
studentTable1.heading('Internship',text='Internship')
studentTable1.heading('backlogs',text='backlogs')
studentTable1.heading('Placements',text='Placements')
studentTable1.heading('Added Date',text='Added Date')
studentTable1.heading('Added Time',text='Added Time')

studentTable1.column('Id',width=50,anchor=CENTER)
studentTable1.column('Name',width=200,anchor=CENTER)
studentTable1.column('Gpa',width=300,anchor=CENTER)
studentTable1.column('Mobile',width=200,anchor=CENTER)
studentTable1.column('Internship',width=300,anchor=CENTER)
studentTable1.column('backlogs',width=100,anchor=CENTER)
studentTable1.column('Placements',width=200,anchor=CENTER)
studentTable1.column('Added Date',width=200,anchor=CENTER)
studentTable1.column('Added Time',width=200,anchor=CENTER)

style=ttk.Style()

style.configure('Treeview', rowheight=40,font=('arial', 12, 'bold'), fieldbackground='white', background='white',)
style.configure('Treeview.Heading',font=('arial', 14, 'bold'),foreground='red')

studentTable1.config(show='headings')

root.mainloop()
