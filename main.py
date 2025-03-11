import tkinter as tk
from tkinter import *
import sys
import os
import time

import TotalAlkilinity as TA
import CalciumHardness as CH
import Temperature as Temp
import Chlorine as Cl
import TDS
import pH
import ORP
import Chemicals

def main():
    # Creating instances of classes with default values
    ta = TA.TotalAlkilinity()  # default value 80
    ch = CH.CalciumHardness()  # default value 200
    temp = Temp.Temperature()  # default value 82
    cl = Cl.Chlorine()         # default value 1.0
    tds = TDS.TDS()            # default value 1500
    ph = pH.pH()               # default value 7.2
    orp = ORP.ORP()            # default value 650
    chems = Chemicals.Chemicals(5, 5, 5)

    # chems.updateValues(cl.get_chlorine(), ta.get_totalAlkilinity(), ph.get_ph(), ch.get_calciumHardness(), orp.get_orp())

    # Create tkinter
    root = tk.Tk()
    root.title("Pool Monitor")
    root.geometry("500x750")
    root.configure(bg="gray")

    #Create a label
    labelCL = Label(root, text="Chlorine Level", bg="blue", fg="white")
    entryCl = Entry(root)
    labelCL.pack()
    entryCl.pack()

    labelpH = Label(root, text="pH Level", bg="blue", fg="white")
    entrypH = Entry(root)
    labelpH.pack()
    entrypH.pack()
    
    labelORP = Label(root, text="ORP Level", bg="blue", fg="white")
    entryORP = Entry(root)
    labelORP.pack()
    entryORP.pack()

    labelTA = Label(root, text="Total Alkalinity Level", bg="blue", fg="white")
    entryTA = Entry(root)
    labelTA.pack()
    entryTA.pack()

    labelCH = Label(root, text="Calcium Hardness Level", bg="blue", fg="white")
    entryCH = Entry(root)
    labelCH.pack()
    entryCH.pack()

    labelTDS = Label(root, text="TDS Level", bg="blue", fg="white")
    entryTDS = Entry(root)
    labelTDS.pack()
    entryTDS.pack()

    labelTemp = Label(root, text="Temperature Level", bg="blue", fg="white")
    entryTemp = Entry(root)
    labelTemp.pack()
    entryTemp.pack()

    def clear():
        entryCl.delete(0, END)
        entrypH.delete(0, END)
        entryORP.delete(0, END)
        entryTA.delete(0, END)
        entryCH.delete(0, END)
        entryTDS.delete(0, END)
        entryTemp.delete(0, END)
        

    def submit():
        fields = [
            (entryTA, ta.set_totalAlkilinity, int, "Total Alkalinity"),
            (entryCH, ch.set_calciumHardness, int, "Calcium Hardness"),
            (entryTemp, temp.set_temperature, int, "Temperature"),
            (entryCl, cl.set_chlorine, float, "Chlorine"),
            (entryTDS, tds.set_tds, int, "TDS"),
            (entrypH, ph.set_ph, float, "pH"),
            (entryORP, orp.set_orp, int, "ORP"),
        ]

        updated_fields = []
        failed_fields = []

        for entry, setter, datatype, field_name in fields:
            value = entry.get().strip()
            if value:  # only update if the entry isn't empty
                try:
                    setter(datatype(value))
                    updated_fields.append(field_name)
                except ValueError:
                    failed_fields.append(field_name)

        if failed_fields:
            print("Invalid input in the following fields:", ", ".join(failed_fields))
        else:
            print("Pool levels updated successfully for:", ", ".join(updated_fields))

        # Display current values after updates
        print("CURRENT POOL LEVELS:")
        print(f"Temperature: {temp.get_temperature()} °F")
        print(f"Total Alkalinity: {ta.get_totalAlkilinity()} ppm")
        print(f"Calcium Hardness: {ch.get_calciumHardness()} ppm")
        print(f"Chlorine: {cl.get_chlorine()} ppm")
        print(f"TDS: {tds.get_tds()} ppm")
        print(f"pH: {ph.get_ph()}")
        print(f"ORP: {orp.get_orp()} mV")
        print("")

    clearBTN = Button(root, text="Clear", command=clear)
    clearBTN.pack()
    submitBTN = Button(root, text="Submit", command=submit)
    submitBTN.pack()

    root.mainloop()

if __name__ == "__main__":
    main()