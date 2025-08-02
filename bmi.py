import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())/100
        bmi=weight/(height**2)



        bmi=round(bmi,2)

        if bmi < 18.5:
            category="You are underweight."
        elif 18.5 <= bmi < 24.9:
            category="You have a healthy weight."
        elif 25 <= bmi < 29.9:
            category="You are overweight."
        else:
            category="You are obese."
        messagebox.showinfo("BMI result",f"your BMI is {bmi}.\n{category}")
    except ValueError:
        messagebox.showerror("Error","Please enter valid numbers.")

root=tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

label_title=tk.Label(root,text="BMI Calculator",font=('Helvetica',16, "bold"),bg="#f0f0f0")
label_title.pack(pady=10)

input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=5)

tk.Label(input_frame, text="Height (cm):", font=("Helvetica", 11), bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5, sticky="e")
height_entry = tk.Entry(input_frame, font=("Helvetica", 11), width=10)
height_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Weight (kg):", font=("Helvetica", 11), bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5, sticky="e")
weight_entry = tk.Entry(input_frame, font=("Helvetica", 11), width=10)
weight_entry.grid(row=1, column=1, padx=5, pady=5)

calculate_button = tk.Button(root, text="Calculate BMI", font=("Helvetica", 11), bg="#4CAF50", fg="white", command=calculate_bmi)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f0f0", wraplength=280, justify="center")
result_label.pack(pady=10)

root.mainloop()


