import tkinter

class SimpleGui:
    def __init__(self):
        # create main window widget
        self.tk = tkinter.Tk()
        
        # set size for window
        self.tk.geometry("512x512")
        
        # set title for window
        self.tk.title('simple gui')
        
        # set label and put it to window
        self.label1 = tkinter.Label(self.tk, text='hello world',borderwidth=2, relief='groove')
        self.label2 = tkinter.Label(self.tk, text="hello mohamed")
        self.label1.pack(side="left")
        self.label2.pack(side="left")
        
        
        # enter the program to main loop
        self.tk.mainloop()
        
# create instance from simple gui class
if __name__ == "__main__":
    gui = SimpleGui()
        