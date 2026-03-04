import os
import tkinter as tk

from datetime import datetime
from tkinter import filedialog


def clean_name(text):
    text = text.strip().lower()
    if len(text) < 3:
        return None
    return text

root = tk.Tk()
root.withdraw()

filename = filedialog.askopenfilename(title= "Vyber subor s menami.", filetypes=[("Textove subory", "*.txt"),("Vsetky subory", "*.*")])

if not filename:
    print("nevybral si ziadny subor.")
    exit()

# 1. nacitanie dat
data = []
with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        #data.append(line.strip()) #kontrola kazdeho riadku aj ked prazdneho
        text = line.strip()
        if text:                   #kontrola riadkov len kde je text
            data.append(text)

# 2. report + pocitadla 
report = []
valid_names = []
valid_count = 0
invalid_count = 0

for t in data:
    result = clean_name(t)

    if result is None:
        report.append(f"INPUT: {t!r} -> INVALID")
        invalid_count += 1
    else:
        report.append(f"INPUT: {t!r} -> VALID ({result})")
        valid_count += 1
        valid_names.append(result)

summary = f"SUMMARY: {valid_count} = valid, {invalid_count} = invalid"

# # xx. vypis do konzoly
# for line in report:
#     print(line)
# print(summary)

# 3. cas soustenia
run_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

os.makedirs("reports", exist_ok=True)
run_time_for_filename = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
report_filename = f"reports/report_{run_time_for_filename}.txt"

# 4. zapis do suboru report.txt
with open(report_filename, "w", encoding="utf-8") as file:
    file.write(f"RUN AT: {run_time}\n")
    file.write("-" *30 + "\n")
    for line in report:
        file.write(line + "\n")
    file.write("-" *30 + "\n")
    file.write(summary + "\n")

# 5. zapis do suboru len validnych mien
with open("valid_names.txt", "w", encoding="utf-8") as file:
    for name in valid_names:
        file.write(name + "\n")