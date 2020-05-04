import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
import time
global f3,ee1,eee1,eee2,eee11,eee22
import tkinter.messagebox
global ee1,var9
from PIL import Image,ImageDraw,ImageFont
import cv2
import xlrd
import xlwt

tim=time.asctime()[11:16]

win = tk.Tk()
win.title('INVENTORY MANAGEMENT')
# bg='#0080FF'
bg='black'
bg1='white'
fg='white'
font='Times New Roman'


conn = sqlite3.connect('.//venv//Scripts//visitors.db')
c = conn.cursor()
conn1=sqlite3.connect('.//venv//Scripts//arwyhnxbhv.db')
c1=conn1.cursor()
conn2=sqlite3.connect('.//venv//Inventory.db')
c2=conn2.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS id_and_password(
            user_id text,
            password integer,
            admin text
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS school(
            scl_name text
            )''')


c1.execute('''CREATE TABLE IF NOT EXISTS key(
            key text
            )''')
c1.execute('''CREATE TABLE IF NOT EXISTS date_and_month(
            date int,
            month text
            )''')

c2.execute('''CREATE TABLE IF NOT EXISTS present_stock(
            ID int,
            Name text number,
            Category text,
            Sub_Category text,
            quantity int,
            cost_price int,
            last_updated_date text number
            )''')

c2.execute('''CREATE TABLE IF NOT EXISTS sales(
            ID int,
            Customer text,
            Product text number,
            Category text,
            Sub_Category text,
            quantity int,
            cost_price int,
            selling_price int,
            total_price int,
            date text number
            )''')

menu=Menu()
win.configure(menu=menu)
bg5 =tk.PhotoImage(file='../venv/images/w.png')
bgl=tk.Label(win,image=bg5)
bgl.place(relwidth=1,relheight=1)


def inv():
    w2=tk.Tk()
    c2.execute('SELECT * FROM present_stock')
    inventory_data=c2.fetchall()
    tv1 = ttk.Treeview(w2, height=20, columns=('NAME','CATEGORY','SUB-CATEGORY', 'QUANTITY','COST PRICE','LAST UPDATED DATE'))
    tv1.grid(row=1, column=3, rowspan=4)
    scroll = Scrollbar(w2, orient='vertical', command=tv1.yview)
    scroll.grid(row=1, column=4, sticky=NS, pady=(10, 0), rowspan=4)
    tv1.configure(yscrollcommand=scroll.set)
    tv1.column("#0", minwidth=0, width=50, stretch=NO, anchor=W)
    tv1.heading('#0', text='ID')
    tv1.column("NAME", minwidth=0, width=200, stretch=NO, anchor=W)
    tv1.heading('NAME', text='NAME')
    tv1.column("CATEGORY", minwidth=0, width=170, stretch=NO, anchor=W)
    tv1.heading('CATEGORY', text='CATEGORY')
    tv1.column("SUB-CATEGORY", minwidth=0, width=170, stretch=NO, anchor=W)
    tv1.heading('SUB-CATEGORY', text='SUB-CATEGORY')
    tv1.column("QUANTITY", minwidth=0, width=80, stretch=NO, anchor=W)
    tv1.heading('QUANTITY', text='QUANTITY')
    tv1.column("COST PRICE", minwidth=0, width=100, stretch=NO, anchor=W)
    tv1.heading('COST PRICE', text='COST PRICE')
    tv1.column("LAST UPDATED DATE", minwidth=0, width=200, stretch=NO, anchor=W)
    tv1.heading('LAST UPDATED DATE', text='LAST UPDATED DATE')
    for i in inventory_data:
        tv1.insert('', END, text=i[0], values=(i[1],i[2],i[3],i[4],i[5],i[6]))
    w2.mainloop()

def ev():
    c2.execute('SELECT * FROM present_stock')
    data = c2.fetchall()
    flag=0

    for i in data:
        if i[1]==E1.get():
            c2.execute("UPDATE present_stock SET quantity=(?) WHERE quantity=(?)",((int(i[4])+int(E2.get())),i[4]))
            conn2.commit()
            c2.execute("UPDATE present_stock SET last_updated_date=(?) WHERE last_updated_date=(?)",(time.asctime(),i[6]))
            conn2.commit()
            tkinter.messagebox.showinfo(message='UPDATED SUCCESSFULLY')
            flag=1


    if flag==0:
        tkinter.messagebox.showinfo(message='PLEASE CHECK THE SPELLINGS ARE CORRECT AND EVERYTHING IS IN UPPER CASE')

    w3.destroy()

def evi():
    c2.execute('SELECT * FROM present_stock')
    data = c2.fetchall()
    flag=0

    for i in data:
        if i[0]==int(E11.get()):
            c2.execute("UPDATE present_stock SET quantity=(?) WHERE quantity=(?)",((int(i[4])+int(E22.get())),i[4]))
            conn2.commit()
            c2.execute("UPDATE present_stock SET last_updated_date=(?) WHERE last_updated_date=(?)",(time.asctime(),i[6]))
            conn2.commit()
            tkinter.messagebox.showinfo(message='UPDATED SUCCESSFULLY')
            flag=1


    if flag==0:
        tkinter.messagebox.showinfo(message='PLEASE CHECK THE ID IS CORRECT')

    w3.destroy()

def receipt():
    global spr
    image = Image.new('RGB', (350, 320), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("arial.ttf", 10)

    c.execute('SELECT * FROM school')
    conn.commit()
    company = c.fetchall()



    if oo==1:
        ID=ide
    elif oo==2:
        ID = int(E11b.get())



    (x, y) = (50, 30)
    color = 'rgb(0, 0, 0)'
    draw.text((x, y), company[0][0], fill=color, font=ImageFont.truetype("arial.ttf", 23))


    (x, y) = (50, 90)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), 'NAME :                                        '+e1112.get(), fill=color, font=font)

    (x, y) = (50, 120)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), 'PRODUCT ID :                            '+str(ID), fill=color, font=font)

    if oo==2:
        (x, y) = (50, 150)
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), 'PRODUCT NAME :                      '+name, fill=color, font=font)
    elif oo==1:
        (x, y) = (50, 150)
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), 'PRODUCT NAME :                      ' + Eb1.get(), fill=color, font=font)

    if oo==2:        #eva
        q=int(Eb22b.get())
    elif oo==1:      #evaa
        q=int(Eb2.get())

    (x, y) = (50, 180)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), 'QUANTITY :                                 '+str(q), fill=color, font=font)

    (x, y) = (50, 210)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), 'PRICE :                                       '+str(int(q)*spr), fill=color, font=font)

    (x, y) = (50, 240)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), 'GST :                                          '+str(int(q)*spr*0.01*int(e11112.get())), fill=color, font=font)

    (x, y) = (50, 270)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), 'TOTAL PRICE :           ' + str((int(q) * spr * 0.01*int(e11112.get()) )+(int(q)*spr)), fill=color, font = ImageFont.truetype("arial.ttf", 15))

    # save the edited image in current directory.
    image.save('.//bills//'+e1112.get() + '.png')
    img2 = cv2.imread('.//bills//'+str(e1112.get())+'.png')
    cv2.imshow('Bill',img2)




r=StringVar(value='Select Product Name')
p=StringVar(value='Select Product Id')


def upstocks():
    global  E1,E2,w3,E11,E22
    w3=tk.Tk()
    c2.execute('SELECT * FROM present_stock')
    sale = c2.fetchall()
    n = []
    o = []

    for i in sale:
        n.append(i[1])
        o.append(i[0])

    fr1=Frame(w3)
    fr1.grid(row=0,column=0,padx=100,pady=20)
    fr2 = Frame(w3)
    fr2.grid(row=1, column=0,pady=20)

    laa1 = Label(fr1, text='UPDATE BY NAME', font=('arial', 25, 'bold italic underline'))
    laa1.grid(row=0, column=0)
    la1=Label(fr2,text='SELECT PRODUCT',font=('arial',15,'bold'))
    la1.grid(row=1,column=0,pady=10,padx=10)
    la2 = Label(fr2, text='QUANTITY', font=('arial', 15, 'bold'))
    la2.grid(row=3, column=0,pady=10,padx=10)

    E1=ttk.Combobox(fr2,font=('arial',15,'bold'),textvariable=r)
    E1['values']=n
    E1.grid(row=2,column=0,pady=10,padx=10)
    E2 = Entry(fr2, font=('arial', 16, 'bold'))
    E2.grid(row=4, column=0,pady=10,padx=30)
    B1=Button(fr2,text='UPDATE',font=('arial',15,'bold'),command=ev)
    B1.grid(row=5, column=0,pady=10)



    frr1 = Frame(w3)
    frr1.grid(row=0, column=1, padx=100,pady=30)
    frr2 = Frame(w3)
    frr2.grid(row=1, column=1,pady=20)

    laaa1 = Label(frr1, text='UPDATE BY ID', font=('arial', 25, 'bold italic underline'))
    laaa1.grid(row=0, column=0)
    law1 = Label(frr2, text='SELECT ID OF PRODUCT', font=('arial', 15, 'bold'))
    law1.grid(row=1, column=0, pady=10, padx=10)
    law2 = Label(frr2, text='QUANTITY', font=('arial', 15, 'bold'))
    law2.grid(row=3, column=0, pady=10, padx=10)
    E11 = ttk.Combobox(frr2, font=('arial', 15, 'bold'),textvariable=p)
    E11['values']=o
    E11.grid(row=2, column=0, pady=10, padx=10)
    E22 = Entry(frr2, font=('arial', 16, 'bold'))
    E22.grid(row=4, column=0, pady=10, padx=30)
    B11 = Button(frr2, text='UPDATE', font=('arial', 15, 'bold'), command=evi)
    B11.grid(row=5, column=0,pady=10)
    r.set(value='Select Product Name')
    p.set(value='Select Product Id')

    w3.mainloop()


def exps():
    c2.execute("SELECT * FROM sales")
    sales=c2.fetchall()
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet1 = workbook.add_sheet('sheet-1')
    sheet1.write(0, 0, 'ID')
    sheet1.write(0, 1, 'CUSTOMER')
    sheet1.write(0, 2, 'NAME')
    sheet1.write(0, 3, 'CATEGORY')
    sheet1.write(0, 4, 'SUB CATEGORY')
    sheet1.write(0, 5, 'QUANTITY')
    sheet1.write(0, 6, 'COST PRICE')
    sheet1.write(0, 7, 'SELLING PRICE')
    sheet1.write(0, 8, 'TOTAL PRICE')
    sheet1.write(0, 9, 'DATE')

    for i in range(len(sales)):
        sheet1.write(i + 1, 0, sales[i][0])
        sheet1.write(i + 1, 1, sales[i][1])
        sheet1.write(i + 1, 2, sales[i][2])
        sheet1.write(i + 1, 3, sales[i][3])
        sheet1.write(i + 1, 4, sales[i][4])
        sheet1.write(i + 1, 5, sales[i][5])
        sheet1.write(i + 1, 6, sales[i][6])
        sheet1.write(i + 1, 7, sales[i][7])
        sheet1.write(i + 1, 8, sales[i][8])
        sheet1.write(i + 1, 9, sales[i][9])

    workbook.save('SALES EXCEL.xls')
    tkinter.messagebox.showinfo(message='EXCEL FILE SAVED AS SALES EXCEL !!!')
    w4.destroy()


def re():
    global E11b,Eb1,Eb2,Eb22b,cust_name,w4,e1112,e11112,sp


    c2.execute('SELECT * FROM present_stock')
    sale = c2.fetchall()
    l = []
    m = []
    for i in sale:
        l.append(i[1])  # name list
        m.append(i[0])  # id list
    w4 = tk.Tk()
    fra1 = Frame(w4)
    fra1.grid(row=1, column=0, padx=10, pady=20)
    fra2 = Frame(w4)
    fra2.grid(row=2, column=0,padx=10, pady=20)
    fra00 = Frame(w4)
    fra00.grid(row=1, column=1, padx=10, pady=20)
    fra0 = Frame(w4)
    fra0.grid(row=2, column=1, padx=10, pady=10)


    l112 = Label(fra00, text='Enter your name / Company name', font=('arial', 15, 'bold'))
    l112.grid(row=0, column=1)
    e1112 = Entry(fra00, font=('arial', 15, 'bold'))
    e1112.grid(row=1, column=1)

    lab1 = Label(fra0, text='Enter GST percent (only number)', font=('arial', 15, 'bold'))
    lab1.grid(row=1, column=0, pady=10, padx=10)
    e11112 = Entry(fra0, font=('arial', 15, 'bold'))
    e11112.grid(row=2, column=0, pady=10, padx=10)
    lab2 = Label(fra0, text='Enter selling price', font=('arial', 15, 'bold'))
    lab2.grid(row=3, column=0, pady=10, padx=10, columnspan=2)
    sp = Entry(fra0, font=('arial', 16, 'bold'))
    sp.grid(row=4, column=0, pady=10, padx=30)
    Bb11 = Button(fra0, text='EXPORT SALES SHEET',font=('arial', 14, 'bold'),command=exps)
    Bb11.grid(row=5, column=0,pady=10)



    laab1 = Label(fra1, text='SALES BY NAME', font=('arial', 25, 'bold italic underline'))
    laab1.grid(row=0, column=0)
    lab1 = Label(fra2, text='SELECT PRODUCT', font=('arial', 15, 'bold'))
    lab1.grid(row=1, column=0, pady=10, padx=10)
    Eb1 = ttk.Combobox(fra2, font=('arial', 15, 'bold'))
    Eb1['values'] = l
    Eb1.grid(row=2, column=0, pady=10, padx=10)
    lab2 = Label(fra2, text='QUANTITY', font=('arial', 15, 'bold'))
    lab2.grid(row=3, column=0, pady=10, padx=10, columnspan=2)
    Eb2 = Entry(fra2, font=('arial', 16, 'bold'))
    Eb2.grid(row=4, column=0, pady=10, padx=30)
    Bb1 = Button(fra2, text='UPDATE', font=('arial', 15, 'bold'),command=evaa)
    Bb1.grid(row=5, column=0, pady=10)

    frra1 = Frame(w4)
    frra1.grid(row=1, column=2, padx=100, pady=30)
    frra2 = Frame(w4)
    frra2.grid(row=2, column=2, pady=20)

    laaab1 = Label(frra1, text='SALES BY ID', font=('arial', 25, 'bold italic underline'))
    laaab1.grid(row=0, column=0)
    lawb1 = Label(frra2, text='SELECT ID OF PRODUCT', font=('arial', 15, 'bold'))
    lawb1.grid(row=1, column=0, pady=10, padx=10)
    E11b = ttk.Combobox(frra2, font=('arial', 15, 'bold'))
    E11b['values'] = m
    E11b.grid(row=2, column=0, pady=10, padx=10)
    laaab2 = Label(frra2, text='QUANTITY', font=('arial', 15, 'bold'))
    laaab2.grid(row=3, column=0, pady=10, padx=10, columnspan=2)
    Eb22b = Entry(frra2, font=('arial', 16, 'bold'))
    Eb22b.grid(row=4, column=0, pady=10, padx=30)
    B11b = Button(frra2, text='UPDATE', font=('arial', 15, 'bold'), command=eva)
    B11b.grid(row=5, column=0, pady=10)

def eva():
    global q,oo,name,spr
    spr=int(sp.get())
    oo=2
    if e1112.get()=='':
        tkinter.messagebox.showerror(message='YOU CANT LEAVE NAME FIELD EMPTY')
    elif e11112.get()=='':
        tkinter.messagebox.showerror(message='YOU CANT LEAVE GST FIELD EMPTY')
    else:
        c2.execute('SELECT * FROM present_stock')
        data = c2.fetchall()
        for i in data:
            if i[0]==int(E11b.get()):
                name=i[1]
                cat=i[2]
                scat=i[3]
                cp=i[5]
                q=int(Eb22b.get())
                total=(spr*int(Eb22b.get()))+(spr*int(Eb22b.get())*0.05)
                break

        for i in data:
            if i[0]==int(E11b.get()):
                if int(i[4])-int(q)>=0:
                    c2.execute("UPDATE present_stock SET quantity=(?) WHERE quantity=(?)",((int(i[4])-int(q)),i[4]))
                    conn2.commit()
                    c2.execute("INSERT INTO sales VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(E11b.get(),e1112.get(),name, cat,scat,q,cp, spr,total,time.asctime()))
                    conn2.commit()
                    f = tkinter.messagebox.askyesno(message=' UPDATED SUCCESSFULLY DO YOU WANT TO PRINT THE RECEIPT ?')
                    if f == True:
                        receipt()
                    else:
                        pass
                else:
                    tkinter.messagebox.showerror(message='YOU DONT HAVE ENOUGH STOCKS')
        w4.destroy()





def evaa():
    global q,oo,ide,spr
    spr=int(sp.get())
    oo=1
    if e1112.get()=='':
        tkinter.messagebox.showerror(message='YOU CANT LEAVE NAME FIELD EMPTY')
    elif e11112.get()=='':
        tkinter.messagebox.showerror(message='YOU CANT LEAVE GST FIELD EMPTY')
    else:
        c2.execute('SELECT * FROM present_stock')
        data = c2.fetchall()

        for i in data:
            if i[1] == (Eb1.get()):
                ide=i[0]
                name = i[1]
                cat = i[2]
                scat = i[3]
                cp = i[5]
                q=Eb2.get()
                total = (spr * int(Eb2.get())) + (spr * int(Eb2.get()) * 0.05)
                break

        for i in data:
            if i[1] == (Eb1.get()):
                if (int(i[4]) - int(q)) >= 0:

                    c2.execute("UPDATE present_stock SET quantity=(?) WHERE quantity=(?)", ((int(i[4]) - int(q)), i[4]))
                    conn2.commit()
                    c2.execute("INSERT INTO sales VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(ide,e1112.get(),name,cat,scat,q, cp,spr,total,time.asctime()))
                    conn2.commit()
                    y = tkinter.messagebox.askyesno(message=' UPDATED SUCCESSFULLY DO YOU WANT TO PRINT THE RECEIPT ?')
                    if y == True:
                        receipt()
                    else:
                        pass

                else:
                    tkinter.messagebox.showerror(message='YOU DONT HAVE ENOUGH STOCKS')
        w4.destroy()



def ad():
    u=[]
    g=[]
    c2.execute('SELECT * FROM present_stock')
    d=c2.fetchall()
    for i in d:
        u.append(i[0])      # id list
        g.append(i[1])      # name list

    if ent1.get() in g:
        ans=tkinter.messagebox.askyesno(message='THIS PRODUCT IS ALREADY PRESENT IN STOCK DO YOU WANT TO UPDATE')
        if ans==True:
            for i in d:
                if i[1] == ent1.get():
                    c2.execute("UPDATE present_stock SET quantity=(?) WHERE quantity=(?)",((int(i[4]) + int(ent2.get())), i[4]))
                    conn2.commit()
                    c2.execute("UPDATE present_stock SET last_updated_date=(?) WHERE last_updated_date=(?)",(time.asctime(),i[7]))
                    conn2.commit()
                    tkinter.messagebox.showinfo(message='UPDATED SUCCESSFULLY')


    elif int(ent0.get()) in u:
        tkinter.messagebox.showerror(message='THIS ID IS ALREADY TAKEN')

    else:
        if (ent1.get()=='' or ent2.get()=='' or ent3.get()=='' or ent4.get()=='' or ent0.get()=='' or ent5.get()=='' ):
            tkinter.messagebox.showerror(message="YOU CAN'T LEAVE ANY FIELD EMPTY")
        else:
            c2.execute("INSERT INTO present_stock VALUES('{}','{}','{}','{}','{}','{}','{}')".format(ent0.get(),ent1.get(),ent3.get(),ent4.get(),ent2.get(),ent5.get(),(time.asctime())))
            conn2.commit()
            tkinter.messagebox.showinfo(message='ADDED SUCCESFULLY')
            w5.destroy()

def add():
    global ent1,ent2,ent3,ent4,w5,ent0,ent5
    w5=tk.Tk()

    fra=Frame(w5)
    fra.grid(row=0,column=0)

    lab0 = Label(fra, text='ID of Product ->', font=('arial', 18, 'bold'))
    lab0.grid(row=0, column=0, padx=12, pady=8)
    lab1=Label(fra,text='Name of Product ->',font=('arial',18,'bold'))
    lab1.grid(row=1,column=0,padx=12,pady=8)
    lab2 = Label(fra, text='Quantity ->', font=('arial', 18, 'bold'))
    lab2.grid(row=2, column=0,padx=12,pady=8)
    lab3 = Label(fra, text='Category of Product ->', font=('arial', 18, 'bold'))
    lab3.grid(row=3, column=0,padx=12,pady=8)
    lab4 = Label(fra, text='Sub Category of Product ->', font=('arial', 18, 'bold'))
    lab4.grid(row=4, column=0,padx=12,pady=8)
    lab5 = Label(fra, text='Cost Price ->', font=('arial', 18, 'bold'))
    lab5.grid(row=5, column=0, padx=12, pady=8)

    ent0 = Entry(fra, font=('arial', 18, 'bold'))
    ent0.grid(row=0, column=1, padx=12, pady=8)
    ent1=Entry(fra, font=('arial', 18, 'bold'))
    ent1.grid(row=1,column=1,padx=12,pady=8)
    ent2 = Entry(fra, font=('arial', 18, 'bold'))
    ent2.grid(row=2, column=1,padx=12,pady=8)
    ent3 = Entry(fra, font=('arial', 18, 'bold'))
    ent3.grid(row=3, column=1,padx=12,pady=8)
    ent4 = Entry(fra, font=('arial', 18, 'bold'))
    ent4.grid(row=4, column=1,padx=12,pady=8)
    ent5 = Entry(fra, font=('arial', 18, 'bold'))
    ent5.grid(row=5, column=1, padx=12, pady=8)

    lab1 = Label(fra, text='*PLEASE WRITE EVERYTHING IN CAPITAL LETTERS', font=('arial', 8, 'bold'))
    lab1.grid(row=7, column=0, padx=12, pady=25)

    bab1=Button(fra, text='Submit', font=('arial', 18, 'bold'),command=ad)
    bab1.grid(row=8,column=0,sticky=E,padx=10,pady=15)
    w5.mainloop()


def sea():
    c2.execute('SELECT * FROM present_stock')
    d=c2.fetchall()
    flag=0

    if eaab.get()=='':
        for i in d:
            if i[0]==int(eaab1.get()):
                tv2.insert('',0,text=i[0],values=i[1:])
                flag=1
                break

    elif eaab1.get()=='':
        for i in d:
            if i[1]==eaab.get():
                tv2.insert('', 0, text=i[0], values=i[1:])
                flag=1
                break

    if flag==0:
        tkinter.messagebox.showerror(message='NOTHING WITH THIS NAME OR ID')





def search():
    global eaab,eaab1,w6,tv2

    w6=tk.Tk()

    fraa=Frame(w6)
    fraa.grid(row=0,column=0)

    tv2 = ttk.Treeview(w6, height=20, columns=('NAME', 'CATEGORY', 'SUB-CATEGORY', 'QUANTITY','COST PRICE','LAST UPDATED DATE'))
    tv2.grid(row=0, column=1, rowspan=4)
    tv2.column("#0", minwidth=0, width=50, stretch=NO, anchor=W)
    tv2.heading('#0', text='ID')
    tv2.column("NAME", minwidth=0, width=100, stretch=NO, anchor=W)
    tv2.heading('NAME', text='NAME')
    tv2.column("CATEGORY", minwidth=0, width=100, stretch=NO, anchor=W)
    tv2.heading('CATEGORY', text='CATEGORY')
    tv2.column("SUB-CATEGORY", minwidth=0, width=100, stretch=NO, anchor=W)
    tv2.heading('SUB-CATEGORY', text='SUB-CATEGORY')
    tv2.column("QUANTITY", minwidth=0, width=100, stretch=NO, anchor=W)
    tv2.heading('QUANTITY', text='QUANTITY')
    tv2.column("COST PRICE", minwidth=0, width=100, stretch=NO, anchor=W)
    tv2.heading('COST PRICE', text='COST PRICE')
    tv2.column("LAST UPDATED DATE", minwidth=0, width=180, stretch=NO, anchor=W)
    tv2.heading('LAST UPDATED DATE', text='LAST UPDATED DATE')


    laab = Label(fraa, text='ENTER PRODUCT NAME TO SEARCH', font=('arial', 18, 'bold'))
    laab.grid(row=0, column=0, padx=12, pady=8)
    eaab = Entry(fraa, font=('arial', 18, 'bold'))
    eaab.grid(row=1, column=0, padx=12, pady=8)
    laab1 = Label(fraa, text='ENTER PRODUCT ID TO SEARCH', font=('arial', 18, 'bold'))
    laab1.grid(row=2, column=0, padx=12, pady=8)
    eaab1 = Entry(fraa, font=('arial', 18, 'bold'))
    eaab1.grid(row=3, column=0, padx=12, pady=8)

    bb1=Button(fraa, text='SEARCH', font=('arial', 18, 'bold'),command=sea)
    bb1.grid(row=4,column=0,pady=20,padx=20)

    laab2 = Label(fraa, text='**PLEASE SEARCH EITHER BY ID OR BY NAME \nNOT BOTH ', font=('arial', 10, 'bold'))
    laab2.grid(row=5, column=0, padx=12, pady=8)



    w6.mainloop()




def login_verify(event=None):
    c1.execute('SELECT * FROM date_and_month')
    dam = c1.fetchall()
    c.execute('SELECT * FROM id_and_password')
    conn.commit()
    c2=c.fetchall()
    if e11.get() == c2[0][0] and e12.get() == str(c2[0][1]):
        f0.grid_forget()
        f1.grid(row=2, column=1, padx=200, pady=15, sticky=E)
        f2.grid(row=0, column=1, padx=180, pady=20)
        f4.grid(row=1, column=1, padx=180, pady=5)
        f5.grid(row=0, column=1, sticky=E)

# cp='#3fa0fc'
cp='black'
# f7=Frame(win,bg='white',relief='raised')
# f7.grid(row=0,column=0,pady=16,padx=11)
f1=Frame(win,relief='raised',bd=3)
f1.configure(width='1700',height='1070')
f2=Frame(win,relief='raised',bg=cp)
f4=Frame(win,relief='raised',bg=cp)
f5=Frame(win,relief='raised',bg=cp)


# f0=Frame(win,bg='#48494B')
loginpagecolor='white'
f0=Frame(win,bg=loginpagecolor)
f0.grid(row=1,column=0,padx=450,pady=130)
l11=Label(f0,text='User-id',font=(font,15),bg=loginpagecolor,fg='black',bd=5)
l11.grid(row=1,column=0,padx=50,pady=5,sticky=W)
e11=Entry(f0,font=(font,20),bg='#eeeeee',fg='BLACK')
e11.grid(row=2,column=0,padx=50,pady=5)
e11.bind('<Return>',login_verify)
l12=Label(f0,text='Password',font=(font,15),bg=loginpagecolor,fg='black',bd=5)
l12.grid(row=3,column=0,padx=50,pady=5,sticky=W)
e12=Entry(f0,font=(font,20),fg='BLACK',bg='#eeeeee',show='*')
e12.grid(row=4,column=0,padx=50,pady=5)
b11=Button(f0,text='LOG IN',font=(font,15),command=login_verify,width=25,bg='#3fa0fc',fg='white')
b11.grid(row=5,column=0,pady=30)
e12.bind('<Return>',login_verify)   #Using bind


canvas = Canvas(master=f0,height=60,width=160,bg='white')
canvas.grid(row=0,column=0,padx=50,pady=20)
my_image = PhotoImage(file="../venv/images/elogo1.png")
canvas.create_image(0,0,anchor=NW, image=my_image)


vari1=StringVar(value='')
vari2=StringVar(value='')
vari3=StringVar(value='')
vari4=StringVar(value='')
vari11=StringVar(value='')
vari22=StringVar(value='')
vari33=StringVar(value='')
varia11=StringVar(value='')
varia22=StringVar(value='')


#------------FUNCTIONS------------------
def change_user():
    global eee1,eee2,eee3,eee4
    w2=tk.Tk()
    w2.configure(bg='#48494B')
    ll1=Label(w2,text='old user id',font=(font,16),bg='#48494B',fg='WHITE')
    ll1.grid(row=1,column=1,padx=35,pady=3)
    eee1=Entry(w2,textvariable=vari1,font=(font,16),bg='#FCD12A',fg='BLACK')
    eee1.grid(row=2,column=1,padx=35,pady=3)
    ll3 = Label(w2, text='admin password',font=(font,16),bg='#48494B',fg='WHITE')
    ll3.grid(row=5, column=1,padx=35,pady=3)
    eee3 = Entry(w2, textvariable=vari3, show='*',font=(font,16),bg='#FCD12A',fg='BLACK')
    eee3.grid(row=6, column=1,padx=35,pady=3)
    ll2 = Label(w2, text='new user id',font=(font,16),bg='#48494B',fg='WHITE')
    ll2.grid(row=7, column=1,padx=35,pady=3)
    eee4 = Entry(w2, textvariable=vari4,font=(font,16),bg='#FCD12A',fg='BLACK')
    eee4.grid(row=8, column=1,padx=35,pady=3)
    bb1=Button(w2,text='change',command=change,font=(font,16))
    bb1.grid(row=9,column=1,padx=35,pady=3)
    w2.mainloop()

def change():
    global eee1,eee4,eee3
    c.execute('SELECT * FROM id_and_password')
    conn.commit()
    c3 = c.fetchall()
    if eee1.get()==c3[0][0]  and eee3.get()==str(c3[0][2]) :
        print(eee4.get())
        print(c3[0][0])
        c.execute("UPDATE id_and_password SET user_id=(?) WHERE user_id=(?)",(eee4.get(),c3[0][0]))
        conn.commit()
        tkinter.messagebox.showinfo('success','user id changed successfully')

    else:
        tkinter.messagebox.showerror('Error', 'old user id or admin password does not match')

def change_pass():
    global eee11,eee22,eee12
    w4=tk.Tk()
    w4.configure(bg='#48494B')
    ll11=Label(w4,text='old password',font=(font,16),bg='#48494B',fg='WHITE')
    ll11.grid(row=1,column=1,padx=35,pady=3)
    eee11=Entry(w4,textvariable=vari11,show='*',font=(font,16),bg='#FCD12A',fg='BLACK')
    eee11.grid(row=2,column=1,padx=35,pady=3)
    ll12 = Label(w4, text='admin password',font=(font,16),bg='#48494B',fg='WHITE')
    ll12.grid(row=3, column=1,padx=35,pady=3)
    eee12 = Entry(w4, textvariable=vari22, show='*',font=(font,16),bg='#FCD12A',fg='BLACK')
    eee12.grid(row=4, column=1,padx=35,pady=3)
    ll22 = Label(w4, text='new password',font=(font,16),bg='#48494B',fg='WHITE')
    ll22.grid(row=5, column=1,padx=35,pady=3)
    eee22 = Entry(w4, textvariable=vari33,show='*',font=(font,16),bg='#FCD12A',fg='BLACK')
    eee22.grid(row=6, column=1,padx=35,pady=3)
    bb11=Button(w4,text='change',command=change1,font=(font,16))
    bb11.grid(row=7,column=1,padx=35,pady=3)
    w4.mainloop()

def change1():
    global eee11,eee22,eee12
    c.execute('SELECT * FROM id_and_password')
    conn.commit()
    c5 = c.fetchall()
    if eee11.get()==str(c5[0][1]) and eee12.get()==str(c5[0][2]):
        c.execute("UPDATE id_and_password SET password=(?) WHERE password=(?)",(eee22.get(),c5[0][1]))
        conn.commit()
        tkinter.messagebox.showinfo('success','password changed successfully')

    else:
        tkinter.messagebox.showerror('Error', 'password or admin password does not match')


def change_admin():
    global ea1,ea2
    w6=tk.Tk()
    w6.configure(bg='#48494B')
    la1=Label(w6,text='old admin password',font=(font,16),bg='#48494B',fg='WHITE')
    la1.grid(row=1,column=1,padx=35,pady=3)
    ea1=Entry(w6,textvariable=varia11,show='*',font=(font,16),bg='#FCD12A',fg='BLACK')
    ea1.grid(row=2,column=1,padx=35,pady=3)
    la2 = Label(w6, text='new admin password',font=(font,16),bg='#48494B',fg='WHITE')
    la2.grid(row=3, column=1,padx=35,pady=3)
    ea2 = Entry(w6, textvariable=varia22, show='*',font=(font,16),bg='#FCD12A',fg='BLACK')
    ea2.grid(row=4, column=1,padx=35,pady=3)
    ba1=Button(w6,text='change',command=change2,font=(font,16))
    ba1.grid(row=7,column=1,padx=35,pady=3)
    w6.mainloop()

def change2():
    global ea1,ea2
    c.execute('SELECT * FROM id_and_password')
    conn.commit()
    c6 = c.fetchall()
    if ea1.get()==str(c6[0][2]):
        c.execute("UPDATE id_and_password SET admin=(?) WHERE admin=(?)",(ea2.get(),c6[0][2]))
        conn.commit()
        tkinter.messagebox.showinfo('success','admin password changed successfully')

    else:
        tkinter.messagebox.showerror('Error', 'old admin password does not match')


def get_val():
    global ee1
    c.execute('SELECT scl_name FROM school')
    conn.commit()
    c4 = c.fetchall()
    c.execute("UPDATE school SET scl_name=(?) WHERE scl_name=(?)",(ee1.get(),c4[0][0]))
    conn.commit()
    tkinter.messagebox.showinfo('Restart', 'Please restart the program')


def change_school_name():
    global ee1
    win1=tk.Tk()
    win1.configure(bg='#48494B')
    win1.title('change school name')
    Label(win1,text='Enter institute name',font=(font,20),bg='#48494B',fg='WHITE').grid(row=0,column=0)
    ee1=Entry(win1,width=30,font=(font,20),bg='#FCD12A',fg='BLACK')
    ee1.grid(row=1,column=0,padx=5,pady=5)
    Button(win1,text='OK',command=get_val,font=(font,15)).grid(row=2,column=0,padx=5,pady=5)
    win1.mainloop()



def exit():
    win.forget(window=win)
    conn.close()
    conn1.close()
    conn2.close()
    c.close()
    c1.close()
    c2.close()



#-------------DISPLAY TIME----------------------------
#
def tick():
    time_string=time.strftime('%H:%M:%S')
    clock.config(text='************* '+time.asctime()[8:10] + ' ' + time.asctime()[4:7]+' '+time_string+' *************')
    clock.after(200,tick)
clock=Label(f4,font=(font,20,'bold italic'),fg='white',bg=cp)
clock.grid(row=1,column=1)
tick()

varl1=StringVar(value='')

def imp():
    workbook = xlrd.open_workbook('Stocks.xlsx')
    sheet = workbook.sheet_by_index(0)
    c2.execute('SELECT * from present_stock')
    dw = c2.fetchall()

    main_id_list=[]
    for e in dw:
        main_id_list.append(int(e[0]))

    for d in range(1,sheet.nrows):
        if int(sheet.cell_value(d,0)) in main_id_list:
            for i in dw:
                if int(sheet.cell_value(d,0)==int(i[0])) and (sheet.cell_value(d,1))==i[1]:
                    c2.execute("UPDATE present_stock SET quantity =(?) WHERE ID=(?)",((int(sheet.cell_value(d,4))+i[4]),int(i[0])))
                    conn2.commit()
                    c2.execute("UPDATE present_stock SET last_updated_date=(?) WHERE last_updated_date=(?)",(time.asctime(),i[6]))
                    conn2.commit()
        else:
            if sheet.cell_value(d,0)!=''and sheet.cell_value(d,1)!='' and sheet.cell_value(d,2) !='' and sheet.cell_value(d,3)!='' and sheet.cell_value(d,4)!='' and sheet.cell_value(d,5)!='':
                c2.execute("INSERT INTO present_stock VALUES('{}','{}','{}','{}','{}','{}','{}')".format(sheet.cell_value(d,0), sheet.cell_value(d,1),sheet.cell_value(d,2),sheet.cell_value(d,3),sheet.cell_value(d,4),sheet.cell_value(d,5),time.asctime()))
                conn2.commit()
            else:
                tkinter.messagebox.showerror(message='YOU HAVE MISSING INFORMATION IN YOUR EXCEL SHEET.PLEASE COMPLETE THEM AND TRY AGAIN')

    tkinter.messagebox.showinfo(message='UPDATED SUCCESSFULLY !!!')



def exp():
    c2.execute("SELECT * FROM present_stock")
    export=c2.fetchall()
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet1 = workbook.add_sheet('sheet-1')
    sheet1.write(0, 0, 'ID')
    sheet1.write(0, 1, 'NAME')
    sheet1.write(0, 2, 'CATEGORY')
    sheet1.write(0, 3, 'SUB CATEGORY')
    sheet1.write(0, 4, 'QUANTITY')
    sheet1.write(0, 5, 'COST PRICE')
    sheet1.write(0, 6, 'LAST UPDATED')

    for i in range(len(export)):
        sheet1.write(i+1, 0,export[i][0])
        sheet1.write(i+1, 1,export[i][1])
        sheet1.write(i+1, 2,export[i][2])
        sheet1.write(i+1, 3,export[i][3])
        sheet1.write(i+1, 4,export[i][4])
        sheet1.write(i+1, 5,export[i][5])
        sheet1.write(i+1, 6,export[i][6])
    workbook.save('EXPORTED EXCEL.xls')
    tkinter.messagebox.showinfo(message='EXCEL FILE SAVED AS EXPORTED EXCEL !!!')



#-----------VARIABLES DECLARATION-------------

var1=StringVar(value='')
var2=IntVar(value='')
var3=StringVar(value='Select identity')
var4=StringVar(value='')
var5=StringVar(value='Select duration')
var6=StringVar(value='')
var7=StringVar(value='')
var8=IntVar(value='')
var10=StringVar(value='')

#------------MENU-------------------

Change_user=Menu(menu)
Change_user.add_command(label='Change user',command=change_user)
menu.add_cascade(label='Change user',menu=Change_user)

Change_pass=Menu(menu)
Change_pass.add_command(label='Change pass',command=change_pass)
menu.add_cascade(label='Change password',menu=Change_pass)

Change_school_name=Menu(menu)
Change_school_name.add_command(label='Change company name',command=change_school_name)
menu.add_cascade(label='Change institute name',menu=Change_school_name)

Change_admin=Menu(menu)
Change_admin.add_command(label='Change admin',command=change_admin)
menu.add_cascade(label='Change admin',menu=Change_admin)




EXIT=Menu(menu)
EXIT.add_command(label='Exit',command=exit)
menu.add_cascade(label='Exit',menu=EXIT)

#-------------LABELS----------------------

c.execute('SELECT * FROM school')
conn.commit()
c4 = c.fetchall()

l1=Label(f2,text=c4[0][0],font=(font,35,'bold'),fg='white',bg=cp)
l1.grid(row=0,column=2, padx=5,pady=10,sticky=E)



#------------------BUTTONS---------------------

b1=Button(f1,text='OPEN INVENTORY',font=(font,16),bg='#29AB87',fg='white',width=27,height=2,command=inv)
b1.grid(row=1,column=2,pady=22,padx=50,sticky=W)

b2=Button(f1,text='SALES',font=(font,16),bg='#29AB87',fg='white',width=27,height=2,command=re)
b2.grid(row=3,column=3,pady=22,padx=50,sticky=W)

b3=Button(f1,text='UPDATE STOCKS',font=(font,16),bg='#29AB87',fg='white',width=27,height=2,command=upstocks)
b3.grid(row=2,column=2,pady=22,padx=50,sticky=W)

b4=Button(f1,text='ADD PRODUCT',font=(font,16),bg='#29AB87',fg='white',width=27,height=2,command=add)
b4.grid(row=1,column=3,pady=22,padx=40,sticky=W)

b5=Button(f1,text='SEARCH',font=(font,16),bg='#29AB87',fg='white',width=27,height=2,command=search)
b5.grid(row=2,column=3,pady=22,padx=40,sticky=W)

b6=Button(f1,text='IMPORT STOCKS',font=(font,16),fg='white',bg='#29AB87',width=27,command=imp,height=2)
b6.grid(row=3,column=2,pady=22,padx=50,sticky=E)

b7=Button(f1,text='EXPORT STOCKS',font=(font,16),fg='white',bg='#29AB87',width=27,command=exp,height=2)
b7.grid(row=4,column=2,pady=22,padx=50,sticky=E)

b6=Button(f1,text='EXIT',font=(font,16),fg='white',bg='#131414',width=27,command=exit,height=2)
b6.grid(row=4,column=3,pady=22,padx=50,sticky=E)


#------------------------------------------------
win.mainloop()
