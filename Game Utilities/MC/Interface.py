import tkinter as tk

class Interface:
    def __init__(self):
        self.window = tk.Tk()
        self.cells = []
        self.odds_labels = []

        validate_cmd = (self.window.register(self.validate_input), "%P")

        for i in range(10):
            reversed_index = (i + 1) % 10

            label = tk.Label(self.window, text=f"Slot {reversed_index}")
            label.grid(row=i, column=0, padx=10, pady=10)

            cell = tk.Entry(self.window, width=2, validate="key", validatecommand=validate_cmd)
            cell.grid(row=i, column=1, padx=10, pady=10)
            self.cells.append(cell)

            odds_label = tk.Label(self.window, text="", width=4)
            odds_label.grid(row=i, column=2, padx=10, pady=10)
            self.odds_labels.append(odds_label)

            cell.bind("<KeyRelease>", self.calculate_and_update_odds)

    def validate_input(self, value):
        if value == "" or (value.isdigit() and len(value) <= 2):
            return True
        else:
            return False

    def calculate_and_update_odds(self, event):
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

    def run(self):
        self.window.mainloop()