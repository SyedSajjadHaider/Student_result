from tkinter import *

#---click function defination-------
def click():
    txt1 = text_entry1.get() # collect text from variable text_entry to txt
    txt2 = text_entry2.get() # collect text from variable text_entry to txt
    txt3 = text_entry3.get() # collect text from variable text_entry to txt
    txt4 = text_entry4.get() # collect text from variable text_entry to txt

    lst = [txt1,txt2,txt3,txt4]
    print(txt1,"\t",txt2,"\t",txt3,"\t",txt4)

    #pass_data(lst)
     #   pass
#----------------------------------

#----------------main---------------
window = Tk()  # important line , it create a window
window.title("Student Result") # window title

#--------------LABLE 1 ----------
lb = Label(window,text="- - -Student Form- - -",bg="yellow",fg="black",font="none 12 bold")
lb.grid(row=1,column=0,sticky=S)

#-------------LABLE 2 -NAME OF STUDENT -----------
lb = Label(window,text="NAME",fg="black",font="none 10 bold")
lb.grid(row=2,column=0,sticky=S)
#------create a text entry box-----
text_entry1 = Entry(window,width=20,bg="white")
text_entry1.grid(row=3,column=0,sticky=S)


#-------------LABLE 3---CLASS OF STUDENT-----------
lb = Label(window,text="CLASS",fg="black",font="none 10 bold")
lb.grid(row=4,column=0,sticky=S)
#------create a text entry box-----
text_entry2 = Entry(window,width=20,bg="white")
text_entry2.grid(row=5,column=0,sticky=S)
#----------------------------------------------------


#-------------LABLE 4---ROLL NUMBER-----------
lb = Label(window,text="ROLL-NO",fg="black",font="none 10 bold")
lb.grid(row=6,column=0,sticky=S)
#------create a text entry box-----
text_entry3 = Entry(window,width=20,bg="white")
text_entry3.grid(row=7,column=0,sticky=S)
#----------------------------------------------------

#-------------LABLE 5---AGE-----------
lb = Label(window,text="AGE",fg="black",font="none 10 bold")
lb.grid(row=8,column=0,sticky=S)
#------create a text entry box-----
text_entry4 = Entry(window,width=20,bg="white")
text_entry4.grid(row=9,column=0,sticky=S)
#----------------------------------------------------



# add a submit button
# click is a  user defined function
b= Button(window,text="SUBMIT",width=6,command=click)
b.grid(row=10,column=0,sticky=S)

window.mainloop()
