from tkinter import *
import tkinter.messagebox as tkMessageBox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):        
        self.v1 = IntVar() # check button will modify the value
        # create check button
        # if selected, v1=1; else v1=0
        self.cbt = Checkbutton(self, text="Bold", variable=self.v1,
                              command=self.hello)
        self.cbt.pack()
        
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        tkMessageBox.showinfo('Message', 'Hello, v1={0}'.format(self.v1.get()) )

        
app = Application()
# create window title
app.master.title('Hello World')
# create msg loop
app.mainloop()
