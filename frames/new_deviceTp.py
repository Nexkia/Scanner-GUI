import json
import time
from tkinter import ttk
import tkinter as tk
from utils import loadPersistent, get_path


class NewDevice(tk.Toplevel):
    def __init__(self, parent, mac, show_load, reload_function):
        super().__init__(parent)
        devices = loadPersistent("devices.json")
        devices_path = get_path("devices.json")
        name_variable = tk.StringVar()
        name = ttk.Entry(self, textvariable=name_variable)
        name.pack(pady=15)

        selected_protocol = tk.StringVar(value="duoek-er2")
        protocol = ttk.Combobox(self, textvariable=selected_protocol)
        protocol["values"] = ("berry1-3", "berry1-4", "viatompc60w", "aoj-20q", "duoek-er2", "bp2", "adf_b27")
        protocol["state"] = "readonly"  # "normal is the counterpart"
        protocol.pack()

        handle_text = tk.StringVar()

        handle_label = ttk.Label(
            self,
            textvariable=handle_text,
            style="Alert.TLabel"
        )

        def save():
            if name_variable.get() in devices.keys():
                handle_text.set("Errore nome già utilizzato")
                self.update()
                time.sleep(2)
            if len(devices) == 5:
                handle_text.set("Non puoi aggiungere altri device")
                self.update()
                time.sleep(2)
                reload_function()
                show_load()
                self.destroy()
            else:
                devices[name_variable.get()] = {"mac": mac, "protocol": selected_protocol.get()}
                with open(devices_path, "w") as outfile:
                    outfile.write(json.dumps(devices))
                self.destroy()

        save_button = ttk.Button(self, text="save", command=save)
        save_button.pack()
        handle_label.pack()
