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
        self.canvas = Canvas(master=self.root, height=self.height,
                             width=self.width)  # Creates a Canvas widget and sets it to the canvas attribute
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
    def __init__(self, x1, x2, y1, y2, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = x1  # top left corner
        self.x2 = x2  # bottom right corner
        self.y1 = y1  # top left corner
        self.y2 = y2  # bottom right corner
        self.window = window

    def draw(self):
        top_left = Point(self.x1, self.y1)
        top_right = Point(self.x2, self.y1)
        bottom_right = Point(self.x2, self.y2)
        bottom_left = Point(self.x1, self.y2)
        if self.has_top_wall:
            top_wall_line = Line(top_left, top_right)
            self.window.draw_line(line=top_wall_line, fill_colour="black")
        else:
            top_wall_line = Line(top_left, top_right)
            self.window.draw_line(line=top_wall_line, fill_colour="white")
        if self.has_bottom_wall:
            bottom_wall_line = Line(bottom_left, bottom_right)
            self.window.draw_line(line=bottom_wall_line, fill_colour="black")
        else:
            bottom_wall_line = Line(bottom_left, bottom_right)
            self.window.draw_line(line=bottom_wall_line, fill_colour="white")
        if self.has_right_wall:
            right_wall_line = Line(top_right, bottom_right)
            self.window.draw_line(line=right_wall_line, fill_colour="black")
        else:
            right_wall_line = Line(top_right, bottom_right)
            self.window.draw_line(line=right_wall_line, fill_colour="white")
        if self.has_left_wall:
            left_wall_line = Line(top_left, bottom_left)
            self.window.draw_line(line=left_wall_line, fill_colour="black")
        else:
            left_wall_line = Line(top_left, bottom_left)
            self.window.draw_line(line=left_wall_line, fill_colour="white")

    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_colour = "gray"
        else:
            fill_colour = "red"
        from_cell_point = Point(round((self.x1 + self.x2) / 2),
                                round(
                                    (self.y1 + self.y2) / 2))  # Change if pixels can't be decimal by using round or int
        to_cell_point = Point(round((to_cell.x1 + to_cell.x2) / 2),
                              round((
                                                to_cell.y1 + to_cell.y2) / 2))  # Change if pixels can't be decimal by using round or int
        print(to_cell_point.x)
        line_between = Line(from_cell_point, to_cell_point)
        self.window.draw_line(line=line_between, fill_colour=fill_colour)

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None):
        self.cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.create_cells()

    def create_cells(self):
        x1 = self.x1
        for j in range(self.num_cols):
            y1 = self.y1
            cell_column = []
            for i in range(self.num_rows):
                cell_column.append(Cell(x1, y1, x1 + self.cell_size_x, y1 + self.cell_size_y))
                y1 += self.cell_size_y
            self.cells.append(cell_column)
            x1 += self.cell_size_x
        for col in self.cells:
            for row in col:
                self.draw_cell(self.cells.index(col), col.index(row))

    def draw_cell(self, i, j):
        cell_x_pos = self.x1 + (i * self.cell_size_x)
        cell_y_pos = self.y1 + (j * self.cell_size_y)
        if self.window:
            cell = Cell(cell_x_pos, cell_x_pos + self.cell_size_x, cell_y_pos, cell_y_pos + self.cell_size_y, self.window)
            cell.has_top_wall = self.cells[i][j].has_top_wall
            cell.has_bottom_wall = self.cells[i][j].has_bottom_wall
            cell.has_left_wall = self.cells[i][j].has_left_wall
            cell.has_right_wall = self.cells[i][j].has_right_wall
            cell.draw()
            self.animate()

    def animate(self):
        self.window.redraw()
        time.sleep(0.05)

    def break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self.draw_cell(0,0)
        self.cells[-1][-1].has_bottom_wall = False
        self.draw_cell(self.num_cols - 1, self.num_rows - 1)




def main():
    win = Window(800, 600)
    maze = Maze(10,10,5,4,50,50,win)
    maze.break_entrance_and_exit()
    win.wait_for_close()


if __name__ == '__main__':
    main()
