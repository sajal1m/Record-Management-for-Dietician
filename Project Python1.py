from tkinter import *
import time

a = Tk()
a.title('The dietician')

count=0

def addrec():
    
    f=open('data.txt','a+')

    name=v1.get()
    size=v2.get()
    w=v3.get()
    en=v4.get()
    protein=v5.get()
    carbo=v6.get()
    fat=v7.get()
    var = Lb.get(ACTIVE)

    if name == "" or size == "" or w == "" or en == "" or protein == "" or carbo == "" or fat == "" or var == "" :
         l13 = Label(a, text = 'Enter all Fields')
         l13.grid(row = 8, columns = 5)

    else :    
        f.writelines(name.ljust(10)+size.ljust(10)+w.ljust(5)+en.ljust(5)+protein.ljust(5)+carbo.ljust(5)+fat.ljust(5)+var.ljust(10)+"\n")
        v1.set("")
        v2.set("")
        v3.set("")
        v4.set("")
        v5.set("")
        v6.set("")
        v7.set("")

        l9 = Label(a, text = 'Success')
        l9.grid(row = 5, columns = 4)
    
    f.close()


def nextrec():
    try :
        global count
        f=open('data.txt','r')
        i=0
        while i <= count:
                l = f.readline()
                i = i+1
        l1=l.split()
        v1.set(l1[0])
        v2.set(l1[1])
        v3.set(l1[2])
        v4.set(l1[3])
        v5.set(l1[4])
        v6.set(l1[5])
        v7.set(l1[6])
        Lb.see(1)
        count=count+1
        f.close()

    except :
         l11 = Label(a, text = 'This is last record')
         l11.grid(row = 7, columns = 5)

def delete():

    k = [v1.get(), v2.get(), v3.get(), v4.get(), v5.get(), v6.get(), v7.get(), Lb.get(ACTIVE)]

    f = open("data.txt","r")

    x = f.readlines()
    f.close()

    f = open("data.txt","w")
    for i in x:
        l2 = i.split()
        if(l2[0] != k[0]):
            f.writelines(l2[0].ljust(10)+l2[1].ljust(10)+l2[2].ljust(5)+l2[3].ljust(5)+l2[4].ljust(5)+l2[5].ljust(5)+l2[6].ljust(5)+l2[7].ljust(10)+"\n")

    v1.set("")
    l9 = Label(a, text = 'Success')
    l9.grid(row = 6, columns = 4)

   
    f.close()

def search():

    k = v1.get()

    f = open("data.txt","r")

    x = f.readlines()

    for i in x:
        j = i.split()
        if j[0] == k:
            v1.set(j[0])
            v2.set(j[1])
            v3.set(j[2])
            v4.set(j[3])
            v5.set(j[4])
            v6.set(j[5])
            v7.set(j[6])

    f.close()

def prevrec():
    try :
        f=open('data.txt','r')
        i=0
        global count
        count=count-1

        while i <= count-1 :
            l = f.readline()
            i = i+1

        l1 = l.split()

        v1.set(l1[0])	
        v2.set(l1[1])
        v3.set(l1[2])
        v4.set(l1[3])
        v5.set(l1[4])
        v6.set(l1[5])
        v7.set(l1[6])

    

        f.close()  

    except :
        l12 = Label(a, text = 'This is first record')
        l12.grid(row = 7, columns = 4)

def update():

    f=open("data.txt","r+")

    name=v1.get()
    size=v2.get()
    w=v3.get()
    en=v4.get()
    protein=v5.get()
    carbo=v6.get()
    fat=v7.get()
    var = Lb.get(ACTIVE)

    h=f.readlines()

    f.seek(0)

    
    for i in h:

        l2=i.split()

        if l2[0]==name :

            f.writelines(name.ljust(10)+size.ljust(10)+w.ljust(5)+en.ljust(5)+protein.ljust(5)+carbo.ljust(5)+fat.ljust(5)+var.ljust(10)+"\n")

        else :
            f.writelines(l2[0].ljust(10)+l2[1].ljust(10)+l2[2].ljust(5)+l2[3].ljust(5)+l2[4].ljust(5)+l2[5].ljust(5)+l2[6].ljust(5)+l2[7].ljust(10)+"\n")


    v1.set("")
    v2.set("")
    v3.set("")
    v4.set("")
    v5.set("")
    v6.set("")
    v7.set("")

    l10 = Label(a, text = 'Updated')
    l10.grid(row = 7, columns = 4)
    
    f.truncate()
    f.close()

def lastrec():
    global count
    f=open('data.txt','r')

    x = f.readlines()
    x1 = x[len(x)-1]
    y = x1.split()
    v1.set(y[0])
    v2.set(y[1])
    v3.set(y[2])
    v4.set(y[3])
    v5.set(y[4])
    v6.set(y[5])
    v7.set(y[6])

    f.close()
    
    nl = 0
    
    with open('data.txt', 'r') as f:
        for line in f:
            nl = nl+1
            count = nl


def firstrec():
    global count
    count = 1
    f = open('data.txt','r')
    x = f.readlines()
    x1 = x[0]
    y = x1.split()
    v1.set(y[0])
    v2.set(y[1])
    v3.set(y[2])
    v4.set(y[3])
    v5.set(y[4])
    v6.set(y[5])
    v7.set(y[6])

    f.close()

l1 = Label(a, text='Name')
l1.grid(row=0,column=0)

l2 = Label(a, text='Size')
l2.grid(row=1,column=0)

l3 = Label(a, text='Weight')
l3.grid(row=2,column=0)

l4 = Label(a, text='Energy')
l4.grid(row=3,column=0)

l5 = Label(a, text='Protein')
l5.grid(row=4,column=0)

l6 = Label(a, text='Carbohydrates')
l6.grid(row=5,column=0)

l7 = Label(a, text='Fat')
l7.grid(row=6,column=0)

l8 = Label(a, text='Food Type')
l8.grid(row=7,column=0)

###############
v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()
v5=StringVar()
v6=StringVar()
v7=StringVar()
###############
e1 = Entry(a, textvariable=v1)
e2 = Entry(a, textvariable=v2)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3 = Entry(a, textvariable=v3)
e4 = Entry(a, textvariable=v4)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5 = Entry(a, textvariable=v5)
e6 = Entry(a, textvariable=v6)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7 = Entry(a, textvariable=v7)
e7.grid(row=6, column=1)

Lb = Listbox(a)
Lb.insert(1, 'Fruits')
Lb.insert(2, 'Baked Goods')
Lb.insert(3, 'Vegetables')
Lb.insert(4, 'Meat')
Lb.insert(5, 'Beverages')
Lb.insert(6, 'Fast Foods')
Lb.insert(7, 'Fats and Oils')
Lb.insert(8, 'Sweets')
Lb.grid(row=7, column=1)

###################################
#var = 'Yo Yo'
#l9 = Label(a, text = var, height = 5, width = 5)
#l9.grid(column=2)
###################################



b1 = Button(a, text = 'Add', width=33, command = addrec)
b1.grid(row=0,column=2)
b1 = Button(a, text = 'Delete', width=33, command = delete)
b1.grid(row=0,column=3)
b1 = Button(a, text = 'Update', width=33, command = update)
b1.grid(row=1,column=2)
b1 = Button(a, text = 'Search', width=33, command = search)
b1.grid(row=1,column=3)
b1 = Button(a, text = 'Previous', width=33, command = prevrec)
b1.grid(row=2,column=2)
b1 = Button(a, text = 'Next', width=33, command = nextrec)
b1.grid(row=2,column=3)
b1 = Button(a, text = 'First', width=33, command = firstrec)
b1.grid(row=3,column=2)
b1 = Button(a, text = 'Last', width=33, command = lastrec)
b1.grid(row=3,column=3)


a.mainloop()
