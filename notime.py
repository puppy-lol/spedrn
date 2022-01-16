from tkinter import *
import random
root = Tk()

root.title("TESTING RANDOM FUENCITON")
root.geometry("500x500")
input_password = Entry(root)
guessed_password_label = Label(root)
generated_password_label = Label(root)

array_3d = [[["I", "J", "K", "L", "M", "N", "O", "P"], ["King", "Queen"], ["!", "@", "#", "$", "%", "^", "&", "*"]]]
print(array_3d[0][2][3])

def new_password(): 
    guessed_password_label["text"] = "Guessed Password: " + input_password.get()
    
    r1 = random.randint(0,5)
    r2 = random.randint(0,1)
    r3 = random.randint(0,7)
    
    letter1 = array_3d[0][0][r1]
    letter2 = array_3d[0][1][r2]
    letter3 = array_3d[0][2][r3]
    
    generated_password_label["text"] = "Generated Password: " + letter1 + "" + letter2 + "" + letter3
    
    
input_password.place(relx = 0.5, rely =0.3, anchor = CENTER)

guessed_password_label.place(relx = 0.5, rely =0.4, anchor = CENTER)

btn = Button(root, text= "new password", command = new_password)
btn.place(relx = 0.5, rely =0.5, anchor = CENTER)

generated_password_label.place(relx = 0.5, rely =0.6, anchor = CENTER)
root.mainloop()