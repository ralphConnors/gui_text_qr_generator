from tkinter import *
from tkinter import scrolledtext

class ViewFile(Toplevel):
    def __init__(self, master, file_path, file_to_text):
        super().__init__(master)

        self.file_path = file_path
        self.file_to_text = file_to_text

        self.title(f"File content: {self.file_path}")
        self.resizable(False, False)

        Label(self, text="File Content:").pack(pady=(10, 0))

        self.text_viewed = scrolledtext.ScrolledText(self, wrap=WORD)
        self.text_viewed.pack(padx=10, pady=10, expand=True, fill=BOTH)
        
        self.text_viewed.insert(INSERT, self.file_to_text)
        self.text_viewed.config(state=DISABLED) # Make it read-only