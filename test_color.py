import tkinter as tk
import json as js
from itertools import cycle

from lib.rgba import RGBAFactory, RGBAMath, RGBAUtility
from lib.tk import TkinterColor
from lib.vector import VectorMath


root = tk.Tk()
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill=tk.BOTH)

def update_loop(delay, root, function):
    def _loop(delay):
        function()
        root.after(delay, lambda: _loop(delay))
    return _loop(delay)


rgba = RGBAFactory.from_hexcode(TkinterColor.hexcode("red"))

target = RGBAFactory.from_hexcode(TkinterColor.hexcode("green"))
channel_max = 255

forward = range(channel_max)
reverse = range(channel_max - 1, 0, -1)
multiplier = cycle((*forward, *reverse))

def update_canvas():
    level = next(multiplier) / channel_max
    # rgb = RGBAMath.overlay(rgba, target, level)
    rgb = RGBAMath.level(rgba, level)
    canvas.config(bg=RGBAUtility.to_hexcode(rgb))

update_loop(2, root, update_canvas)

root.mainloop()
