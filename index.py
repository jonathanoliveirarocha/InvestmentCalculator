import requests
from tkinter import *  

def result():   
    monthlyFee = (((1 + int(interestRate.get())/100)**(1/12)) - 1) * 1.05
    amount = int(initialCapital.get())
    for i in range(int(months.get())):
        amount += int(monthlyInjection.get())
        amount = amount * ( 1 + monthlyFee)
 
    result["text"] = "Your ROI will be (Accumulated amount): $" + str(round(amount, 2)) 
    

window = Tk()
window.title("Investment Calculator")

#First Label
first_text = Label(window, text="Hello, here we can easily simulate the returns on an investment!")
first_text.grid(column=0,row=0, padx=10, pady=10)


#Initial Capital
label_InitialCapital = Label(window, text="Initial Capital:")
label_InitialCapital.grid(column=0,row=1, padx=10, pady=10)

initialCapital = Entry(window)
initialCapital.grid(column=0, row=2)


#Monthly Injection
label_MonthlyInjection = Label(window, text="Monthly Injection:")
label_MonthlyInjection.grid(column=0,row=3, padx=10, pady=10)

monthlyInjection = Entry(window)
monthlyInjection.grid(column=0, row=4)


#Months
label_Months = Label(window, text="How many months:")
label_Months.grid(column=0,row=5, padx=10, pady=10)

months = Entry(window)
months.grid(column=0, row=6)


#Annual interest rate
label_InterestRate = Label(window, text="Annual interest rate:")
label_InterestRate.grid(column=0,row=7, padx=10, pady=10)

interestRate = Entry(window)
interestRate.grid(column=0, row=8)


#Result
btn = Button(window, text="Calculate", command=result)
btn.grid(column=0,row=9, padx=10, pady=10)

result = Label(window, text="")
result.grid(column=0,row=10, padx=10, pady=10)

window.mainloop()

