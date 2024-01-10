# import Tkinter as tk
# win=tk.Tk()
# win.mainloop()


try:
    import Tkinter as tk  # Python 2
except ImportError:
    import tkinter as tk  # Python 3

win = tk.Tk()
win.mainloop()


# from PIL import Image
# imgvar=Image.open("Downloads/images (6).jpeg")
# imgvar.show()


# from PIL import Image

# try:
#     imgvar = Image.open("Downloads/images (6).jpeg")
#     imgvar.show()
# except FileNotFoundError:
#     print("Error: File not found. Please check the file path.")
# except Exception as e:
#     print(f"An error occurred: {e}")
