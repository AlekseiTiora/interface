from tkinter import *
import math 
win=Tk()
win.title("Решение квадратного уровнения")
win.geometry("600x400")
def reshenie():
    x=a
    x1=b
    x2=c
    try:
        D = int(x1)**2-4*int(x)*int(x2)
    except:
        raise SystemExit

    Label(text="Дискриминант:", fg="dark red").grid(row=2, column=6)    
    label1=Label(text=D)
    label1.grid(row=2,column=7)

    if D > 0:
        b= int(x1)-int(x1*2)
        x_1=(b+math.sqrt(D)) / 2*int(x)
        Label(text="Первый x:", fg="dark red").grid(row=4, column=7)
        label_2 = Label(text=x_1)
        label_2.grid(row=4,column=9)
        x_2= (b-math.sqrt(D)) / 2*int(x)
        Label(text="Второй x:", fg="dark green").grid(row=5, column=7)
        label_3= Label(text=x_2)
        label_3.grid(row=5,column=9)
    elif D==0:
        b= int(x1)-int(x1*2)
        x_1=(b+math.sqrt(D)) / 2*int(x)
        Label(text="Первый x:", fg="dark red").grid(row=4, column=7)
        label_2 = Label(text=x_1)
        label_2.grid(row=4,column=9)
        x_2= (b-math.sqrt(D)) / 2*int(x)
        Label(text="Второй x:", fg="dark green").grid(row=5, column=7)
        label_3= Label(text="Отсутсвует.")
        label_3.grid(row=5,column=9)  
    else:
        Label(text="x:",fg="red").grid(row=5,column=7)
        label_1=Label(text="Дискриминант меньше нуля, корни отсуствуют.")
        label_1.grid(row=5, column=8)

        x_1=b / 2*int(x)
        Label(text)


frame = Frame(win)
frame.grid()
#Запрос числа а
a = Entry(frame, width=3)
a.grid(row=1,column=3,padx=(10,0))

a_lab=Label(frame,text="a=").grid(row=1,column=2)
#Запрос числа b
b = Entry(frame, width=3)
b.grid(row=1,column=6)

b_lab = Label(frame, text="b=").grid(row=1, column=4)
#Запрос числа c 
c = Entry(frame, width=4)
c.grid(row=1, column=10)

c_lab = Label(frame, text="c=").grid(row=1, column=7)

button = Button(frame, text="Решить")
button.grid(row=1, column=11, padx=(10,0))

button.bind("<Button-1>",reshenie)
win.mainloop()
