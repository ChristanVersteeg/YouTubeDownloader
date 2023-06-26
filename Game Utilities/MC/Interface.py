import tkinter as tk
import sys

class Interface:
    def __init__(self):
        self.window = tk.Tk()
        self.cells = []
        self.odds_labels = []
        self.paused = False
        self.window.iconbitmap(sys._MEIPASS + '\\ChiseledSandstone.ico' if hasattr(sys, '_MEIPASS') else 'ChiseledSandstone.ico')
        self.window.title("")
        
        validate_cmd = (self.window.register(self.validate_input), "%P")

        for i in range(9):
            label = tk.Label(self.window, text=f"Slot {i + 1}")
            label.grid(row=i, column=0, padx=10, pady=10)

            cell = tk.Entry(self.window, width=2, validate="key", validatecommand=validate_cmd)
            cell.grid(row=i, column=1, padx=10, pady=10)
            self.cells.append(cell)

            odds_label = tk.Label(self.window, text="", width=5)
            odds_label.grid(row=i, column=2, padx=10, pady=10)
            self.odds_labels.append(odds_label)

            cell.bind("<KeyRelease>", self.calculate_and_update_odds)

        # Add a fixed-width frame to contain the buttons
        button_frame = tk.Frame(self.window, width=25)
        button_frame.grid(row=10, column=0, columnspan=3)

        # Add the Pause/Unpause button
        self.pause_button = tk.Button(button_frame, text="Pause", command=self.toggle_pause, width=7)
        self.pause_button.pack(side="left", padx=10, pady=10)

        # Add the Stop button
        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop, width=7)
        self.stop_button.pack(side="right", padx=10, pady=10)

    def validate_input(self, value):
        if value == "" or (value.isdigit() and len(value) <= 2):
            return True
        else:
            return False

    def calculate_and_update_odds(self, event):
        if self.paused:
            return

        total_value = sum(int(cell.get()) for cell in self.cells if cell.get().isdigit())
        if total_value == 0:
            return  # Avoid division by zero

        for i, cell in enumerate(self.cells):
            if cell.get().isdigit():
                value = int(cell.get())
                cell_percentage = (value / total_value) * 100
                cell_percentage = round(cell_percentage, 1)
                cell_percentage = int(cell_percentage) if cell_percentage.is_integer() else cell_percentage
                self.odds_labels[i].config(text=f"{cell_percentage}%")
            else:
                self.odds_labels[i].config(text="")

    def toggle_pause(self):
        self.paused = not self.paused
        if self.paused:
            self.pause_button.config(text="Unpause")
        else:
            self.pause_button.config(text="Pause")

    def stop(self):
        self.window.destroy()

    def run(self):
        self.window.mainloop()