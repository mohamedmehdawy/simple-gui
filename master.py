import tkinter

class SimpleGui:
    def __init__(self):
        # create main window widget
        self.tk = tkinter.Tk()
        
        # set size for window
        self.tk.geometry("512x512")
        
        # set title for window
        self.tk.title('simple gui')
        
        # create frames
        self.top_frame = tkinter.Frame(self.tk)
        self.bottom_frame = tkinter.Frame(self.tk)
        
        # set labels and put it to top frame
        self.label1 = tkinter.Label(self.top_frame, text='hello world',borderwidth=2, relief='solid')
        self.label2 = tkinter.Label(self.top_frame, text='hello mohamed', borderwidth=2, relief='solid')
        self.label1.pack(ipadx=10, ipady=10, padx=10, pady=10)
        self.label2.pack(ipadx=10, ipady=10, padx=10, pady=10)
        
        # set labels and put it to bottom fram
        self.label2 = tkinter.Label(self.bottom_frame, text='my age is 32',borderwidth=2, relief='solid')
        self.label3 = tkinter.Label(self.bottom_frame, text='bla bla bla', borderwidth=2, relief='solid')
        self.label2.pack(ipadx=10, ipady=10, padx=10, pady=10, side='left')
        self.label3.pack(ipadx=10, ipady=10, padx=10, pady=10, side='left')
        
        # register frames to main window
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        # enter the program to main loop
        self.tk.mainloop()
        
# create instance from simple gui class
if __name__ == "__main__":
    gui = SimpleGui()
        