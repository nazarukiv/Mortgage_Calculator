from tkinter import *

def payment():
    if amount_entry.get() and interest_entry.get() and term_entry.get():
        years = int(term_entry.get())
        months = years * 12
        rate = float(interest_entry.get())
        laon = int(amount_entry.get())
        # Calculate the Loan
        # Monthly Interest Rate
        monthly_rate = rate / 100 / 12
        # Get our payment
        payment = (monthly_rate / (1 - (1 + monthly_rate)**(-months))) * laon
        #Return statment
        payment_label.config(text=f"Your monthly payment is ${payment:.2f}")
    else:
        payment_label.config(text="All fields are required")

root = Tk()
root.title("Mortgage Calculator")
root.iconbitmap("/Users/ivan/Desktop/coding/programming/petprojects/Mortgage_Calculator/6676681.png")
root.geometry("500x400")

my_label_frame = LabelFrame(root, text="Mortgage Calculator")
my_label_frame.pack(pady=20, padx=20)

my_frame = Frame(my_label_frame)
my_frame.pack(pady=20)

# Labels and Entry Boxes
amount_label = Label(my_frame, text="Loan Amount")
amount_entry = Entry(my_frame, font=("Helvetica", 18))

interest_label = Label(my_frame, text="Interest Rate")
interest_entry = Entry(my_frame, font=("Helvetica", 18))

term_label = Label(my_frame, text="Term (Years)")
term_entry = Entry(my_frame, font=("Helvetica", 18))

amount_label.grid(row=0, column=0)
amount_entry.grid(row=0, column=1)

interest_label.grid(row=1, column=0)
interest_entry.grid(row=1, column=1, pady=20) 

term_label.grid(row=2, column=0)
term_entry.grid(row=2, column=1)

# Button
my_button = Button(my_label_frame, text="Calculate Payment", command=payment)
my_button.pack(pady=20)

payment_label = Label(root, text="", font=("Helvetica", 18))
payment_label.pack()

root.mainloop()
