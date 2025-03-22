import tkinter as tk
import pandas as pd
from matplotlib import pyplot as plt
import scipy.stats as stats

root=tk.Tk()
root.geometry("1000x750")
root.title("Expense Tracker App")
root.configure(bg="#081A40")

item_list=[]

def add_item():
    item=item_txt.get()
    qty=qty_txt.get()
    cost=cost_txt.get()
    total=int(qty) * int(cost)
    single_item_lbl=tk.Label(frame2, text=f"{item}\t\t{qty}\t\t{cost}\t\t{total}", bg="#081A40", fg="#ffffff", font=("Segoe UI", 15))
    single_item_lbl.pack(pady=5)
    single_item_list={"Item":item, "Quantity":qty, "Cost":cost, "Total Amount":total}
    item_list.append(single_item_list)

def clr_item():
    item_txt.delete(0, "end")    #Delete all characters of item_txt starting from posn 0 till end.
    qty_txt.delete(0, "end")
    cost_txt.delete(0, "end")

def analyse():
    df=pd.DataFrame(item_list)

    if not df.empty:
        mean_cost = df['Total Amount'].mean()
        median_cost = df['Total Amount'].median()
        mode_cost = stats.mode(df['Total Amount'], keepdims=True).mode[0] # Get mode

        # Print statistical results
        stats_lbl = tk.Label(root, text=f"Mean: {mean_cost:.2f} | Median: {median_cost:.2f} | Mode: {mode_cost}", bg="#081A40", fg="#ffffff", font=("Segoe UI", 15))
        stats_lbl.pack(pady=5)

        items=df['Item']
        total=df['Total Amount']
        fig=plt.figure(figsize=(10,5))
        plt.bar(items, total, color='#081A40', width=0.4)
        plt.xlabel("Items Puchased")
        plt.ylabel("Cost of Items")
        plt.title("Expense Tracker Analysis")
        plt.show()
    else:
        print("No expenses to analyze.")

#Item
title_lbl=tk.Label(root, text="Expense Tracker", bg="#081A40", fg="#ffffff", font=("Segoe UI Semibold", 20))
#Now a title label is created, but it won't be shown on screen because we haven't placed it on screen yet.
title_lbl.pack(pady=20)

item_lbl=tk.Label(root, text="Item", bg="#081A40", fg="#ffffff", font=("Segoe UI Semibold", 15))
item_lbl.pack(pady=(20,5))    #30 padding from top, 5 padding from bottom on Y-axis.

#Now, for text box, we will use tk.Entry().
item_txt=tk.Entry(root, font=("Arial 15"))
item_txt.pack()


#Quantity
qty_lbl=tk.Label(root, text="Quantity", bg="#081A40", fg="#ffffff", font=("Segoe UI Semibold", 15))
qty_lbl.pack(pady=(20,5))    

qty_txt=tk.Entry(root, font=("Arial 15"))
qty_txt.pack()


#Cost
cost_lbl=tk.Label(root, text="Cost per Unit", bg="#081A40", fg="#ffffff", font=("Segoe UI Semibold", 15))
cost_lbl.pack(pady=(20,5))    

cost_txt=tk.Entry(root, font=("Arial 15"))
cost_txt.pack()


#Use a frame to group items together (here, we want to group buttons together siuch that they're side by side).
frame1=tk.Frame(root, bg="#081A40")

add_btn=tk.Button(frame1, text="Add Item", bg="#004892", fg="#ffffff", font=("Arial", 15), command=add_item)
add_btn.pack(padx=10, pady=20, side=tk.LEFT)

clr_btn=tk.Button(frame1, text="Clear", bg="#004892", fg="#ffffff", font=("Arial", 15), command=clr_item)
clr_btn.pack(padx=10, pady=20, side=tk.RIGHT)

#Every widget created (Such as frame, label, textbox, etc.) must be packed. So we must pack frame now.
frame1.pack()


display_lbl=tk.Label(root, text="Expenses", bg="#081A40", fg="#ffffff", font=("Segoe UI", 17))
display_lbl.pack(pady=(20,5))   


frame2=tk.Frame(root, bg="#081A40")

# \t is tab
heading_lbl=tk.Label(root, text="Item\t\tQuantity\t\tUnit Cost\t\tTotal", bg="#081A40", fg="#ffffff", font=("Segoe UI", 15))
heading_lbl.pack(pady=5)   

frame2.pack()

analyse_btn=tk.Button(root, text="Analyse", bg="#004892", fg="#ffffff", font=("Arial", 15), command=analyse)
analyse_btn.pack(pady=30)


root.mainloop()
'''When root.mainloop() is called, it enters an infinite event loop, keeping the GUI window open and responsive.
If mainloop() is not called, the window might appear for a brief moment and then disappear as the script completes execution.'''
