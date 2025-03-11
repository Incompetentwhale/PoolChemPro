import tkinter as tk
from Chemicals import Chemicals

# GUI setup
root = tk.Tk()
root.title("PoolChem Pro")
root.geometry("400x700")

# Input fields
fields = [
    ("Length", 50),
    ("Width", 75),
    ("Average Depth", 7.5),
    ("Chlorine", "1"),
    ("pH", "7.4"),
    ("Total Alkalinity", "80"),
    ("Calcium Hardness", "200"),
    ("CYA", "30"),
]

entries = {}
for label_text, default in fields:
    label = tk.Label(root, text=label_text)
    label.pack()
    entry = tk.Entry(root)
    entry.insert(0, default)
    entry.pack()
    entries[label_text] = entry

AdjustmentsNeeded = tk.Label(root, text="📌ADJUSTMENTS NEEDED", fg="red")
AdjustmentsNeeded.pack()

# Create a frame to hold the dynamic adjustment labels
output_frame = tk.Frame(root)
output_frame.pack(pady=10)

# Define acceptable target ranges as (min, max) tuples
TARGET_RANGES = {
    "Chlorine": (1.0, 5.0),
    "pH": (7.2, 7.8),
    "Total Alkalinity": (80, 120),
    "Calcium Hardness": (200, 300),
    "CYA": (10, 30),
}

def submit():
    length = float(entries["Length"].get())
    width = float(entries["Width"].get())
    depth = float(entries["Average Depth"].get())
    pool = Chemicals(length, width, depth)
    # Clear previous dynamic labels
    for widget in output_frame.winfo_children():
        widget.destroy()

    adjustmentsNeedToPool = []

    try:
        # Read current pool measurements
        current_values = {
            "Chlorine": float(entries["Chlorine"].get()),
            "pH": float(entries["pH"].get()),
            "Total Alkalinity": float(entries["Total Alkalinity"].get()),
            "Calcium Hardness": float(entries["Calcium Hardness"].get()),
            "CYA": float(entries["CYA"].get()),
        }
        
        # Chlorine adjustment (supports increase and reduction)
        chlorine_min, chlorine_max = TARGET_RANGES["Chlorine"]
        if current_values["Chlorine"] < chlorine_min:
            chem, amount = pool.adjust_chlorine(current_values["Chlorine"], chlorine_min)
            adjustmentsNeedToPool.append(f"Chlorine: Add {amount} oz of {chem} to raise level to {chlorine_min} ppm.")
        elif current_values["Chlorine"] > chlorine_max:
            chem, amount = pool.adjust_chlorine(current_values["Chlorine"], chlorine_max)
            adjustmentsNeedToPool.append(f"Chlorine: Add {amount} oz of {chem} to lower level to {chlorine_max} ppm.")
        else:
            adjustmentsNeedToPool.append("Chlorine: No adjustment needed.")

        # pH adjustment (supports both directions)
        pH_min, pH_max = TARGET_RANGES["pH"]
        if current_values["pH"] < pH_min:
            chem, amount = pool.adjust_pH(current_values["pH"], pH_min)
            adjustmentsNeedToPool.append(f"pH: Add {amount} oz of {chem} to raise pH to {pH_min}.")
        elif current_values["pH"] > pH_max:
            chem, amount = pool.adjust_pH(current_values["pH"], pH_max)
            adjustmentsNeedToPool.append(f"pH: Add {amount} oz of {chem} to lower pH to {pH_max}.")
        else:
            adjustmentsNeedToPool.append("pH: No adjustment needed.")

        # Total Alkalinity adjustment (only supports increase)
        alk_min, alk_max = TARGET_RANGES["Total Alkalinity"]
        if current_values["Total Alkalinity"] < alk_min:
            chem, amount = pool.adjust_alkalinity(current_values["Total Alkalinity"], alk_min)
            adjustmentsNeedToPool.append(f"Total Alkalinity: Add {amount} oz of {chem} to raise alkalinity to {alk_min} ppm.")
        elif current_values["Total Alkalinity"] > alk_max:
            adjustmentsNeedToPool.append("Total Alkalinity: High level. Consider dilution or partial water replacement.")
        else:
            adjustmentsNeedToPool.append("Total Alkalinity: No adjustment needed.")

        # Calcium Hardness adjustment (only supports increase)
        ch_min, ch_max = TARGET_RANGES["Calcium Hardness"]
        if current_values["Calcium Hardness"] < ch_min:
            chem, amount = pool.adjust_calcium_hardness(current_values["Calcium Hardness"], ch_min)
            adjustmentsNeedToPool.append(f"Calcium Hardness: Add {amount} oz of {chem} to raise level to {ch_min} ppm.")
        elif current_values["Calcium Hardness"] > ch_max:
            adjustmentsNeedToPool.append("Calcium Hardness: High level. Consider partial water replacement.")
        else:
            adjustmentsNeedToPool.append("Calcium Hardness: No adjustment needed.")

        # CYA adjustment (only supports increase)
        cya_min, cya_max = TARGET_RANGES["CYA"]
        if current_values["CYA"] < cya_min:
            chem, amount = pool.adjust_cya(current_values["CYA"], cya_min)
            adjustmentsNeedToPool.append(f"CYA: Add {amount} oz of {chem} to raise level to {cya_min} ppm.")
        elif current_values["CYA"] > cya_max:
            adjustmentsNeedToPool.append("CYA: High level. Consider partial water replacement.")
        else:
            adjustmentsNeedToPool.append("CYA: No adjustment needed.")

        # Dynamically create and display labels for every adjustment in the list
        for message in adjustmentsNeedToPool:
            msg_label = tk.Label(output_frame, text=message)
            msg_label.pack(anchor="w")

    except ValueError:
        error_label = tk.Label(output_frame, text="❌ Invalid input! Please enter numeric values.", fg="red")
        error_label.pack()

def clear():
    for entry in entries.values():
        entry.delete(0, tk.END)
    for widget in output_frame.winfo_children():
        widget.destroy()

# Buttons for submit and clear actions
submitBTN = tk.Button(root, text="Submit", command=submit)
submitBTN.pack(pady=5)

clearBTN = tk.Button(root, text="Clear", command=clear)
clearBTN.pack(pady=5)

root.mainloop()
