from tkinter import *

root = Tk()
root.title('Apps')
root.geometry("500x450")


#clear function

def confirm():
    mylabel = Label(main_frame, text= clicked.get())
    mylabel.grid(row = 4, column = 1)

def submit():
    Xi_value.delete(0, END)
    Xu_value.delete(0, END)
    Err_value.delete(0, END)


#Mainframe
main_frame = Frame(root, bg= "white")
main_frame.pack(fill = BOTH, expand = 1)

mylabel = Label(main_frame, text ="Biseksi, Regulfasi, Secant", font=("times new roman", 20), bg="white")
mylabel.grid(row = 1, column = 1)

mylabel = Label(main_frame, text ="Choose the method :", font=("times new romaan", 10), bg="white")
mylabel.grid(row = 2, column = 0, pady = 10)


#Text Box
Xi_value = Entry(main_frame, width = 30, borderwidth = 2)
Xi_value.grid(row = 5, column = 1, pady = 10)

Xu_value = Entry(main_frame, width = 30, borderwidth = 2)
Xu_value.grid(row = 6, column = 1, pady = 10)

Err_value = Entry(main_frame, width = 30, borderwidth = 2)
Err_value.grid(row = 7, column = 1, pady = 10)

#Label


Xi_value_label = Label(main_frame, text="Xi Value :", bg= "white")
Xi_value_label.grid(row = 5, column = 0)

Xu_value_label = Label(main_frame, text="Xu Value :", bg = "white")
Xu_value_label.grid(row = 6, column = 0)

Err_value_label = Label(main_frame, text="Error Value :", bg = "white")
Err_value_label.grid(row = 7, column = 0)

#drop down box

clicked = StringVar()
clicked.set("Biseksi")

drop = OptionMenu(main_frame, clicked, "Biseksi", "Regulfasi", "Secant")
drop.grid(row = 2, column = 1)

#Button
compare_btn = Button (main_frame, text = "Compare", command = submit)
compare_btn.grid(row = 8, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 70)

confirm_btn = Button (main_frame, text = "Confirm", command = confirm)
confirm_btn.grid(row = 3, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 70)

quit_btn = Button (main_frame, text = "Exit Program", command = root.quit)
quit_btn.grid(row = 9, column = 0, columnspan = 2, pady = 100, padx = 10, ipadx = 70)


root.mainloop()