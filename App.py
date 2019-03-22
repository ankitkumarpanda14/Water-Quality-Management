import Tkinter as tkinter
import cv2
import PIL.Image, PIL.ImageTk
from mainuploadcode import liverec
from instant_watsapp import messenger
import tkFont

class App:
    def __init__(self, window, window_title, image_path="/home/pi/WQM.png"):
        self.window = window
        self.window.title(window_title)
 
        # Load an image using OpenCV
        self.cv_img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

        # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
        self.height, self.width, no_channels = self.cv_img.shape
 
        # Create a canvas that can fit the above image
        self.canvas = tkinter.Canvas(window, width = self.width, height = self.height)
        self.canvas.pack()
 
        # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
 
        # Add a PhotoImage to the Canvas
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
        
        # Button that lets the user ALERT manager
        custfont = tkFont.Font(weight = tkFont.BOLD)
        self.btn_mem = tkinter.Button(window, text="ALERT!!", width=50, bg ='red', command=self.alert, font = custfont)
        self.btn_mem.pack(anchor=tkinter.CENTER, expand=True)

        # Button that lets the user for live record
        self.btn_item=tkinter.Button(window, text="START REAL TIME RECORDING", width=50, command=self.live_record)
        self.btn_item.pack(anchor=tkinter.CENTER, expand=True)

        # Button that lets the user Quit
        self.btn_quit=tkinter.Button(window, text="EXIT", width=50, command=exit)
        self.btn_quit.pack(anchor=tkinter.CENTER, expand=True)
        
        self.window.mainloop()
        
        
    def alert(self):
        msg = "ALERT!!"
        mg = messenger(msg)
        mg.message_maker()

    def live_record(self):
        liverec()

# Create a window and pass it to the Application object
App(tkinter.Tk(), "Water Quality Manager")
