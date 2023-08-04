from tkinter import *


def calculate():

    miles = float(mile_input.get())
    kilometer = round(miles * 1.60934, 3)
    km_lb["text"] = kilometer
    print(f"Complete Calculation: {miles} miles is equal to {kilometer} km.")


# Window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Labels
lb_1 = Label(text="Miles", font=15)
lb_1.grid(column=2, row=0)
lb_2 = Label(text="is equal to", font=15)
lb_2.grid(column=0, row=1)
lb_3 = Label(text="Km", font=15)
lb_3.grid(column=2, row=1)
km_lb = Label(text="0", font=15)
km_lb.grid(column=1, row=1)

# Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

# Entry
mile_input = Entry(width=7)
mile_input.grid(column=1, row=0)
print(mile_input.get())


window.mainloop()  # Keep window on
