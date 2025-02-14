import tkinter as tk

# Constants for grid size
ROWS = 10
COLS = 10
CELL_SIZE = 50
ERASER_SIZE = 60  # Slightly larger for a smoother erase effect

class CanvasEraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Eraser")

        # Create canvas
        self.canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE, bg="white")
        self.canvas.pack()

        # Create grid of blue rectangles
        self.cells = {}
        for row in range(ROWS):
            for col in range(COLS):
                x1, y1 = col * CELL_SIZE, row * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
                self.cells[rect] = (x1, y1, x2, y2)

        # Create the eraser (a draggable rectangle)
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="gray")

        # Bind mouse events for dragging
        self.canvas.bind("<B1-Motion>", self.move_eraser)

    def move_eraser(self, event):
        """Moves the eraser and erases blue cells it touches."""
        x1, y1 = event.x - ERASER_SIZE // 2, event.y - ERASER_SIZE // 2
        x2, y2 = x1 + ERASER_SIZE, y1 + ERASER_SIZE

        # Move the eraser
        self.canvas.coords(self.eraser, x1, y1, x2, y2)

        # Erase cells that intersect with the eraser
        for rect, (rx1, ry1, rx2, ry2) in self.cells.items():
            if not self.canvas.itemcget(rect, "fill") == "white":  # Only erase blue cells
                if self.intersects(x1, y1, x2, y2, rx1, ry1, rx2, ry2):
                    self.canvas.itemconfig(rect, fill="white")

    @staticmethod
    def intersects(x1, y1, x2, y2, rx1, ry1, rx2, ry2):
        """Checks if two rectangles intersect."""
        return not (x2 < rx1 or x1 > rx2 or y2 < ry1 or y1 > ry2)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CanvasEraserApp(root)
    root.mainloop()
