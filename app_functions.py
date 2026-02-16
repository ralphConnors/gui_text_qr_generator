import qrcode, os, random, webbrowser, json
from tkinter import *
from tkinter import messagebox, filedialog
from datetime import datetime

class AppFunctions():
    def __init__(self):
        self.color = ["White", "Green", "Yellow", "#5691DA", "#DCCD90"] # Used for color selection.
        self.colVar = 0

        self.date = ""
        self.fileName = ""
        self.link = ""

        self.error_messages = "error_messages.json"
        self.qrCode_folder = 'qrcodes'
        self.choice_Feature = ''

        self.data = ""

    def check_qr_folder(self):
        try:
            os.mkdir(self.qrCode_folder)
        except FileExistsError:
            pass
        except Exception as e:
            print(f"Debug Error: {e}")
    
    def open_qr_folder(self):
        try:
            webbrowser.open(self.qrCode_folder)
        except Exception as e:
            self.check_qr_folder()
            webbrowser.open(self.qrCode_folder)
    
    def json_variable(self):
        try:
            with open(self.error_messages, 'r') as f:
                self.error_messages = json.load(f)
            print("CONSOLE: error_messages.json found.")
        except Exception as e:
            print("CONSOLE: Error, cannot grab file.")
    
    def v_encrypt(self, data):
        result = []
        key = self.error_messages[12].upper()
        ki = 0
        for ch in data:
            if ch.isalpha():
                offset = 65 if ch.isupper() else 97
                shift = ord(key[ki % len(key)]) - 65
                result.append(chr((ord(ch) - offset + shift) % 26 + offset))
                ki += 1
            else:
                result.append(ch)
        return ''.join(result)

    def browse_file(self, entry):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")]) # What if user wants to add in text file instead?

        if file_path:
            with open(file_path, 'r') as file:
                file_to_Text = file.read() # It turns the text file into string
            entry.delete(0, END) # Deletes what's inside of entry first.
            entry.insert(0, file_to_Text)

    def clear_entry(self, entry):
        entry.delete(0, END)
    
    def feature_select(self):
        match self.choice_Feature.get():
            case "1": # Binary mode
                self.colVar = 1
                self.data = ' '.join(format(ord(char), 'b') for char in self.data)
            case "2": # Consochain mode
                self.colVar = 2
                vowels = 'aeiouAEIOU'
                self.data = ''.join(char for char in self.data if char not in vowels)
                self.data = self.data.replace(' ', '')
            case "3": # Reverse mode
                self.colVar = 3
                self.data = self.data[::-1]
            case "4": # Effigy Mode
                self.colVar = 4
                self.data = self.v_encrypt(self.data)
            case _:
                self.colVar = 0
    
    def generate_qr(self):
        self.date = datetime.now().strftime("%y%m%d-%H%M%S") # Gets current date and time, for unique filename.
        self.fileName = f"qrcode_{self.date}.png"
        self.link = f"{self.qrCode_folder}/{self.fileName}"

        self.feature_select()
        self.check_qr_folder()

        try: # The QR code is being created.
            qr = qrcode.QRCode(version=3, box_size=3, border=4)
            qr.add_data(self.data)
            qr.make(fit=True)

            image = qr.make_image(fill="Black", back_color=self.color[self.colVar])
            image.save(self.link) # Saves with unique filename.
        except Exception as e: # Uh oh, QR Code isn't made properly, we want user to see.
            messagebox.showerror("Error", f"Failed to create QR Code: {e}\n\n{self.error_messages[random.randint(0, 15)]}") # Shows error.
        return self.date, self.fileName, self.link # QR Code is finished! We transfer it back to starting variables.    
            