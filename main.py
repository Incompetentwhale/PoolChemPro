import tkinter as tk
from Chemicals import Chemicals

# Initialize Pool Dimensions (75ft x 50ft x 7.5ft)
pool = Chemicals(75, 50, 7.5)  

# GUI setup
root = tk.Tk()
root.title("PoolChem Pro")
root.geometry("400x700")

# Labels and entries clearly laid out
fields = [
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

# Target values for ideal chemistry
TARGET_RANGES = {
    "Chlorine": (1.0, 5.0),
    "pH": (7.2, 7.8),
    "Total Alkalinity": (80, 120),
    "Calcium Hardness": (200, 400),
    "CYA": (10, 30),
}


def submit():
    try:
        # Read current pool measurements
        current_values = {
            "Chlorine": float(entries["Chlorine"].get()),
            "pH": float(entries["pH"].get()),
            "Total Alkalinity": float(entries["Total Alkalinity"].get()),
            "Calcium Hardness": float(entries["Calcium Hardness"].get()),
            "CYA": float(entries["CYA"].get()),
        }
        
        adjustments = {}

        # Chlorine adjustment (this method supports both increase and reduction)
        chlorine_min, chlorine_max = TARGET_RANGES["Chlorine"]
        if current_values["Chlorine"] < chlorine_min:
            # Increase chlorine
            adjustments["Chlorine"] = pool.adjust_chlorine(current_values["Chlorine"], chlorine_min)
        elif current_values["Chlorine"] > chlorine_max:
            # Reduce chlorine (using same method since it returns a reduction chemical)
            adjustments["Chlorine"] = pool.adjust_chlorine(current_values["Chlorine"], chlorine_max)
        else:
            adjustments["Chlorine"] = (None, 0)

        # pH adjustment (also supports both directions)
        pH_min, pH_max = TARGET_RANGES["pH"]
        if current_values["pH"] < pH_min:
            adjustments["pH"] = pool.adjust_pH(current_values["pH"], pH_min)
        elif current_values["pH"] > pH_max:
            adjustments["pH"] = pool.adjust_pH(current_values["pH"], pH_max)
        else:
            adjustments["pH"] = (None, 0)

        # Total Alkalinity adjustment (only supports increases)
        alk_min, alk_max = TARGET_RANGES["Total Alkalinity"]
        if current_values["Total Alkalinity"] < alk_min:
            adjustments["Total Alkalinity"] = pool.adjust_alkalinity(current_values["Total Alkalinity"], alk_min)
        elif current_values["Total Alkalinity"] > alk_max:
            adjustments["Total Alkalinity"] = ("No chemical reduction available; consider partial water replacement.", 0)
        else:
            adjustments["Total Alkalinity"] = (None, 0)

        # Calcium Hardness adjustment (only supports increases)
        ch_min, ch_max = TARGET_RANGES["Calcium Hardness"]
        if current_values["Calcium Hardness"] < ch_min:
            adjustments["Calcium Hardness"] = pool.adjust_calcium_hardness(current_values["Calcium Hardness"], ch_min)
        elif current_values["Calcium Hardness"] > ch_max:
            adjustments["Calcium Hardness"] = ("No chemical reduction available; consider partial water replacement.", 0)
        else:
            adjustments["Calcium Hardness"] = (None, 0)

        # CYA adjustment (only supports increases)
        cya_min, cya_max = TARGET_RANGES["CYA"]
        if current_values["CYA"] < cya_min:
            adjustments["CYA"] = pool.adjust_cya(current_values["CYA"], cya_min)
        elif current_values["CYA"] > cya_max:
            adjustments["CYA"] = ("No chemical reduction available; consider partial water replacement.", 0)
        else:
            adjustments["CYA"] = (None, 0)

        print("\n📌 CHEMICALS REQUIRED:")
        for chem, (action, amount) in adjustments.items():
            if action is None:
                print(f"{chem}: No adjustment needed.")
            else:
                if amount != 0:
                    print(f"{chem}: Add {amount} oz of {action}.")
                else:
                    print(f"{chem}: {action}")

    except ValueError:
        print("❌ Invalid input! Please enter numeric values.")

def clear():
    for entry in entries.values():
        entry.delete(0, tk.END)

# Buttons
submitBTN = tk.Button(root, text="Submit", command=submit)
submitBTN.pack(pady=5)

clearBTN = tk.Button(root, text="Clear", command=clear)
clearBTN.pack(pady=5)

root.mainloop()
