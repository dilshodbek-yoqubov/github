
from datetime import datetime
from tkinter import *

screen=Tk()
screen.title('Calculation')
screen.geometry('300x300')

result=Label(text='Result',bg='red')
result.place(x=90,y=135,width=120,height=40)

year=Entry()
year.place(x=75,y=50,width=150,height=30)

def difference():
    today=datetime.today()
    result.config(text=today.year-int(year.get()))
    
button=Button(text='Calculation',command=difference)
button.place(x=90,y=90,width=120,height=40)


screen.mainloop()