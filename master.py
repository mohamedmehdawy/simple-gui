import tkinter
import tkinter.messagebox
class SimpleGui:
    def __init__(self):
        # create main window widget
        self.main_window = tkinter.Tk()
        
        print(dir(self.main_window))
        # set size for window
        self.main_window.geometry("512x512")
        
        # set title for window
        self.main_window.title('simple gui')
        
        # create button when user click him the show method will excute
        self.button = tkinter.Button(self.main_window, text='click me to show my name', command=self.show)
        
        # create quit button
        self.quit = tkinter.Button(self.main_window, text='quit', command=self.main_window.destroy)
        
        # pack buttons
        self.button.pack(ipadx=20, ipady=20)
        self.quit.pack(pady=50)

        # enter the program to main loop
        self.main_window.mainloop()
    def show(self) -> None:
        """
            this function render info dialog box
        """
        tkinter.messagebox.showinfo('name', 'my name is mohamed')
# create instance from simple gui class
if __name__ == "__main__":
    gui = SimpleGui()
        