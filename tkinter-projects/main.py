import tkinter as tk

window = tk.Tk()
window.title("Welcome to Xerox Paarc")
window.minsize(width=200, height=100)
window.config(padx=100 , pady=100)

user_input = tk.Entry(window, width=10)
user_input.grid(column = 1, row = 0)

miles = tk.Label(window, text="MILES")
miles.grid(column = 2,row= 0)

is_equal_to = tk.Label(window, text="IS EQUAL TO")
is_equal_to.grid(column = 0,row= 1)
output = tk.Entry(window, width=10)
output.grid(column = 1, row = 1)

km = tk.Label(window, text="KM")
km.grid(column = 2,row= 1)

def calculate():
    input = float(user_input.get())
    output_km = input * 1.60934
    output.insert(0, output_km)

button = tk.Button(window, text="CALCULATE", command=calculate)
button.grid(column = 1 , row = 2)




window.mainloop()
