import time
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
        self.root.title("My Maze Solver Application")  # Sets the root attributes title
        self.canvas = Canvas(master=self.root, height=self.height, width=self.width)  # Creates a Canvas widget and sets it to the canvas attribute
        self.canvas.pack()  # Packs the canvas widget so it's ready to drawn
        self.running = False  # Represents whether the window is "running"
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_colour):
        line.draw(canvas=self.canvas, fill_colour=fill_colour)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_one, point_two):
        self.point_one = point_one
        self.point_two = point_two

    def draw(self, canvas, fill_colour):
        canvas.create_line(self.point_one.x, self.point_one.y, self.point_two.x, self.point_two.y, fill=fill_colour,
                           width=2)

class Cell:
    def __init__(self, x1, x2, y1, y2, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = x1 # top left corner
        self.x2 = x2 # bottom right corner
        self.y1 = y1 # top left corner
        self.y2 = y2 # bottom right corner
        self.window = window

    def draw(self):
        top_left = Point(self.x1,self.y1)
        top_right = Point(self.x2, self.y1)
        bottom_right = Point(self.x2, self.y2)
        bottom_left = Point(self.x1, self.y2)
        if self.has_top_wall:
            top_wall_line = Line(top_left, top_right)
            self.window.draw_line(line=top_wall_line, fill_colour="black")
        if self.has_bottom_wall:
            bottom_wall_line = Line(bottom_left, bottom_right)
            self.window.draw_line(line=bottom_wall_line, fill_colour="black")
        if self.has_right_wall:
            right_wall_line = Line(top_right, bottom_right)
            self.window.draw_line(line=right_wall_line, fill_colour="black")
        if self.has_left_wall:
            left_wall_line = Line(top_left, bottom_left)
            self.window.draw_line(line=left_wall_line, fill_colour="black")

def main():
    win = Window(800, 600)
    first_point = Point(0,0)
    second_point = Point(200,400)
    line = Line(first_point, second_point)
    win.draw_line(line=line, fill_colour="red")
    win.wait_for_close()

if __name__ == '__main__':
    main()
