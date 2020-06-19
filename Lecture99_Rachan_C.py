from tkinter import *
import math

def leftClick(event):
    bmi = (float(textBoxWeight.get())/math.pow((float(textBoxHeight.get())/100),2))
    print('Your BMI is: ', bmi)
    if bmi >=30:
        labelResult.configure(text='DANGER!!')
    elif bmi >=25:
        labelResult.configure(text='More than Over Weight')
    elif bmi >=23:
        labelResult.configure(text='Over Weight')
    elif bmi >= 18.6:
        labelResult.configure(text='Good')
    elif bmi <=18.5:
        labelResult.configure(text='Under Weight')




main = Tk()
labelHeight = Label(main, text='Height (cm.)').grid(row=0, column=0)
textBoxHeight = Entry(main)
textBoxHeight.grid(row=0, column=1)
labelWeight = Label(main, text='Weight (Kg.)').grid(row=1, column=0)
textBoxWeight = Entry(main)
textBoxWeight.grid(row=1, column=1)
calculateButton = Button(main, text='Calculate')
calculateButton.grid(row=2)
calculateButton.bind('<Button-1>',leftClick)
labelResult = Label(main, text='Result')
labelResult.grid(row=2, column=1)
main.mainloop()