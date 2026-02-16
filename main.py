from tkinter import *
from tkinter import messagebox
from app_functions import AppFunctions
from PIL import ImageTk

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Text QR Code Generator")
        self.resizable(False, False)

        app_ctrl = AppFunctions()
        app_ctrl.json_variable()

        self.frame3 = main_frame3(self, app_ctrl)
        self.frame1 = main_frame1(self, self.frame3, app_ctrl)
        self.frame1.grid(row=0, column=0, padx=20, pady=20)
        self.frame2 = main_frame2(self, self.frame1, app_ctrl)
        self.frame2.grid(row=0, column=1, padx=20, pady=20)
        self.frame3.grid(row=0, column=2, columnspan=2, padx=20, pady=20)

class main_frame1(Frame):
    def __init__(self, master, qr_frame, app_ctrl):
        super().__init__(master)

        self.qr_frame = qr_frame
        self.app_ctrl = app_ctrl

        self.label_title = Label(self, text="Text QR Code Generator", font=('Arial', 20))
        self.label_desc = Label(self, text="Enter anything in the textbox", font=("Arial", 11, "italic"))
        self.entry = Entry(self, width=30, font=('Arial', 17))
        self.label_features = Label(self, text="- - - - - - - - - - - - MODES - - - - - - - - - - - -", font=('Helvetica', 15))
        self.label_desc2 = Label(self, text="Then, press the button to generate QR Code", font=("Arial", 11, "italic"))
        
        self.target = frame_subFrame1(self)
        
        self.buttonGenerate = Button(self, text="GENERATE", command=self.generate_and_view, font=('Arial', 15))

        for variables in [self.label_title, self.label_desc, self.entry, self.label_desc2, self.buttonGenerate, self.label_features, self.target]:
            variables.pack(pady=7, fill='x', expand=True)

    def generate_and_view(self):
        self.app_ctrl.data = self.entry.get()
        self.app_ctrl.choice_Feature = self.target.choice_Feature
        self.app_ctrl.generate_qr()
        self.qr_frame.view_qr()


class main_frame2(Frame):
    def __init__(self, master, target, app_ctrl):
        super().__init__(master)

        self.target = target
        self.app_ctrl = app_ctrl

        self.label_file = Label(self, text="Or, you can browse a file you can turn into a QR Code.", wraplength=250, justify="center", font=('Helvetica', 10))
        self.label_file.pack(pady=10)

        for textIn, btnCommand, colorBtn in [ # In loop to optimize, and it looks good in readability.
            ("BROWSE FILE", lambda: self.app_ctrl.browse_file(self.target.entry), "#67B174"),
            ("CLEAR", lambda: self.app_ctrl.clear_entry(self.target.entry), "powder blue"),
            ("OPEN STORAGE", lambda: self.app_ctrl.open_qr_folder(), "powder blue"),
            ("ABOUT", lambda: self.about(), "powder blue")
        ]:
            Button(
                self, 
                text=textIn, 
                command=btnCommand, 
                width=25,
                font=('Helvetica', 15),
                bg=colorBtn
            ).pack(pady=10, fill='x', expand=True)
    
    def about(self):
        messagebox.showinfo("Text QR Code Generator", 
                        "Forked from KDTal1's original 'python-gui_text_qr_generator'. ")

class main_frame3(Frame): # Window for QR Code view
    def __init__(self, master, app_ctrl):
        super().__init__(master)

        self.app_ctrl = app_ctrl

        self.label = Label(self, text="TEXT QR CODE GENERATED:", font=("Helvetica", 12))
        self.label.pack(pady=10)
        self.qr_label = Label(self)
        self.qr_label.pack(pady=15, padx=15)
    
    def view_qr(self):
        try:
            qr_image = ImageTk.PhotoImage(file=self.app_ctrl.link)
            self.qr_label.config(image=qr_image)
            self.qr_label.image = qr_image
        except Exception as e:
            # messagebox.showerror("Error", f"Failed to show QR Code: {e}\n\n{error_messages[random.randint(0, 15)]}")
            # label.config(text="ERROR, NO QR CODE FOUND.")
            pass
    
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