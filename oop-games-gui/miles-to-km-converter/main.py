import tkinter as tk

window = tk.Tk()
window.title("Mile to Kilometer CONVERTER")
window.minsize(width=600, height=450)
window.config(padx=200, pady=200)

def cal():
    number = int(input.get())
    print(type(number))
    k_number = str(round(number * 1.6, 1))
    fourth_label.config(text=k_number)

first_label = tk.Label(text="Miles", font=("Aerial", 15))
first_label.grid(row=0, column=2)

second_label = tk.Label(text="is equal to", font=("Aerial", 15))
second_label.grid(row=1, column=0)

third_label = tk.Label(text="Km", font=("Aerial", 15))
third_label.grid(row=1, column=2)

first_buttom = tk.Button(text="CALCULATE", font=("Aerial", 10), command=cal)
first_buttom.grid(row=2, column=1)

input = tk.Entry(width=10)
input.grid(row=0, column=0)

fourth_label = tk.Label(font=("Aerial", 15))
fourth_label.grid(row=1, column=1)

# def cal():
#     number = int(input.get())
#     k_number = number * 1.6
#     return k_number




window.mainloop()
