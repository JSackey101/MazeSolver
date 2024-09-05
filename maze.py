from tkinter import Tk, BOTH, Canvas


# Will better comment at the end

class Window:
    """
    A class to represent a graphical window
    """

    def __init__(self, width, height):
        """
        Constructor method that defines all the necessary attributes for window objects created from this class

        Parameters
        ----------
        width
        height
        """
        self.width = width
        self.height = height
        self.root = Tk()  # Creates initial root widget using Tk() and sets it to root attribute
        self.root.protocol("WM_DELETE_WINDOW", self.close())
        self.root.title("My Maze Solver Application")  # Sets the root attributes title
        self.canvas = Canvas(master=self.root)  # Creates a Canvas widget and sets it to the canvas attribute
        self.canvas.pack()  # Packs the canvas widget so it's ready to drawn
        self.running = False  # Represents whether the window is "running"

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        if self.running:
            self.redraw()

    def close(self):
        self.running = False






def main():
    win = Window(800, 600)
    win.wait_for_close()

if __name__ == '__main__':
    main()