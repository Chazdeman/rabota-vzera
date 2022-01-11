from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np

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
n=0
D=-1
t="Нет решения!"

def open_win():
    def rrr():
        global a,D,b,c,t
        graf=""
        if (a.get()!="" and b.get()!="" and c.get()!=""):
            if (float(a.get())==0 and float(b.get())==0 and float(c.get())==0):
                vastus.configure(text=f"Ошибка!")
                a.configure(bg="red")
                b.configure(bg="red")
                c.configure(bg="red")
                graf=False
            elif float(a.get())==0 and float(b.get())!=0 and float(c.get())!=0:
                vastus.configure(text=f"Ошибка!")
                a.configure(bg="red")
                b.configure(bg="#03ecfc")
                c.configure(bg="#03ecfc")
                graf=False
            elif float(a.get())!=0 and float(b.get())==0 and float(c.get())!=0:
                vastus.configure(text=f"Ошибка!")
                b.configure(bg="red")
                a.configure(bg="#03ecfc")
                c.configure(bg="#03ecfc")
                graf=False
            elif float(a.get())!=0 and float(b.get())!=0 and float(c.get())==0:
                vastus.configure(text=f"Ошибка!")
                c.configure(bg="red")
                b.configure(bg="#03ecfc")
                a.configure(bg="#03ecfc")
                graf=False
            elif float(a.get())!=0 and float(b.get())!=0 and float(c.get())!=0:
                a_=float(a.get())
                b_=float(b.get())
                c_=float(c.get())
                D=b_*b_-4*a_*c_
                if D > 0:
                    x1_=round((-1*b_+sqrt(D))/(2*a_),2)
                    x2_=round((-1*b_-sqrt(D))/(2*a_),2)
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
        return graf,D,t
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
    global a,b,c
    t=0
    def veel():
        global t
        if t==0:
            win.geometry(str(win.winfo_width())+"x"+str(win.winfo_height()-200))
            btn_veel.config(text="Уменьшить окно")
            t=1
        else:
            win.geometry(str(win.winfo_width())+"x"+str(win.winfo_height()+200))
            btn_veel.config(text="Увеличить окно")
            t=0
    win=Toplevel()#создаём второе(дочернее) окно Tk делает главную Toplevel делает вторую
    win.geometry("1000x500")
    win.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
    win.configure(bg="#A9A9A9")
    #f1=Frame(win,width=500,height=200)
    #f1.pack(side=TOP)
    #f2=Frame(win,width=500,height=200)
    #f2.pack(side=BOTTOM)
    lbl=Label(win,text="Решение квадратного уравнения", height=4,width=30, font="Arial 20",fg="black", bg="pink")
    lbl.pack()
    btn_veel=Button(win,text="Увеличить окно",font="Calibri 26",bg="green",command=veel)
    btn_veel.pack(side=BOTTOM)
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
    lbl4.pack(side=LEFT)#Nikita
    win.mainloop()

def open_win2():
    def ket():
        x1 = np.arange(0, 9.5, 1)#min max step
        y1=(2/27)*x1*x1-3
        x2 = np.arange(-10, 0.5, 1)#min max step
        y2=0.04*x2*x2-3
        x3 = np.arange(-9, -2.5, 1)#min max step
        y3=(2/9)*(x3+6)**2+1
        x4 = np.arange(-3, 9.5, 1)#min max step
        y4=(-1/12)*(x4-3)**2+6
        x5 = np.arange(5, 8.8  , 1)#min max step
        y5=(1/9)*(x5-5)**2+2
        x6 = np.arange(5, 9 , 1)#min max step
        y6=(1/8)*(x6-7)**2+1.5
        x7 = np.arange(-13, -8.5 , 1)#min max step
        y7=(-0.75)*(x7+11)**2+6
        x8 = np.arange(-15, -12.5 , 1)#min max step
        y8=(-0.5)*(x8+13)**2+3
        x9 = np.arange(-15, -9.5 , 1)#min max step
        y9=[1]*len(x9)
        x10 = np.arange(3, 4.5 , 1)#min max step
        y10=[3]*len(x10)
        fig = plt.figure()
        plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
        plt.title('КИТ')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
    def ochi():
        x1 = np.arange(-9,-0.5, 0.5)#min max step
        y1=(-1/16)*(x1+5)**2+2
        x2 = np.arange(1,9.5, 0.5)#min max step
        y2=(-1/16)*(x2-5)**2+2
        x3 = np.arange(-9,-0.5, 0.5)#min max step
        y3=(1/4)*(x3+5)**2-3
        x4 = np.arange(1,9.5, 0.5)#min max step
        y4=(1/4)*(x4-5)**2-3
        x5 = np.arange(-9,-5.5  , 0.5)#min max step
        y5=-(x5+7)**2+5
        x6 = np.arange(6,9.5 , 0.5)#min max step
        y6=-(x6-7)**2+5
        x7 = np.arange(-1, 1.5 , 0.5)#min max step
        y7=(-0.5)*x7*x7+1.5
        fig = plt.figure()
        plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
        plt.title('ОЧКИ')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()      
    def vibor():
        viber=var.get()
        lbl.configure(text=viber)
    win2=Toplevel()#создаём второе(дочернее) окно Tk делает главную Toplevel делает вторую
    win2.geometry("1000x500")
    win2.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
    win2.configure(bg="#A9A9A9")
    lbl=Label(win2,text="!Ф-И-Г-У-Р-Ы!", height=4, width=20, font="Arial 20", fg="black", bg="pink")
    var=StringVar()
    var.set("ODIN")
    r1=Radiobutton(win2,text="Кит",height=3, width=6, font="Arial 20", fg="black", bg="green" , variable=var,value="kala", command=ket)
    r2=Radiobutton(win2,text="Зонтик",height=3, width=6, font="Arial 20", fg="black", bg="green" ,variable=var,value="Зонтик")
    r3=Radiobutton(win2,text="Лягушка",height=3, width=6, font="Arial 20", fg="black", bg="green" ,variable=var,value="Лягуха",)
    r4=Radiobutton(win2,text="Очки",height=3, width=6, font="Arial 20", fg="black", bg="green" ,variable=var,value="Очки", command=ochi)
    lbl.pack()
    r1.pack(side=TOP)
    r2.pack(side=LEFT)
    r3.pack(side=RIGHT)
    r4.pack(side=BOTTOM)
def cmd1():
    print("Exit . . . ")
    aken.destroy()
def cmd2():
    print("Toplevel")
    aken.command=open_win()
def cmd3():
    print("TOPLEVEL")
    aken.command=open_win2()

anim(0,0,"В Ы Х О Д","#ffcc66","white",cmd1)
anim(0,37,"Р Е Ш Е Н И Е","#f86263","white", cmd2)
anim(0,74, "Ф И Г У Р А", "#f86263","white", cmd3)
#canvas=Canvas(aken,width=600,height=300)
#canvas.grid(columnspan=3)


aken.mainloop()