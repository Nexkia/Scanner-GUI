import json
from tkinter import ttk
import tkinter as tk


class NewDevice(tk.Toplevel):
    def __init__(self, parent, mac):
        super().__init__(parent)
        devices = loadPersistent("devices.json")
        devices_path = get_path("devices.json")
        name_variable = tk.StringVar()
        name = ttk.Entry(self, textvariable=name_variable)
        name.pack(pady=15)

        selected_protocol = tk.StringVar(value="duoek-er2")
        protocol = ttk.Combobox(self, textvariable=selected_protocol)
        protocol["values"] = ("berry1-3", "berry1-4", "viatompc60w", "aoj-20q", "duoek-er2", "bp2")
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
            else:
                devices[name_variable.get()] = {"mac": mac, "protocol": selected_protocol.get()}
                with open(devices_path, "w") as outfile:
                    outfile.write(json.dumps(devices))
                self.destroy()

        save_button = ttk.Button(self, text="save", command=save)
        save_button.pack()
        handle_label.pack()


def get_path(nameFile):
    return "/home/.ihosp/" + nameFile


def loadPersistent(nameFile):
    path_file = "/home/.ihosp/" + nameFile
    with open(path_file) as json_file:
        return openJson(json_file)


def openJson(json_file):
    try:
        out = json.load(json_file)
    except json.decoder.JSONDecodeError:
        out = {}
    return out
