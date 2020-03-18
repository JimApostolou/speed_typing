from tkinter import *
import random
import time

root = Tk()
root.title('Speed Typing')


def start():
    global start,new
    e.delete(0,END)
    x = random.randint(1,6)
    f = open('sentences.txt','r')
    for i in range(x):
        f.readline()
    new = f.readline()
    f.close()
    label_text.configure(text=new)
    label_text.grid(row=0, column=0, columnspan=2)   
    start = time.time()


def confirm():
    end = time.time()
    counter = 1
    check = e.get()
    for i in range(len(check)):
        if(check[i] == new[i]):
            counter += 1
    if(counter != 1):
        value = counter/len(new)*100
        label_accuracy = Label(root, text='Accuracy: {}%'.format(round(value,2)))
        label_accuracy.grid(row=3, column=0)
        label_time = Label(root, text='Time: {} sec.'.format(round((end-start),2)))
        label_time.grid(row=3, column=1)
    else:
        label_accuracy = Label(root, text='Accuracy: 0%')
        label_accuracy.grid(row=3, column=0)
        label_time = Label(root, text='Time: {} sec.'.format(round((end-start),2)))
        label_time.grid(row=3, column=1)


label_text = Label(root, text='Here will be the text once you start')
label_text.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=50, border=5)
e.grid(row=1, column=0, columnspan=2)
button_start = Button(root, text='Start/Next', command=start)
button_start.grid(row=2, column=0)
button_confirm = Button(root, text='Confirm', command=confirm)
button_confirm.grid(row=2, column=1)

root.mainloop()