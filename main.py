import tkinter as tk
import tkinter.font as font

window = tk.Tk()
window.title("คำนวณอัตราแลกเปลี่ยนเงินไทยเป็นเงินดอลลาร์สหรัฐ")
window.geometry('600x230')

myFont = font.Font(size=15)

lblRate = tk.Label(window, text="ป้อนอัตราแลกเปลี่ยนเงินบาทไทยต่อ 1 ดอลลาร์ : ")
lblRate.grid(column=0, row=0, sticky=tk.W, pady=5)
lblRate.config(font=myFont)

txtRate = tk.Entry(window, width=15)
txtRate.grid(column=1, row=0, sticky=tk.W, pady=5)
txtRate.config(font=myFont)

lblBaht = tk.Label(window, text="ป้อนจำนวณเงินบาทไทย : ")
lblBaht.grid(column=0, row=1, sticky=tk.W, pady=5)
lblBaht.config(font=myFont)

txtBaht = tk.Entry(window, width=15)
txtBaht.grid(column=1, row=1, sticky=tk.W, pady=5)
txtBaht.config(font=myFont)

lblDollar = tk.Label(window, text="คำนวณเป็นเงินดอลลาร์ได้ : ")
lblDollar.grid(column=0, row=2, sticky=tk.W, pady=5)
lblDollar.config(font=myFont)

lblDollarResult = tk.Label(window, text="")
lblDollarResult.grid(column=1, row=2, sticky=tk.W, pady=5)
lblDollarResult.config(font=myFont)

def clicked() :
    dollar = float(txtBaht.get()) / float(txtRate.get())
    dollar = round(dollar, 2)
    lblDollarResult.configure(text= str(dollar) + " ดอลลาร์")

btn = tk.Button(window,  text="คำนวณ", command=clicked)
btn.grid(column=1, row=3, sticky=tk.W, pady=5)
btn.config(font=myFont)

window.mainloop
