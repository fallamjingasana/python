from tkinter import *
from datetime import date
root = Tk()

root.title('grtting started with widgets')
root.geometry('400x200')

lbl = Label(text = 'hey theyre', fg ='white',bg ='blue',height=1,width=300,)

name_lbl = Label(text='full name',bg='blue')
name_entry =Entry()

def display():
    name= name_entry.get()
    global Message
    Message = 'welcom to the aplication \n todays date is :'
    greet = 'hello' + name +'\n'

    text_box.insert(EMD,greet)
    text_box.insert(EMD,message)
    text_box.insert(EMD,today())
text_box = Text(height=5)

btn = Button(text='begin', command = display,height=1,fg='red',bg='cyan')

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()