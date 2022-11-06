from utils import  get_path
import sys
import tkinter as tk
from tkinter import ttk
from ble import scanning


class HomeFrame(ttk.Frame):
    def __init__(self, container, show_frame, show_load, scan_frame, *args, **kwargs):
        super().__init__(container)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.textLabel = tk.StringVar(value="Scanning page")
        self.label = ttk.Label(self, textvariable=self.textLabel)
        self.label.pack(pady=20)

        def scan_device():
            self.textLabel.set("Wait 30 seconds to scan")
            self.update()
            result = scanning()
            scan_frame.scan(result, self)
            show_frame()

        self.button_start = ttk.Button(
            self,
            text="add device",
            command=scan_device
        )
        self.button_start.pack()

        self.load_devices = ttk.Button(
            self,
            text="load configuration",
            command=show_load
        )
        self.load_devices.pack(pady=70)

