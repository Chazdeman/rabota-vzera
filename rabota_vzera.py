
<<<<<<< HEAD
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
                c.configure(bg="#03ecfc")#1
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
    t=0
    def veel():
        global t
        if t==0:
            win2.geometry(str(win2.winfo_width())+"x"+str(win2.winfo_height()-200))
            btn_veel.config(text="Уменьшить окно")
            t=1
        else:
            win2.geometry(str(win2.winfo_width())+"x"+str(win2.winfo_height()+200))
            btn_veel.config(text="Увеличить окно")
            t=0
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
    def lagushka():
        x1 = np.arange(-7,7.5, 0.5)#min max step
        y1=(-3/49)*x1*x1+8
        x2 = np.arange(-7,7.5, 0.5)#min max step
        y2=(4/49)*x2*x2+1
        x3 = np.arange(-6.8,-1.5, 0.5)#min max step
        y3=(-0.75)*(x3+4)**2+11
        x4 = np.arange(2,7.3, 0.5)#min max step
        y4=(-0.75)*(x4-4)**2+11
        x5 = np.arange(-5.8,-2.3  , 0.5)#min max step
        y5=-(x5+4)**2+9
        x6 = np.arange(2.8, 6.3 , 0.5)#min max step
        y6=-(x6-4)**2+9
        x7 = np.arange(-4,4.5 , 0.5)#min max step
        y7=(4/9)*x7*x7-5
        x8 = np.arange(-5.2,5.7 , 0.5)#min max step
        y8=(4/9)*x8*x8-9
        x9 = np.arange(-7,-2.3 , 0.5)#min max step
        y9=(-1/16)*(x9+3)**2-6
        x10 = np.arange(2.8,7.5 , 0.5)#min max step
        y10=(-1/16)*(x10-3)**2-6
        x11 = np.arange(-7,0.5, 0.5)#min max step
        y11=(1/9)*(x11+4)**2-11
        x12 = np.arange(0, 7.5 ,0.5)#min max step
        y12=(1/9)*(x12-4)**2-11
        x13 = np.arange(-7,-4.0 ,0.5)#min max step
        y13=-(x13+5)**2
        x14 = np.arange(4.5 ,7.5 ,0.5)#min max step
        y14=-(x14-5)**2
        x15 = np.arange(-3, 3.5 ,0.5)#min max step
        y15=(2/9)*x15*x15+2
        fig = plt.figure()
        plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13,x14,y14,x15,y15)
        plt.title('КИТ')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
    def zontik():
        x1 = np.arange(-12, 12, 0.5)#min max step
        y1=(-1/18)*x1*x1+12
        x2 = np.arange(-4, 4, 0.5)#min max step
        y2=(-1/8)*x2*x2+6
        x3 = np.arange(-12, -4, 0.5)#min max step
        y3=(-1/8)*(x3+8)**2+6
        x4 = np.arange(4, 12, 0.5)#min max step
        y4=(-1/8)*(x4-8)**2+6
        x5 = np.arange(-4, -0.3 , 0.5)#min max step
        y5=2*(x5+3)**2-9
        x6 = np.arange(-4, 0.2 , 0.5)#min max step
        y6=1.5*(x6+3)**2-10

        fig = plt.figure()
        plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
        plt.title("umbrella")
        plt.ylabel("y")
        plt.xlabel("y")
        plt.grid(True)
        plt.show()

    def vibor():
        viber=var.get()
        lbl.configure(text=viber)
    win2=Toplevel()#создаём второе(дочернее) окно Tk делает главную Toplevel делает вторую
    win2.geometry("1000x500")
    win2.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
    win2.configure(bg="#A9A9A9")
    btn_veel=Button(win2,text="Увеличить окно",font="Calibri 26",bg="green",command=veel)
    lbl=Label(win2,text="!Ф-И-Г-У-Р-Ы!", height=4, width=20, font="Arial 20", fg="black", bg="pink")
    var=StringVar()
    var.set("ODIN")
    r1=Radiobutton(win2,text="Кит",height=3, width=6, font="Arial 20", fg="black", bg="green" , variable=var,value="kala", command=ket)
    r2=Radiobutton(win2,text="Зонтик",height=3, width=6, font="Arial 20", fg="black", bg="green" ,variable=var,value="Зонтик",command=zontik)
    r3=Radiobutton(win2,text="Лягушка",height=3, width=6, font="Arial 20", fg="black", bg="green" ,variable=var,value="Лягуха",command=lagushka)
    r4=Radiobutton(win2,text="Очки",height=3, width=6, font="Arial 20", fg="black", bg="green" ,variable=var,value="Очки", command=ochi)
    lbl.pack()
    btn_veel.pack(side=BOTTOM)
    r1.pack(side=LEFT)
    r2.pack(side=RIGHT)
    r3.pack(side=LEFT)
    r4.pack(side=RIGHT)


def open_formul():
    def vibor():
        viber=var.get()
        lbl.configure(text=viber)
    def vibor():
        viber=var.get()
        lbl.configure(text=viber)
    formul=Toplevel()#создаём второе(дочернее) окно Tk делает главную Toplevel делает вторую
    formul.geometry("1000x500")
    formul.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
    formul.configure(bg="#A9A9A9")
    var=StringVar()
    var.set("ODIN")
    r1=Radiobutton(formul,text="D=0",height=3, width=6, font="Arial 20", fg="black", bg="green" , variable=var,value="Один корень",command=vibor)
    r2=Radiobutton(formul,text="D>0",height=3, width=6, font="Arial 20", fg="black", bg="green" ,variable=var,value="Два корня",command=vibor)
    r3=Radiobutton(formul,text="D<0",height=3, width=6, font="Arial 20", fg="black", bg="green" ,variable=var,value="Нет корней",command=vibor)
    lbl=Label(formul,text="ax**2 + bx + c = 0\n D = b**2 − 4ac.", height=4, width=20, font="Arial 20", fg="black", bg="pink")
    r1.pack(side=BOTTOM)
    r2.pack(side=LEFT)
    r3.pack(side=RIGHT)
    lbl.pack()

    formul.mainloop()

def open_lizo():
    def lisa_nina():
        if var_nina.get()=="Nina":
            c.create_oval((225, 225, 275, 275), fill="#d44444", outline="#d44444") #нос
        elif var_nina.get()=="tühi":
            c.create_oval((225, 225, 275, 275), fill="#b58645", outline="#b58645") #нос
    def lisa_suu():
        if var_suu.get()=="Suu":
            c.create_arc((100, 300, 400,400),start=180,extent=180, style=ARC, fill="#d44478", outline="black",width=50)
            c.create_arc((100, 300, 400,400),start=180,extent=180, style=ARC, fill="red", outline="red",width=10)
        elif var_suu.get()=="tühi":
            c.create_arc((100, 300, 400,400),start=180,extent=180, style=ARC,   fill="#b58645", outline="#b58645",width=50)
    def lisa_eyes():
        if var_eyes.get()=="Silmad":
            c.create_oval((300, 100, 400, 200), fill="#050504", outline="black") 
            c.create_oval((375,175,325,125), fill="red", outline="black")
            c.create_oval((200, 200, 100, 100), fill="#050504", outline="black") 
            c.create_oval((125,125,175,175), fill="red", outline="black") 
        elif var_eyes.get()=="tühi":
            c.create_oval((300, 100, 400, 200),  fill="#b58645", outline="#b58645") 
            c.create_oval((200, 200, 100, 100),  fill="#b58645", outline="#b58645") 
    def lisa_nao():
        if var_nao.get()=="Nägu":
            c.create_oval((10, 10, 490, 490), fill="#b58645", outline="black") 
        elif var_nao.get()=="tühi":
            c.create_oval((10, 10, 490, 490), fill="#A9A9A9", outline="#A9A9A9") 
    def lisa_brov():
        if var_nao.get()=="Brov":
            c.create_line((400,100, 80, 100), fill="#0f0909",width=40) 
        elif var_nao.get()=="tühi":
            c.create_line((175,175,95,95), fill="#b58645") 
    lizo=Toplevel()#создаём второе(дочернее) окно Tk делает главную Toplevel делает вторую
    lizo.geometry("800x500")
    lizo.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
    lizo.configure(bg="#A9A9A9")

    c = Canvas(lizo, width=500, height=500, bg="#A9A9A9")
    c.pack(side=RIGHT)
    var_nina=StringVar()
    ch_nina=Checkbutton(lizo,text="НОС",height=3, width=15, font="Arial 20", fg="black", bg="green",variable=var_nina, onvalue="Nina", offvalue="tühi",command=lisa_nina)
    ch_nina.pack()
    var_suu=StringVar()
    ch_suu=Checkbutton(lizo,text="РОТ",height=3, width=15, font="Arial 20", fg="black", bg="green", variable=var_suu, onvalue="Suu", offvalue="tühi",command=lisa_suu)
    ch_suu.pack()
    var_eyes=StringVar()
    ch_eyes=Checkbutton(lizo,text="ГЛАЗА",height=3, width=15, font="Arial 20", fg="black", bg="green",variable=var_eyes, onvalue="Silmad", offvalue="tühi",command=lisa_eyes)
    ch_eyes.pack()
    var_nao=StringVar()
    ch_nao=Checkbutton(lizo,text="ГОЛОВА",height=3, width=15, font="Arial 20", fg="black", bg="green", variable=var_nao, onvalue="Nägu", offvalue="tühi",command=lisa_nao)
    ch_nao.pack()
    var_brov=StringVar()
    ch_brov=Checkbutton(lizo,text="БРОВЬ",height=3, width=15, font="Arial 20", fg="black", bg="green", variable=var_nao, onvalue="Brov", offvalue="tühi",command=lisa_brov)
    ch_brov.pack()
    lizo.mainloop()
def cmd1():
    print("Exit . . . ")
    aken.destroy()
def cmd2():
    print("Toplevel")
    aken.command=open_win()
def cmd3():
    print("TOPLEVEL")
    aken.command=open_win2()
def cmd4():
    print("формулы")
    aken.command=open_formul()
def cmd5():
    print("ЛИЦО")
    aken.command=open_lizo()
anim(0,0,"Р Е Ш Е Н И Е","#f86263","white", cmd2)
anim(0,37,"Ф О Р М У Л Ы","#f86263","white", cmd4)
anim(0,74, "Ф И Г У Р А", "#f86263","white", cmd3)
anim(0,111, "ФОТО РОБОТ", "#f86263","white", cmd5)
anim(0,148,"В Ы Х О Д","#ffcc66","white",cmd1)

#canvas=Canvas(aken,width=600,height=300)
#canvas.grid(columnspan=3)


aken.mainloop()

