from tkinter import *

def btnClick(item):
	tmp=str(text_Input.get())
	text_Input.set(tmp+item)

def btnClear():
	text_Input.set('')

def btnEq():
	tmp=str(text_Input.get())
	s=eval(tmp)
	text_Input.set(s)


cal=Tk()
cal.title("Calculator") 
text_Input=StringVar()



textDisplay=Entry(cal,font=('arial',15,'bold'),bg='plum',bd=20,justify='right',width=25,textvariable=text_Input).grid(row=0,columnspan=5)

btn7=Button(cal,font=('arial',20,'bold'),width=4,text='7',fg='blue',bg='tan',bd=10,command=lambda:btnClick('7')).grid(row=1,column=0)
btn8=Button(cal,font=('arial',20,'bold'),width=4,text='8',fg='blue',bg='tan',bd=10,command=lambda:btnClick('8')).grid(row=1,column=1)
btn9=Button(cal,font=('arial',20,'bold'),width=4,text='9',fg='blue',bg='tan',bd=10,command=lambda:btnClick('9')).grid(row=1,column=2)
c=Button(cal,font=('arial',20,'bold'),width=4,text='c',fg='blue',bg='red',bd=10,command=lambda:btnClear()).grid(row=1,column=3)

btn4=Button(cal,font=('arial',20,'bold'),width=4,text='4',fg='blue',bg='tan',bd=10,command=lambda:btnClick('4')).grid(row=2,column=0)
btn5=Button(cal,font=('arial',20,'bold'),width=4,text='5',fg='blue',bg='tan',bd=10,command=lambda:btnClick('5')).grid(row=2,column=1)
btn6=Button(cal,font=('arial',20,'bold'),width=4,text='6',fg='blue',bg='tan',bd=10,command=lambda:btnClick('6')).grid(row=2,column=2)
minus=Button(cal,font=('arial',20,'bold'),width=4,text='-',fg='blue',bg='orange',bd=10,command=lambda:btnClick('-')).grid(row=2,column=3)

btn1=Button(cal,font=('arial',20,'bold'),width=4,text='1',fg='blue',bg='tan',bd=10,command=lambda:btnClick('1')).grid(row=3,column=0)
btn2=Button(cal,font=('arial',20,'bold'),width=4,text='2',fg='blue',bg='tan',bd=10,command=lambda:btnClick('2')).grid(row=3,column=1)
btn3=Button(cal,font=('arial',20,'bold'),width=4,text='3',fg='blue',bg='tan',bd=10,command=lambda:btnClick('3')).grid(row=3,column=2)
mult=Button(cal,font=('arial',20,'bold'),width=4,text='*',fg='blue',bg='orange',bd=10,command=lambda:btnClick('*')).grid(row=3,column=3)

polint=Button(cal,font=('arial',20,'bold'),width=4,text='=',fg='blue',bg='green',bd=10,command=lambda:btnEq()).grid(row=4,column=0)
btn0=Button(cal,font=('arial',20,'bold'),width=4,text='0',fg='blue',bg='tan',bd=10,command=lambda:btnClick('0')).grid(row=4,column=1)
div=Button(cal,font=('arial',20,'bold'),width=4,text='/',fg='blue',bg='orange',bd=10,command=lambda:btnClick('/')).grid(row=4,column=2)
pilus=Button(cal,font=('arial',20,'bold'),width=4,text='+',fg='blue',bg='orange',bd=10,command=lambda:btnClick('+')).grid(row=4,column=3)









cal.mainloop()