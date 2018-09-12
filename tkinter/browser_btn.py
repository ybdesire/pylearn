from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.alertButton = Button(self, text='SelectFile', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        filename = filedialog.askopenfilename()
        messagebox.showinfo('Message', 'file:{0}'.format(filename))

        
app = Application()
# create window title
app.master.title('Hello World')
# create msg loop
app.mainloop()
