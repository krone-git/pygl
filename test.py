import tkinter as tk
import time

from lib.tk.rectangle import TkCanvasRoundedRectangle, TkCanvasPill


if __name__ == "__main__":
    root = tk.Tk()

    c = tk.Canvas(root, bg="light gray")
    c.pack(fill=tk.BOTH, expand=True)

    s = TkCanvasPill(c, 20, 20, 200,50, radius=25, landscape=True, fill="red")
    s.draw()

    def func():
        for i in range(30):
            s.scale(1.01, 1.01)
            time.sleep(.005)
            c.update()
        print(
            s.bbox(),
            s._body.bbox(),
            s._right.bbox(),
            sep="\n"
            )

    c.after(2000, func)

    c.create_rectangle(*s.bbox(), outline="green")
    c.after(2500, lambda: c.create_rectangle(*s.bbox(), outline="blue"))

    root.mainloop()
