from tkinter import *
from tkinter import messagebox



root = Tk()
root.title('Лабораторная 3')
root.geometry('300x400')

l = Label(root, bg='white', width=20, text='Задание 1')
l.pack()


def click_button():
    i = int(0)
    if (var1.get() == 1):
        i=i+int(30)
    if (var2.get() == 1):
        i=i+int(20)
    if (var3.get() == 1):
        i=i+int(100)
    if (var4.get() == 1):
        i=i+int(144)
    if (var5.get() == 1):
        i=i+int(34)
    if (var6.get() == 1):
        i=i+int(46)

    messagebox.showinfo("Стоимость: ", i)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()

c1 = Checkbutton(root, text='Помидоры',variable=var1, onvalue=1, offvalue=0)
c1.pack()
c2 = Checkbutton(root, text='Капуста',variable=var2, onvalue=1, offvalue=0)
c2.pack()
c3 = Checkbutton(root, text='Компот',variable=var3, onvalue=1, offvalue=0)
c3.pack()
c4 = Checkbutton(root, text='Колбаса',variable=var4, onvalue=1, offvalue=0)
c4.pack()
c5 = Checkbutton(root, text='МОлоко',variable=var5, onvalue=1, offvalue=0)
c5.pack()
c6 = Checkbutton(root, text='Конфеты',variable=var6, onvalue=1, offvalue=0)
c6.pack()


btn = Button(text="Рассчитать", command =click_button )
btn.pack()


l = Label(root, bg='white', width=20, text='Задание 3')
l.pack()

main_menu = Menu()
file_menu = Menu()
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit")
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit")
main_menu.add_cascade(label="View")
root.config(menu=main_menu)


listbox_items = ['Раз', 'Два', 'Три']

def select_item(event):
    value = (listbox.get(listbox.curselection()))
    print(value)


listbox = Listbox(root, width=40, height=5, font=('times', 13))
listbox.bind('<<ListboxSelect>>', select_item)
listbox.place(x=15, y=15)

for item in listbox_items:
    listbox.insert(END, item)




root.mainloop()
