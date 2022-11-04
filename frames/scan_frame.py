from tkinter import ttk
from .scan_container import Scan


class ScanFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.scan_window = None
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        input_frame = ttk.Frame(self, padding=10)
        input_frame.grid(row=1, column=0, sticky="EW")

    def scan(self, values, home_frame):
        self.scan_window = Scan(self, values, home_frame)
        self.scan_window.grid(row=0, column=0, sticky="NSEW", pady=5)
