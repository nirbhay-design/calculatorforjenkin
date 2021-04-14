# font=("Comic sans ms" ,25, "bold")
from tkinter import *
root = Tk()
root.title("my calculator")
root.geometry("444x535")
root.resizable(0,0)
def click(event):
    global screenval
    text = event.widget.cget("text")
    if text =="=":
        if screenval.get().isdigit():
            val = int(screenval.get())

        else:
            try:
                val = eval(screenval.get())
            except Exception as e:
                val=e
        screenval.set(val)
        screen.update()
    elif text == "C":
        screenval.set("")
        screen.update()

    elif text=="<=":
        screenval.set(screenval.get()[:-1])
        screen.update()
    else:
        screenval.set(screenval.get()+text)
        screen.update()


# to make the  buttons closeley packed we set the border to 0 and relief to groove 
frame = Frame(root,borderwidth=2,bg='grey')
frame.pack()
screenval= StringVar()
screenval.set("")
screen = Entry(master=frame,width=23,textvar=screenval,relief=GROOVE,font=("Comic sans ms" ,25, "bold"))
screen.pack(ipadx=10,ipady=10)

b=Button(frame,text='9',font=("Comic sans ms" ,25, "bold"),relief=GROOVE,width=5,bg='orange',fg="black")
b.pack(pady=5,padx=5,side=LEFT)
b.bind('<Button-1>',click)
b=Button(frame,text='8',font=("Comic sans ms" ,25, "bold"),relief=GROOVE,width=5,bg='orange',fg="black")
b.pack(pady=5,padx=5,side=LEFT)
b.bind('<Button-1>',click)
b=Button(frame,text='7',font=("Comic sans ms" ,25, "bold"),relief=GROOVE,width=5,bg='orange',fg="black")
b.pack(pady=5,padx=5,side=LEFT)
b.bind('<Button-1>',click)
b=Button(frame,text='C',font=("Comic sans ms" ,25, "bold"),relief=GROOVE,width=5,bg='orange',fg="black")
b.pack(pady=5,padx=5,side=LEFT)
b.bind('<Button-1>',click)

frame1 = Frame(root,borderwidth=4,bg='grey')
frame1.pack()
b=Button(frame1,text='6',font=("Comic sans ms" ,25, "bold"),relief=GROOVE,width=5,bg='orange',fg="black")
b.pack(pady=3,padx=5,side=LEFT)
b.bind('<Button-1>',click)
b=Button(frame1,text='5',font=("Comic sans ms" ,25, "bold"),relief=GROOVE,width=5,bg='orange',fg="black")
b.pack(pady=3,padx=5,side=LEFT)
b.bind('<Button-1>',click)
b=Button(frame1,text='4',font=("Comic sans ms" ,25, "bold"),relief=GROOVE,width=5,bg='orange',fg="black")
b.pack(pady=3,padx=5,side=LEFT)
b.bind('<Button-1>',click)
b=Button(frame1,text='-',font=("Comic sans ms" ,25, "bold"),relief=GROOVE,width=5,bg='orange',fg="black")
b.pack(pady=3,padx=5,side=LEFT)
b.bind('<Button-1>',click)

frame2 = Frame(root,borderwidth=4,bg='grey')
frame2.pack()
b=Button(frame2,text='3',font=("Comic sans ms" ,25, "bold"),relief=GROOVE,width=5,bg='orange',fg="black")
b.pack(pady=3,padx=5,side=LEFT)
b.bind('<Button-1>',click)
b=Button(frame2,text='2',font=("Comic sans ms" ,25, "bold"),relief=GROOVE,width=5,bg='orange',fg="black")
b.pack(pady=3,padx=5,side=LEFT)
b.bind('<Button-1>',click)
b=Button(frame2,text='1',font=("Comic sans ms" ,25, "bold"),relief=GROOVE,width=5,bg='orange',fg="black")
b.pack(pady=3,padx=5,side=LEFT)
b.bind('<Button-1>',click)
b=Button(frame2,text='*',font=("Comic sans ms" ,25, "bold"),relief=GROOVE,width=5,bg='orange',fg="black")
b.pack(pady=3,padx=5,side=LEFT)
b.bind('<Button-1>',click)

frame3 = Frame(root,borderwidth=4,bg='grey')
frame3.pack()
b=Button(frame3,text='0',font=("Comic sans ms" ,25, "bold"),relief=GROOVE,width=5,bg='orange',fg="black")
b.pack(pady=3,padx=5,side=LEFT)
b.bind('<Button-1>',click)
b=Button(frame3,text='.',font=("Comic sans ms" ,25, "bold"),relief=GROOVE,width=5,bg='orange',fg="black")
b.pack(pady=3,padx=5,side=LEFT)
b.bind('<Button-1>',click)
b=Button(frame3,text='<=',font=("Comic sans ms" ,25, "bold"),relief=GROOVE,width=5,bg='orange',fg="black")
b.pack(pady=3,padx=5,side=LEFT)
b.bind('<Button-1>',click)
b=Button(frame3,text='+',font=("Comic sans ms" ,25, "bold"),relief=GROOVE,width=5,bg='orange',fg="black")
b.pack(pady=3,padx=5,side=LEFT)
b.bind('<Button-1>',click)

frame4 = Frame(root,borderwidth=4,bg='grey')
frame4.pack()
b=Button(frame4,text='/',font=("Comic sans ms" ,25, "bold"),relief=GROOVE,width=5,bg='orange',fg="black")
b.pack(pady=3,padx=5,side=LEFT)
b.bind('<Button-1>',click)
b=Button(frame4,text='%',font=("Comic sans ms" ,25, "bold"),relief=GROOVE,width=5,bg='orange',fg="black")
b.pack(pady=3,padx=5,side=LEFT)
b.bind('<Button-1>',click)
b=Button(frame4,text='=',font=("Comic sans ms" ,25, "bold"),relief=GROOVE,width=5,bg='orange',fg="black")
b.pack(pady=3,padx=5,side=LEFT)
b.bind('<Button-1>',click)
b=Button(frame4,text='//',font=("Comic sans ms" ,25, "bold"),relief=GROOVE,width=5,bg='orange',fg="black")
b.pack(pady=3,padx=5,side=LEFT)
b.bind('<Button-1>',click)

root.mainloop()