import keyword
import tkinter as tk
from tkinter import StringVar, ttk
from PassManager import *
from backend.removepassword import *
import csv
import pandas
from pandas import *
import time
LARGE_FONT = ("Verdana", 12)


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Password Manager")  
        global app_data 
        self.app_data= {"key":StringVar(), "table":pandas.DataFrame()}  #place to store key outside of each page IMPORTANT   

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.von_ueberall_erreichbar = None
        self.frames = {}

        def get_key(self):
            return self.controller.app_data["key"].get()

        for F in (StartPage, newUser, returnUser,mainMenu, addPass, modPass, delPass, viewPass):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def getVUE(self):
        return self.von_ueberall_erreichbar



    def show_frame(self, targetFrame):
        frame = self.frames[targetFrame]
        self.frames[targetFrame].label2.config(text=self.getVUE())
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = ttk.Label(self, text="Welcome to Password Manager", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.label2 = ttk.Label(self, text=controller.getVUE(), font=LARGE_FONT)
        self.label2.pack(pady=10,padx=10)

            

        if ("key.key.zip" in os.listdir()) and ("Vault.csv" in os.listdir()):
            button2 = ttk.Button(self, text="Returning User", command=lambda: controller.show_frame(returnUser))
            button2.pack()
        else:
            button = ttk.Button(self, text="New User",command=lambda: controller.show_frame(newUser))
            button.pack()



class newUser(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def close():
           self.quit()

        closeButton = ttk.Button(self, text="Close Program", command = close)
        closeButton.pack()
        label = ttk.Label(self, text="Input Matching Password", font=LARGE_FONT).pack(pady=10,padx=10)
        inputlabel = ttk.Label(self, text="After inputting matching\npassword, program will close.\nPlease restart to access features.", font=("Arial",10))
        inputlabel.configure(anchor=tk.CENTER)
        inputlabel.pack(pady=10,padx=10)
        enteredPass = tk.StringVar()
        enteredPassConfirm = tk.StringVar()
           
        insertPass = tk.Entry(self, show="*", width=15, textvariable=enteredPass)
        insertPass.pack()

        verPass = tk.Entry(self, show="*", width=15)
        verPass.pack()
        #global label
        
        def start_setup(self):#the next class called needs to be from here, (menu), and the fernet key needs to be passed as a parameter to said class
            if insertPass.get() == verPass.get() and (insertPass.get() != "" or verPass.get() != ""):
                #label.set("We're Setting up your account. Please restart after program closes")
                initialSetup(insertPass.get(), verPass.get())
                
                ttk.Label(self, text="We're Setting up your account. Please restart program after it closes", font=LARGE_FONT).pack(pady=10,padx=10)
                app.destroy()
            else:
                label = ttk.Label(self, text="Error: Non Matching Password", font=LARGE_FONT).pack(pady=10,padx=10)
                insertPass.delete(0, tk.END)
                verPass.delete(0, tk.END)
        
        
        buttonPrint = ttk.Button(self, text="Confirm Password", command=lambda: start_setup(self)).pack()
    

        self.label2 = ttk.Label(self, text=controller.getVUE(), font=LARGE_FONT)
        self.label2.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Start Page",command=lambda: controller.show_frame(StartPage))
        button1.pack()


class returnUser(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        
        def close():
           self.quit()

        closeButton = ttk.Button(self, text="Close Program", command = close)
        closeButton.pack()
        key_var = ""
        def check(self):#the next class called needs to be from here, (menu), and the fernet key needs to be passed as a parameter to said class
            var = getFernetKey(insertPass.get())
            self.controller.app_data["key"]  = var #sending the key to the controller to be stores in memory IMPORTANT
            controller.show_frame(mainMenu)
        insertPass = tk.Entry(self, show="*", width=15)
  
        insertPass.pack()

        buttonPrint = ttk.Button(self, text="Confirm Password", command=lambda: check(self)).pack()

        label = ttk.Label(self, text="Log In", font=LARGE_FONT).pack(pady=10,padx=10)

        self.label2 = ttk.Label(self, text=controller.getVUE(), font=LARGE_FONT)
        self.label2.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Start Page",command=lambda: controller.show_frame(StartPage))
        button1.pack()

        
class mainMenu(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        key = self.controller.app_data["key"].get() #GETTING THE KEY! IMPORTANT AS FUCK!!!!!!!!
        #print(key)
        tk.Frame.__init__(self, parent)

        def close():
           self.quit()

        closeButton = ttk.Button(self, text="Close Program", command = close)
        closeButton.pack()

        label = ttk.Label(self, text="Pick an Option", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.label2 = ttk.Label(self, text=controller.getVUE(), font=LARGE_FONT)
        self.label2.pack(pady=10,padx=10)
        def getAllPass(self, key):
            table = (viewPasswordTable(key))#KEY PASSED TO FUNCTION STRICTLY LIKE THIS
            #print(table)
            self.controller.app_data["table"] = viewPasswordTable(key)
            #self.controller.app_data["table"] = table
            self.controller.show_frame(viewPass)



        button1 = ttk.Button(self, text="Add a Passwod", command=lambda: controller.show_frame(addPass))
        button1.pack()

        button2 = ttk.Button(self, text="Modify Password",command=lambda: controller.show_frame(modPass))
        button2.pack()

        button3 = ttk.Button(self, text="Delete a Password", command=lambda: controller.show_frame(delPass))
        button3.pack()

        button4 = ttk.Button(self, text="View Password List", command=lambda: getAllPass(self, self.controller.app_data["key"]))#KEY PASSED STRICTLY LIKE THIS
        button4.pack()

class addPass(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)

        def close():
           self.quit()

        closeButton = ttk.Button(self, text="Close Program", command = close)
        closeButton.pack()


        inputlabel = ttk.Label(self, text="Input Name Associated\nFor Generated Password:", font=("Arial",10)).pack(pady=10,padx=10)
        #verPass = tk.Entry(self, show="", width=15).pack()
        def genPass(self, key):
            name = insertPass.get()
            addToPasswordTable(key, name)
            insertPass.delete(0, tk.END)
        
        insertPass = tk.Entry(self, show="", width=15)
  
        insertPass.pack()

        buttonPrint = ttk.Button(self, text="Generate Password", command=lambda: genPass(self, self.controller.app_data["key"])).pack()

        label = ttk.Label(self, text="Add a Password", font=LARGE_FONT).pack(pady=10,padx=10)

        self.label2 = ttk.Label(self, text=controller.getVUE(), font=LARGE_FONT)
        self.label2.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Main Menu",command=lambda: controller.show_frame(mainMenu))
        button1.pack()

        button2 = ttk.Button(self, text="Start Page",command=lambda: controller.show_frame(StartPage))
        button2.pack()


class modPass(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)

        def close():
           self.quit()

        closeButton = ttk.Button(self, text="Close Program", command = close)
        closeButton.pack()

        def get_input():
           label.config(text=""+insertPass.get())

        insertPass = tk.Entry(self, show="*", width=15)
  
        insertPass.pack()

        verPass = tk.Entry(self, show="*", width=15)
        verPass.pack()

        buttonPrint = ttk.Button(self, text="Confirm Password", command=get_input)
        buttonPrint.pack()

        label = ttk.Label(self, text="Modify a Password", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.label2 = ttk.Label(self, text=controller.getVUE(), font=LARGE_FONT)
        self.label2.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Main Menu", command=lambda: controller.show_frame(mainMenu))
        button1.pack()

        button2 = ttk.Button(self, text="Start Page", command=lambda: controller.show_frame(StartPage))
        button2.pack()

class delPass(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)

        def close():
           self.quit()

        closeButton = ttk.Button(self, text="Close Program", command = close)
        closeButton.pack()

        def get_input():
           label.config(text=""+insertPass.get())

        insertPass =  tk.Entry(self, show="*", width=15)
  
        insertPass.pack()

        verPass = tk.Entry(self, show="*", width=15)
        verPass.pack()

        buttonPrint = ttk.Button(self, text="Confirm Password", command=get_input)
        buttonPrint.pack()

        label = ttk.Label(self, text="delete a password", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.label2 = ttk.Label(self, text=controller.getVUE(), font=LARGE_FONT)
        self.label2.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Main Menu", command=lambda: controller.show_frame(mainMenu))
        button1.pack()

        button2 = ttk.Button(self, text="Start Page",command=lambda: controller.show_frame(StartPage))
        button2.pack()

class viewPass(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        print("addpass", self.controller.app_data["key"].get())
        tk.Frame.__init__(self, parent)

        def close():
           self.quit()

        closeButton = ttk.Button(self, text="Close Program", command = close)
        closeButton.pack()

        
        text2 = tk.Text(self)
        
        def buildTable(self, table):
            text2.delete(1.0,"end")
            text2.insert(1.0, str(table.iloc[0:len(table),0:len(table.columns)]))
            text2.tag_configure("text2", justify=tk.CENTER)
            text2.pack()
        def hideTable(self):
            text2.delete(1.0,"end")


        buttonPrint = ttk.Button(self, text="Show table", command= lambda: buildTable(self,self.controller.app_data["table"])).pack()
        buttonPrint2 = ttk.Button(self, text="Hide table", command= lambda: buildTable(self,self.controller.app_data["table"])).pack()
        label = ttk.Label(self, text="table here", font=LARGE_FONT)#have to create the when viewPass button is clicked, then store it as controller variable, then open in viewPass class
        label.pack(pady=10,padx=10)

        self.label2 = ttk.Label(self, text=controller.getVUE(), font=LARGE_FONT)
        self.label2.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Main Menu",command=lambda: controller.show_frame(mainMenu))
        button1.pack()

        button2 = ttk.Button(self, text="Start Page",command=lambda: controller.show_frame(StartPage))
        button2.pack()





app = Application()

# set window size
app.minsize(width=900, height=600)

# init menubar
menubar = tk.Menu(app)

# creating the menus
menuManage = tk.Menu(menubar, tearoff=0)

# list of menubar elements
menubar.add_cascade(menu=menuManage, label="Frame")

# menu: manage
menuManage.add_command(label="viewPass", command=lambda: app.show_frame(viewPass))
menuManage.add_command(label="delPass", command=lambda: app.show_frame(delPass))
menuManage.add_command(label="modPass", command=lambda: app.show_frame(modPass))
menuManage.add_command(label="addPass", command=lambda: app.show_frame(addPass))
menuManage.add_command(label="Main Menu", command=lambda: app.show_frame(mainMenu))
menuManage.add_command(label="newUser", command=lambda: app.show_frame(newUser))
menuManage.add_command(label="returnUser", command=lambda: app.show_frame(returnUser))
menuManage.add_command(label="Start Page", command=lambda: app.show_frame(StartPage))

# attach menubar
#app.config(menu=menubar) 


app.mainloop()
