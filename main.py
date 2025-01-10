from tkinter import *
from navbar import NavBar

def Main():
    Window = Tk()
    Window.state('zoomed')
    Window.resizable(False,False)
    NavBar(Window)
    Window.mainloop()
if __name__ == '__main__':
    Main()