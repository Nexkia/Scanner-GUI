import json
import tkinter as tk
from tkinter import ttk
import re
from utils import loadPersistent, get_path


class LoadFrame(ttk.Frame):
    def __init__(self, container, show_frame, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.columnconfigure(0, weight=1)

        # https://stackoverflow.com/a/17457843/1587271
        self.devices = loadPersistent("devices.json")
        devices_path = get_path("devices.json")
        result = [str(key) + " " + str(value) for key, value in self.devices.items()]
        result = tuple(result)
        self.result = tk.StringVar(value=result)
        self.listbox = tk.Listbox(self, listvariable=self.result, width=55, height=11)
        self.listbox.columnconfigure(1, weight=1)
        self.listbox.grid(sticky="NEWS", padx=(10, 50), pady=10)
        self.listbox.focus()

        def getSelected():
            selected = self.listbox.get(self.listbox.curselection())
            res = re.match(r"(.{1,})\s({)", selected)
            self.devices.pop(res.group(1))
            with open(devices_path, "w") as outfile:
                outfile.write(json.dumps(self.devices))
            self.reload_devices()

        self.back_button = ttk.Button(
            self,
            text="back",
            command=show_frame
        )
        self.back_button.grid(row=1, column=0, sticky="w")

        self.remove_button = ttk.Button(
            self,
            text="remove",
            command=getSelected
        )
        self.remove_button.grid(row=1, column=0, sticky="e")

    def reload_devices(self):
        self.devices = loadPersistent("devices.json")
        result = [str(key) + " " + str(value) for key, value in self.devices.items()]
        result = tuple(result)
        self.result.set(result)
        self.update()
