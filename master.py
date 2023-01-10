import tkinter
class SimpleConvertGUI:
    """
        this program convert distance from kilo to meter
    """
    def __init__(self):
        # create main window widget
        self.main_window = tkinter.Tk()
        
        # set size for window
        self.main_window.geometry("512x512")
        
        # frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        # set top frame widgets
        self.label = tkinter.Label(self.top_frame, text='enter a distance in kilometers:')
        self.input = tkinter.Entry(self.top_frame)
        self.label.pack(side='left')
        self.input.pack(side='left')
        
        # set mid frame widgets
        self.value = tkinter.StringVar()
        self.desc = tkinter.Label(self.mid_frame, text='result = ')
        self.result = tkinter.Label(self.mid_frame, textvariable=self.value)
        self.unit = tkinter.Label(self.mid_frame, text='meter')
        
        self.desc.pack(side='left')
        self.result.pack(side='left')
        self.unit.pack(side='left')
        
        # set bottom frame widgets
        self.convert_button = tkinter.Button(self.bottom_frame, text='convert', command=self.convert)
        self.quit = tkinter.Button(self.bottom_frame, text='quit', command=self.main_window.destroy)
        
        self.convert_button.pack(side='left', padx=20)
        self.quit.pack(side='left')
        
        # pack frames
        self.top_frame.pack()
        self.mid_frame.pack(pady=20)
        self.bottom_frame.pack()
        
        # enter tkinter to main loop
        self.main_window.mainloop()
    def convert(self):
        """
        this function convert distance from kilo to meter
        """
        distance = float(self.input.get())
        meter = distance * 1000
        self.value.set(meter)
# create instance from simple gui class
if __name__ == "__main__":
    gui = SimpleConvertGUI()
        