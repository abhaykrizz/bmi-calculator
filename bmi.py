import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
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

label_title=tk.Label(root,text="BMI Calculator",font=('Segoe UI',16))
label_title.pack(pady=10)

label_weight=tk.Label(root,text="Enter your weight in Kilograms : ")
label_weight.pack()
entry_weight=tk.Entry(root)
entry_weight.pack()

label_height=tk.Label(root,text="Enter your height in Metres : ")
label_height.pack()
entry_height=tk.Entry(root)
entry_height.pack()

btn=tk.Button(root,text="Calculate BMI",command=calculate_bmi)
btn.pack(pady=15)

root.mainloop()


