from tkinter import *
from math import *

global a,d,b,c
aken=Tk()
aken.geometry("300x500")
aken.configure(bg="white")
aken.title("LOGITpv21")
def anim(x,y,text,bcolor,fcolor,cmd):
    def on_enter(e):
        mybutton["background"]=bcolor
        mybutton["foreground"]=fcolor
    def on_leave(e):
        mybutton["background"]=fcolor
        mybutton["foreground"]=bcolor
    mybutton=Button(aken,width=42, height=2,text=text,
                    fg=bcolor,
                    bg=fcolor,
                    border=0,
                    activeforeground=fcolor,
                    activebackground=bcolor,
                    command=cmd,)
    mybutton.bind("<Enter>", on_enter)
    mybutton.bind("<Leave>", on_leave)

    mybutton.place(x=x,y=y)

def open_win():
    def rrr():
        if (a.get()!="" and b.get()!="" and c.get()!=""):

            a_=float(a.get())
            b_=float(b.get())
            c_=float(c.get())
            D=b_*b_-4*a_*c_
            if D > 0:
                x1 = (-b + sqrt(d)) / (2 * a)
                x2 = (-b - sqrt(d)) / (2 * a)
                t=f"X1={x1_}, \nX2={x2_}"
                graf=True
            elif D == 0:
                x1_=round((-1*b_)/(2*a_),2)
                t=f"X1={x1_}"
                graf=True
            else:
                t="Корней нет"
                graf=False
            vastus.configure(text=f"D={D}\n{t}")
            a.configure(bg="#03ecfc")
            b.configure(bg="#03ecfc")
            c.configure(bg="#03ecfc")
        else:
            if a.get()=="":
                a.configure(bg="red")
            if b.get()=="":
                b.configure(bg="red")
            if c.get()=="":
                c.configure(bg="red")
def grafik():
    flag,D,t=rrr()
    if flag==True:
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x = np.arange(x0-10, x0+10, 0.5)#min max step
        y=a_*x*x+b_*x+c_
        fig = plt.figure()
        plt.plot(x, y,'b:o', x0, y0,'g-d')
        plt.title('Квадратное уравнение')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text=f"Вершина параболлы ({x0},{y0})"
    else:
        text=f"График нет возможности построить"
    vastus.configure(text=f"D={D}\n{t}\n{text}")
        return graf,D,t
    global a,b,c
    win=Toplevel()#создаём второе(дочернее) окно Tk делает главную Toplevel делает вторую
    win.geometry("1000x500")
    win.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
    win.configure(bg="#A9A9A9")
    lbl=Label(win,text="Решение квадратного уравнения", height=4,width=30, font="Arial 20",fg="black", bg="pink")
    lbl.pack()
    vastus=Label(win,text="Решение", height=4, width=40, font="Arial 20", fg="black", bg="pink")
    vastus.pack(side=BOTTOM)
    reh=Button(win,text="График",font="Times_New_Roman 20", fg="black" ,bg="green", height=4,width=15, command=grafik)
    reh.pack(side=RIGHT)
    reh=Button(win,text="Решение",font="Times_New_Roman 20", fg="black" ,bg="green", height=4,width=15, command=rrr)
    reh.pack(side=RIGHT)
    a=Entry(win,font="Times_New_Roman 30", width=3,fg="red", bg="#03ecfc",justify=RIGHT)
    a.pack(side=LEFT)
    lbl2=Label(win,text="x**2+", height=1, width=6, font="Arial 20", fg="black", bg="#A9A9A9")
    lbl2.pack(side=LEFT,padx=5,pady=5)
    b=Entry(win,font="Times_New_Roman 30", width=3,fg="red", bg="#03ecfc",justify=RIGHT)
    b.pack(side=LEFT)
    lbl3=Label(win,text="x+", height=1, width=6, font="Arial 20", fg="black", bg="#A9A9A9")
    lbl3.pack(side=LEFT)
    c=Entry(win,font="Times_New_Roman 30", width=3,fg="red", bg="#03ecfc",justify=RIGHT)
    c.pack(side=LEFT)
    lbl4=Label(win,text="=0", height=1, width=6, font="Arial 20", fg="black", bg="#A9A9A9")
    lbl4.pack(side=LEFT)

    win.mainloop()


def cmd1():
    print("Exit . . . ")
    aken.destroy()
def cmd2():
    print("Toplevel")
    aken.command=open_win()


anim(0,0,"В Ы Х О Д","#ffcc66","white",cmd1)
anim(0,37,"Р Е Ш Е Н И Е","#f86263","white", cmd2)

#canvas=Canvas(aken,width=600,height=300)
#canvas.grid(columnspan=3)


aken.mainloop()