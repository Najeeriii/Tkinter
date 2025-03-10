import tkinter as tk 

window =tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.SUNKEN,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=8, pady=8)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn{j}")
        label.pack()
window.mainloop()