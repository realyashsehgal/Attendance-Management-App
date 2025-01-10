import tkinter as tk
from datetime import datetime
from tkinter import font

# Get current day, date, and month
localdatetime = datetime.now()
DAY = localdatetime.strftime("%A")
DATE = localdatetime.strftime("%d")
MONTH = localdatetime.strftime("%B")



def NavBar(Window):
    # Create the main window (navbar)
    TopFrame = tk.Frame(Window, bg="black", height=80)
    TopFrame.pack(fill="x")  # Full width navbar

    # Left div for day, date, and month
    LeftDiv = tk.Frame(TopFrame, bg="black", width=300)
    LeftDiv.pack(side="left", fill="y", padx=2, pady=4)  # Anchored to left side, vertically fills the navbar

    # Day Partition - Horizontal (top part)
    DayFrame = tk.Frame(LeftDiv, bg="black", height=30)
    DayFrame.grid(row=1, column=0, sticky="ew")  # Fill horizontally in row 0

    # Date and Month Partition - Side by Side (bottom part)
    DateFrame = tk.Frame(LeftDiv, bg="black", height=30)
    DateFrame.grid(row=0, column=1, sticky="w")  # Date on the left side

    MonthFrame = tk.Frame(LeftDiv, bg="black", height=30)
    MonthFrame.grid(row=0, column=0, sticky="w")  # Month on the right side

    # Adding labels for Day, Date, and Month with custom font
    DayLabel = tk.Label(DayFrame, text=DAY, fg="white", bg="black", font="helvetica")  # Use custom_font directly
    DayLabel.pack(anchor="w")

    DateLabel = tk.Label(DateFrame, text=DATE, fg="white", bg="black", font="helvetica")  # Use custom_font directly
    DateLabel.pack(anchor="w")

    MonthLabel = tk.Label(MonthFrame, text=MONTH, fg="white", bg="black", font="helvetica")  # Use custom_font directly
    MonthLabel.pack(anchor="w")

