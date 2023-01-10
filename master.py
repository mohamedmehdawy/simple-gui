import tkinter

class SimpleGui:
    def __init__(self):
        # create main window widget
        self.tk = tkinter.Tk()
        # set titlte for window
        self.tk.title('simple gui')
        # enter the program to main loop
        self.tk.mainloop()
        
# create instance from simple gui class
if __name__ == "__main__":
    gui = SimpleGui()
        