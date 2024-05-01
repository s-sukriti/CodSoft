import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.configure(background='lightpink')

        self.entry = tk.Entry(root, width=20, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        self.create_buttons()
        self.configure_grid()

    def create_buttons(self):
        row = 1
        col = 0
        for button in self.buttons:
            if button == '=':
                tk.Button(self.root, text=button, width=10, height=2, command=self.calculate).grid(row=row, column=col, padx=5, pady=5, sticky="ew")
            elif button == 'C':
                tk.Button(self.root, text=button, width=10, height=2, command=self.clear).grid(row=row, column=col, padx=5, pady=5, sticky="ew")
            else:
                tk.Button(self.root, text=button, width=10, height=2, command=lambda b=button: self.add_to_entry(b)).grid(row=row, column=col, padx=5, pady=5, sticky="ew")
            col += 1
            if col > 3:
                col = 0
                row += 1

    def configure_grid(self):
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)

    def add_to_entry(self, value):
        current_text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current_text + value)

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def clear(self):
        self.entry.delete(0, tk.END)


def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
