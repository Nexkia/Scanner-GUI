import tkinter as tk
from tkinter import ttk
from .new_deviceTp import NewDevice
import re


class Scan(tk.Canvas):
    def __init__(self, container, values, home_frame, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.messages_frame = ttk.Frame(container)
        self.messages_frame.columnconfigure(0, weight=1)

        self.values = values
        self.scrollable_window = self.create_window((0, 0), window=self.messages_frame, anchor="nw")

        def configure_scroll_region(event):
            self.configure(scrollregion=self.bbox("all"))

        def configure_window_size(event):
            self.itemconfig(self.scrollable_window, width=self.winfo_width())

        self.bind("<Configure>", configure_window_size)
        self.messages_frame.bind("<Configure>", configure_scroll_region)
        self.bind_all("<MouseWheel>", self._on_mousewheel)

        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.yview)
        scrollbar.grid(row=0, column=1, sticky="NS")

        self.yview_moveto(1.0)
        # https://stackoverflow.com/a/17457843/1587271
        result = tk.StringVar(value=self.values)
        self.listbox = tk.Listbox(self, listvariable=result, width=55, height=11)
        self.listbox.config(yscrollcommand=scrollbar.set)
        self.listbox.columnconfigure(1, weight=1)
        self.listbox.grid(sticky="NEWS", padx=(10, 50), pady=10)
        scrollbar.config(command=self.listbox.yview)
        self.listbox.focus()

        def getSelected():
            selected = self.listbox.get(self.listbox.curselection())
            res = re.match(r"name=(.{1,})\smac=(.{1,})", selected)
            NewDevice(self, res.group(2))

        def new_scan():
            home_frame.tkraise()
            home_frame.textLabel.set("Scanning page")
            self.destroy()

        self.new_button = ttk.Button(
            self,
            text="new scan",
            command=new_scan
        )
        self.new_button.grid(row=1, column=0, sticky="w")
        self.submit_button = ttk.Button(
            self,
            text="submit",
            command=getSelected
        )
        self.submit_button.grid(row=1, column=0)

    def _on_mousewheel(self, event):
        self.yview_scroll(-int(event.delta / 120), "units")
