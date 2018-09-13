#coding=utf-8
from tkinter import *
 
class WidgetsDemo:
    def __init__(self):
        window = Tk()                 # ����һ������
        window.title("Widgets Demo")  # ���ñ���
        
        frame1 = Frame(window)        # ����һ�����
        frame1.pack()                 # �����frame1������window��
        
        self.v1 = IntVar()
        # ����һ����ѡ�����ѡ����self.v1Ϊ1,����Ϊ0,�����cbtBoldʱ������processCheckbutton����
        cbtBold = Checkbutton(frame1,text="Bold",variable=self.v1,
                              command=self.processCheckbutton)
        
        self.v2 = IntVar()
        # ����������ѡ��ť��������frame1�У���ť�ı��Ƿֱ���Red��Yellow������ɫ�ֱ��Ǻ�ɫ�ͻ�ɫ��
        # ��rbRed��ť��ѡ��ʱself.v2Ϊ1,��rbYellow��ť��ѡ��ʱ��self.v2Ϊ2����ť�����ʱ����processRadiobutto����
        rbRed = Radiobutton(frame1,text="Red",bg="red",
                            variable=self.v2,value=1,
                            command=self.processRadiobutton)
        rbYellow = Radiobutton(frame1,text="Yellow",bg="yellow",
                               variable=self.v2,value=2,
                               command=self.processRadiobutton)
        # grid����
        cbtBold.grid(row=1,column=1)
        rbRed.grid(row=1,column=2)
        rbYellow.grid(row=1,column=3)
        
        frame2 = Frame(window)   # �������frame2
        frame2.pack()            # ��frame2������window��
        
        
        label = Label(frame2,text="Enter your name: ")   # ������ǩ
        self.name = StringVar()
        # ����Entry����������self.name����
        entryName = Entry(frame2,textvariable=self.name)
        # ������ť�������ťʱ����processButton����
        btGetName = Button(frame2,text="Get Name",
                           command=self.processButton)
        
        # ������Ϣ
        message = Message(frame2,text="It is a widgets demo")
        
        # grid����
        label.grid(row=1,column=1)
        entryName.grid(row=1,column=2)
        btGetName.grid(row=1,column=3)
        message.grid(row=1,column=4)
        
        # ������ʽ���ı�����������window��
        text = Text(window)
        text.pack()
        text.insert(END,"Tip\nThe best way to learn Tkinter is to read")
        text.insert(END,"these carefully designed examples and use them")
        text.insert(END,"to create your applications.")
        
        # ����¼�ֱ��window���ر�
        window.mainloop()
    
    # ��ѡ������ť����
    def processCheckbutton(self):
        print ("Check button is:" 
               + ("checked" if self.v1.get() == 1 else "unchecked"))
    
    # ��ѡ��ť�������
    def processRadiobutton(self):
        print (("Red" if self.v2.get() == 1 else "Yellow")
               + " is selected.")
    
    # Get Name��ť�������
    def processButton(self):
        print ("Your name is " + self.name.get())
    
WidgetsDemo()
