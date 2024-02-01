from tkinter import * 
from tkinter import messagebox
from time import sleep
#funcs--------------------------------
lst = []
def clear_entry():
    en_name.delete(0,END)
    en_family.delete(0,END)
    en_city.delete(0,END)
    en_tel.delete(0,END)

def add():
    name_v = en_name.get()
    family_v = en_family.get()
    city_v = en_city.get()
    tel_v = en_tel.get()

    if name_v == ''  or not name_v.isalpha():
        messagebox.showerror('Eror', 'fill in the name box also just enter Letters !(A-Z)')
        en_name.delete(0,END)
        en_name.focus_set()

    elif family_v == '' or not family_v.isalpha():
        messagebox.showerror('Eror', 'fill in the name box also just enter Letters !(A-Z)')
        en_family.delete(0,END)
        en_family.focus_set()

    elif city_v == '' or not city_v.isalpha():
        messagebox.showerror('Eror', 'fill in the name box also just enter Letters !(A-Z)')
        en_city.delete(0,END)
        en_city.focus_set()

    elif not tel_v.isdigit() :
        messagebox.showerror('Eror', 'fill in the tel box also just enter number ! ')
        en_tel.delete(0,END)
        en_tel.focus_set()

    else:
        lst_box.insert(0,name_v + ' ' +family_v + ' ' +city_v + ' ' + tel_v)
        en_name.focus_set()
        lst.append(name_v)
        lst.append(family_v)
        lst.append(city_v)
        lst.append(tel_v)
        clear_entry()

def delete():
    choice = lst_box.curselection()
    user = messagebox.askyesno('Question' , 'do you want to continue?',default= messagebox.NO)
    if user == True :
        sleep(0.5)
        lst_box.delete(choice)

def clear():
    user = messagebox.askyesno('Question' , 'do you want to continue?',default= messagebox.NO)
    if user == True:
        sleep(0.4)
        clear_entry()

def fetch() :
    choice = lst_box.curselection()
    done = lst_box.get(choice)
    clear_entry()
    en_name.insert(choice, lst[0])
    en_family.insert(choice,lst[1])
    en_city.insert(choice,lst[2])
    en_tel.insert(choice,lst[3])

def leave():
    user = messagebox.askyesno('Question' , 'do you want to continue?',default= messagebox.NO)
    if user == True :
        sleep(0.5)
        win.destroy()

#window------------------------
win = Tk()
win.title('Normal GUI')
win.geometry('800x600')
win.resizable(0,0)
win['bg'] = '#BADB15'
#frame------------------------------
fr1 = Frame(win, width=400,height=450 ,bg= 'white')
fr1.place(relx=0.5 , rely= 0.5 , anchor='c')
#Entry--------------------------------
en_name = Entry(win, width= 25 , bg= '#fffffb' , font= 'arial 13')
en_name.place(relx= 0.5 , y= 110 , anchor='c')
en_family = Entry(win, width= 25 , bg= '#fffffb' , font= 'arial 13')
en_family.place(relx=0.5 , y= 140 , anchor='c')
en_city = Entry(win, width=25 , bg= '#fffffb' , font= 'arial 13')
en_city.place(relx=0.5 , y= 170 , anchor='c')
en_tel = Entry(win, width=25 , bg= '#fffffb' , font= 'arial 13')
en_tel.place(relx=0.5 , y= 200 , anchor='c')
#label--------------------------------
lbl_name = Label(win, text= 'Name :' , font= 'consolas 12' , bg='white')
lbl_name.place(x= 256 , y= 108 , anchor='c')
lbl_family = Label(win, text= 'Family :' , font= 'consolas 12' , bg='white')
lbl_family.place(x= 247 , y= 138 , anchor='c')
lbl_city = Label(win, text= 'City :' , font= 'consolas 12' , bg='white')
lbl_city.place(x= 256 , y= 168 , anchor='c')
lbl_tel = Label(win, text= 'Tel :' , font= 'consolas 12' , bg='white')
lbl_tel.place(x= 260 , y= 198 , anchor='c')
lbl_shafiei = Label(win, text= '--by Shafiei--' , font= 'consolas 10' , bg='white')
lbl_shafiei.place(relx= 0.5 , y= 510 , anchor='c')
#listbox--------------------------------
lst_box = Listbox(win, bg='#fffffb' , width=31, height=5 , font= 'arial 13' )
lst_box.place(relx=0.5 , y = 285 , anchor='c')
#Buttons--------------------------------
btn_add = Button(win, text='Add' , font= 'arial 13' , width=12 , bg= '#fffffb' , command= add)
btn_add.place(x= 320 , y= 370 , anchor='c')
btn_delete = Button(win, text='Delete' , font= 'arial 13' , width=12 , bg= '#fffffb' , command= delete)
btn_delete.place(x= 478 , y= 370 , anchor='c')
btn_clear = Button(win, text='Clear' , font= 'arial 13' , width=12 , bg= '#fffffb' , command=clear)
btn_clear.place(x= 320 , y= 410 , anchor='c')
btn_fetch = Button(win, text='Fetch' , font= 'arial 13' , width=12 , bg= '#fffffb' , command=fetch)
btn_fetch.place(x= 478 , y= 410 , anchor='c')
btn_exit = Button(win, text='Exit' , font= 'arial 13' , width=28 , bg= '#fffffb' , command= leave)
btn_exit.place(relx=0.5 , y= 450 , anchor='c')
#-------------------
win.mainloop()