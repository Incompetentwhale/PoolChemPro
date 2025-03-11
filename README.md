# PoolChem Pro

PoolChem Pro is a Python-based pool chemistry calculator designed to help pool owners and maintenance professionals accurately determine the amount of chemicals required to adjust pool water parameters. With a user-friendly graphical interface built using Tkinter, PoolChem Pro dynamically calculates pool volume from user-provided dimensions and provides detailed chemical adjustment recommendations based on target ranges.

## Features

- **Dynamic Pool Volume Calculation:**  
  Enter pool dimensions (Length, Width, and Average Depth) to calculate the pool's volume in gallons.

- **Comprehensive Chemical Adjustments:**  
  The application calculates adjustments for key pool chemistry parameters:
  - Chlorine (both increase and reduction using Calcium Hypochlorite and Sodium Thiosulfate)
  - pH (adjustment using Soda Ash or Muriatic Acid)
  - Total Alkalinity (using Sodium Bicarbonate)
  - Calcium Hardness (using Calcium Chloride)
  - CYA (using Cyanuric Acid)

- **Target Range Support:**  
  Set acceptable target ranges for each parameter, allowing the application to determine if the current reading is too low, too high, or within the ideal range.

- **Dynamic GUI Output:**  
  The program dynamically displays adjustment recommendations in the GUI, updating in real-time as new values are entered.

## Prerequisites

- **Python 3.x**  
  Ensure that you have Python 3 installed on your system.

- **Tkinter:**  
  Tkinter is included in most Python distributions. If it's not installed, you can install it via your package manager or by using:
  ```bash
  pip install tk
# Install
```
git clone https://github.com/yourusername/PoolChemPro.git
cd PoolChemPro
```
# Usage 
```
python main.py
```
The GUI allows you to input:
- Pool Dimensions: Length, Width, and Averge depth (Deepest + Shallowest point /2)
- Pool Chemistry Readings: Chlorine, pH, Total Alkilinity, Calcium Hardness, and Cyanuric Acid
### Submit to Calculate Adjustments:
Click the Submit button to see the dynamic pool volume calculation and chemical adjustment recommendations.
The adjustments are shown in a dedicated output frame within the GUI. If any input is invalid, an error message is displayed.
### Clear
Clears all values easily.

## Target Ranges
**The target ranges are set to standard pool chemistry values, feel free to change at your own risk**