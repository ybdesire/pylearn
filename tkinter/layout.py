from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel1 = Label(self, text='Hello, world!')
        #self.helloLabel1.pack()
        self.helloLabel2 = Label(self, text='222222Hello, world!222222')
        #self.helloLabel2.pack()
        self.helloLabel3 = Label(self, text='333333Hello, world!333333')
        #self.helloLabel3.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        #self.quitButton.pack()
        # layout
        self.helloLabel1.grid(row=1,column=1)
        self.helloLabel2.grid(row=1,column=2)
        self.helloLabel3.grid(row=2,column=1)
        self.quitButton.grid(row=2,column=2)

        
app = Application()
# create window title
app.master.title('Hello World')
# create msg loop
app.mainloop()
