from itertools import cycle 
from PIL import Image, ImageTk
import tkinter as tk


root= tk.Tk()
root.title("image slideshow viewer")
# list of image path
image_paths= [
    r"C:\Users\HP\Pictures\Screenshots\Screenshot 2025-10-07 154659.png",
    r"C:\Users\HP\Pictures\Screenshots\Screenshot 2025-10-24 204838.png",
    r"C:\Users\HP\Pictures\209c67f1ba2d150991dbd846775e08ea.jpg",
    r"C:\Users\HP\Pictures\captain-america-marvel-disney-movie-metal-07-11-2024-1731050780-hd-wallpaper.webp",
    r"C:\Users\HP\Pictures\IMG-20251003-WA0021[1].jpg",
    r"C:\Users\HP\Pictures\captain-america-marvel-disney-movie-metal-07-11-2024-1731050780-hd-wallpaper.webp",
    r"C:\Users\HP\Pictures\Screenshots\Screenshot 2025-10-29 005122.png",
    r"C:\Users\HP\Pictures\Screenshots\Screenshot 2025-11-02 115334.png",
]


# now we will resize our image to 1080*1080
image_size= (1080,1080)
images= [Image.open(path).resize(image_size) for path in image_paths]
photo_images= [ImageTk.PhotoImage(image) for image in images]


label= tk.Label(root)
label.pack()
slideshow= cycle(photo_images)


def update_image():
    photo_image= next(slideshow)
    label.config(image = photo_image)
    root.after(3000, update_image)


def start_slideshow():
    update_image()
    

play_button= tk.Button(root, text= "play slideshow",command= start_slideshow)
play_button.pack()
root.mainloop()