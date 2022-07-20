from tkinter import*
root=Tk()

my_label=Label(root,text='Hello world I love python !!')

my_label.pack()

root.mainloop()


from tkinter import*
root=Tk()

root.title('MY BOX GUI')

# p1 = PhotoImage(file = "index1.png")
# root.iconphoto(False,p1)
# root.iconbitmap('test.ico')

my_label=Label(root,text="hi")
my_label2=Label(root,text="how do you doing?")

my_label.pack()
my_label2.pack()

root.mainloop()



from tkinter import*
root=Tk()


root.title("MY GUI APP")
# root.iconbitmap("star.ico")
root.geometry("500x500")


my_label=Label(root,text="MY NEW GUI APP!")
my_label2=Label(root,text="this is line 2")


my_label.grid(row=0,column=1)
my_label2.grid(row=0,column=2)


root.mainloop()



from tkinter import*                                                                                        
root=Tk()


root.title("MY BUTTON")
# root.iconbitmap("apple.ico")
root.geometry("500x500")


def my_click():
    my_label=Label(root,text="WELCOME TO THE COURSE!",fg="#3371FF")
    my_label.pack()

mybutton=Button(root,text="HEY CLICK THIS!",command = my_click,fg="red",bg="orange",padx=30,pady=30)
mybutton.pack()

root.mainloop()




from tkinter import*
root=Tk()


root.title("MY BUTTON")
# root.iconbitmap("apple.ico")
root.geometry("500x500")


e=Entry(root,width=50,fg="red")
e.grid(row=0,column=1)


ee=Entry(root,width=50,fg="black")
ee.grid(row=0,column=2)


def clickme():
    mylabel=Label(root,text="Hello"+'  '+e.get())
    mylabel.grid(row=5,column=1)
    e.delete(0,END)

def click2():
    mylabel=Label(root,text="Hello"+'  '+ee.get())
    mylabel.grid(row=5,column=2)
    ee.delete(0,END)

mybutton=Button(root,text="ENTER YOUR FIRST NAME",padx=10,pady=10,bg="white",fg="red",command=clickme)
mybutton.grid(row=3,column=1)

mybutton=Button(root,text="ENTER YOUR LAST NAME",padx=10,pady=10,bg="white",fg="red",command=click2)
mybutton.grid(row=3,column=2)


root.mainloop()

