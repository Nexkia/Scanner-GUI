import tkinter as tk
from tkinter import ttk
from .home_frame import HomeFrame
from .scan_frame import ScanFrame


COLOUR_PRIMARY = "#2e3f4f"
COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_BACKGROUND = "#fff"
COLOUR_LIGHT_TEXT = "#eee"
COLOUR_DARK_TEXT = "#8095a8"
COLOR_ALERT = "#ff0000"


class Root(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("IHOSP")
        self.geometry("480x260")
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.frames = {}
        scan_frame = ScanFrame(self)
        home_frame = HomeFrame(self, lambda: self.show_frame(ScanFrame), scan_frame)
        home_frame.grid(row=0, column=0, sticky="NESW")
        scan_frame.grid(row=0, column=0, sticky="NESW")
        self.frames[HomeFrame] = home_frame
        self.frames[ScanFrame] = scan_frame
        self.show_frame(HomeFrame)

        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure(
            "WelcomeText.TLabel",
            foreground=COLOUR_PRIMARY,
            font=("TkDefaultFont", 24)

        )
        style.configure(
            "ConfigText.TLabel",
            foreground=COLOUR_PRIMARY,
            font=("TkDefaultFont", 12)

        )
        style.configure("Timer.TFrame", background=COLOUR_LIGHT_BACKGROUND)
        style.configure("Background.TFrame", background=COLOUR_PRIMARY)
        style.configure(
            "TimerText.TLabel",
            foreground=COLOUR_DARK_TEXT,
            font="Courier 20"
        )
        style.configure(
            "Alert.TLabel",
            foreground=COLOR_ALERT,
            font=("TkDefaultFont", 11)
        )
        style.configure(
            "LightText.TLabel",
            foreground=COLOUR_PRIMARY,
            font=("TkDefaultFont", 11)
        )
        style.configure(
            "Title.TLabel",
            foreground=COLOUR_PRIMARY,
            font=("TkDefaultFont", 13)
        )
        style.configure(
            "ClickButton.TButton",
            background=[COLOUR_SECONDARY],
            foreground=COLOUR_LIGHT_TEXT,
            font=("TkDefaultFont", 11)
        )

        style.map(
            "ClickButton.TButton",
            background=[("active", COLOUR_PRIMARY), ("disabled", COLOUR_LIGHT_TEXT)]
        )

        # Main app window is a tk widget, so background is set directly
        self["background"] = COLOUR_PRIMARY

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
