import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Password Manager")       

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.von_ueberall_erreichbar = None
        self.frames = {}

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

        button = ttk.Button(self, text="New User",command=lambda: controller.show_frame(newUser))
        button.pack()

        button2 = ttk.Button(self, text="Returning User", command=lambda: controller.show_frame(returnUser))
        button2.pack()



class newUser(tk.Frame):

    def __init__(self, parent, controller):
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
        

        label = ttk.Label(self, text="Create a New Password", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.label2 = ttk.Label(self, text=controller.getVUE(), font=LARGE_FONT)
        self.label2.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Start Page",command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Main Menu",command=lambda: controller.show_frame(mainMenu))
        button2.pack()


class returnUser(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def close():
           self.quit()

        closeButton = ttk.Button(self, text="Close Program", command = close)
        closeButton.pack()

        def get_input():
           label.config(text=""+insertPass.get())

        insertPass = tk.Entry(self, show="*", width=15)
  
        insertPass.pack()

        buttonPrint = ttk.Button(self, text="Confirm Password", command=get_input)
        buttonPrint.pack()

        label = ttk.Label(self, text="Log In", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.label2 = ttk.Label(self, text=controller.getVUE(), font=LARGE_FONT)
        self.label2.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Start Page",command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Main Menu",command=lambda: controller.show_frame(mainMenu))
        button2.pack()

        
class mainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def close():
           self.quit()

        closeButton = ttk.Button(self, text="Close Program", command = close)
        closeButton.pack()

        label = ttk.Label(self, text="Pick an Option", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.label2 = ttk.Label(self, text=controller.getVUE(), font=LARGE_FONT)
        self.label2.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Add a Passwod", command=lambda: controller.show_frame(addPass))
        button1.pack()

        button2 = ttk.Button(self, text="Modify Password",command=lambda: controller.show_frame(modPass))
        button2.pack()

        button3 = ttk.Button(self, text="Delete a Password", command=lambda: controller.show_frame(delPass))
        button3.pack()

        button4 = ttk.Button(self, text="View Password List", command=lambda: controller.show_frame(viewPass))
        button4.pack()

class addPass(tk.Frame):

    def __init__(self, parent, controller):
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

        label = ttk.Label(self, text="Add a Password", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.label2 = ttk.Label(self, text=controller.getVUE(), font=LARGE_FONT)
        self.label2.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Main Menu",command=lambda: controller.show_frame(mainMenu))
        button1.pack()

        button2 = ttk.Button(self, text="Start Page",command=lambda: controller.show_frame(StartPage))
        button2.pack()


class modPass(tk.Frame):

    def __init__(self, parent, controller):
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

        label = ttk.Label(self, text="Delete a Password", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.label2 = ttk.Label(self, text=controller.getVUE(), font=LARGE_FONT)
        self.label2.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Main Menu", command=lambda: controller.show_frame(mainMenu))
        button1.pack()

        button2 = ttk.Button(self, text="Start Page",command=lambda: controller.show_frame(StartPage))
        button2.pack()

class viewPass(tk.Frame):

    def __init__(self, parent, controller):
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

        label = ttk.Label(self, text="View Password List", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.label2 = ttk.Label(self, text=controller.getVUE(), font=LARGE_FONT)
        self.label2.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Main Menu",command=lambda: controller.show_frame(mainMenu))
        button1.pack()

        button2 = ttk.Button(self, text="Start Page",command=lambda: controller.show_frame(StartPage))
        button2.pack()


app = Application()

# set window size
app.geometry("210x180+30+30")

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
app.config(menu=menubar) 


app.mainloop()
