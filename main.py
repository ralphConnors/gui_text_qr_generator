from tkinter import *
import commands, mainProcess

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Text QR Code Generator - 1.5 - KDTal1")
        self.resizable(False, False)

        self.frame1 = main_frame1(self)
        self.frame1.grid(row=0, column=0, padx=20, pady=20)
        self.frame2 = main_frame2(self, self.frame1)
        self.frame2.grid(row=0, column=1, padx=20, pady=20)

class main_frame1(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_title = Label(self, text="Text QR Code Generator", font=('Arial', 20))
        self.label_desc = Label(self, text="Enter anything in the textbox", font=("Arial", 11, "italic"))
        self.entry = Entry(self, width=30, font=('Arial', 17))
        self.label_features = Label(self, text="- - - - - - - - - - - - MODES - - - - - - - - - - - -", font=('Helvetica', 15))
        self.label_desc2 = Label(self, text="Then, press the button to generate QR Code", font=("Arial", 11, "italic"))
        
        self.target = frame_subFrame1(self)
        
        self.buttonGenerate = Button(self, text="GENERATE", command=lambda: [mainProcess.generate_qr(commands.qrCode_folder, commands.error_messages, self.target.choice_Feature, self.entry), mainProcess.view_qr(commands.error_messages)], font=('Arial', 15))

        for variables in [self.label_title, self.label_desc, self.entry, self.label_desc2, self.buttonGenerate, self.label_features, self.target]:
            variables.pack(pady=7, fill='x', expand=True)

class main_frame2(Frame):
    def __init__(self, master, target):
        super().__init__(master)

        self.target = target

        self.label_file = Label(self, text="Or, you can browse a file you can turn into a QR Code.", wraplength=250, justify="center", font=('Helvetica', 10))
        self.label_file.pack(pady=10)

        for textIn, btnCommand, colorBtn in [ # In loop to optimize, and it looks good in readability.
            ("BROWSE FILE", lambda: commands.browse_file(self.target.entry), "#67B174"),
            ("CLEAR", lambda: commands.clear_entry(self.target.entry), "powder blue"),
            ("OPEN STORAGE", lambda: commands.open_folder(), "powder blue"),
            ("ABOUT", lambda: commands.about(), "powder blue")
        ]:
            Button(
                self, 
                text=textIn, 
                command=btnCommand, 
                width=25,
                font=('Helvetica', 15),
                bg=colorBtn
            ).pack(pady=10, fill='x', expand=True)

class frame_subFrame1(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.choice_Feature = StringVar(value="0")
        
        for featTxt, val, rowNum, colNum in [ # In loop to optimize, and it looks good in readability.
            ("Normal", "0", "0", "0"),
            ("Binary", "1", "0", "1"),
            ("Consochain", "2", "0", "2"),
            ("Reverse", "3", "0", "3"),
            ("Effigy", "4", "0", "4")
        ]:
            Radiobutton(
                self, 
                variable=self.choice_Feature, 
                text=featTxt, 
                value=val
            ).grid(
                row=rowNum,
                column=colNum,
                padx=2,
                pady=2
            )

if __name__ == "__main__":
    app = App()
    app.mainloop()