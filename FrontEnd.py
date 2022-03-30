#Resource https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python
from tkinter import *
#importing functions from backend for GUI input capability
#from backend.PassManager import *

window=Tk()
#button options for program
btn=Button(window, text="This is Button widget", fg='blue')
#Add this part for referncing a function from backend command = viewPasswordTable(key)
btnAdd=Button(window, text="Add a password", fg='green', )
btnEdit=Button(window, text="Edit a stored password", fg='green', )
btnViewAll=Button(window, text="View stored passwords", fg='green', )
btn.place(x=80, y= 100)
btnAdd.place(x=40, y=50)
window.title('CryptVault - Secure Password Manager')
window.geometry("450x200+600+300")
window.mainloop()

#updates on click - using command as a BUTTON passed variable

#add pass(involves new pass generation), view pass, modify pass,
#delete pass(name, pass, entry) - different key generation ?
