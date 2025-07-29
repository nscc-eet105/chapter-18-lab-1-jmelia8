#Joe Melia EET-107
import tkinter

class Converter:
    def __init__(self):
        self.window = tkinter.Tk()

        self.title = tkinter.Label(self.window, text = "Feet and Inches Converter")
        self.title.pack()
        self.inputs = tkinter.Frame(self.window)
        self.inputs.pack()
        self.feet_label = tkinter.Label(self.inputs, text = "Feet:")
        self.feet_label.pack(side = "left")
        self.feet_entry = tkinter.Entry(self.inputs, width=3)
        self.feet_entry.pack(side = "left")
        self.inches_label = tkinter.Label(self.inputs, text = "Inches:")
        self.inches_label.pack(side = "left")
        self.inches_entry = tkinter.Entry(self.inputs, width=3)
        self.inches_entry.pack(side = "left")
        self.result = tkinter.Frame(self.window)
        self.result.pack()
        self.total_label = tkinter.Label(self.result, text = "Inches:")
        self.total_label.pack()
        self.buttons = tkinter.Frame(self.window)
        self.buttons.pack()
        self.convert = tkinter.Button(self.buttons, text="Convert", command=self.convert)
        self.convert.pack(side="left")
        self.exit = tkinter.Button(self.buttons, text="Exit", command=self.window.destroy)
        self.exit.pack(side="left")
        
        tkinter.mainloop()

    def convert(self):
        feet = int(self.feet_entry.get())
        inches = int(self.inches_entry.get())
        total = feet * 12
        total += inches
        self.total_label.config(text=f"Inches: {total}")
Gui = Converter()
