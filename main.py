import tkinter as  tk
from tkinter import ttk, messagebox

class ResturantApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Resturant App")
        self.root.geometry("600x500")

        self.menue = {
            "fries meal":2,
            "lunch meal":2,
            " burger meal":3,
            "chese burger":2.5,
            "drinks":1
        }

        try:
            self.bg= tk.PhotoImage()

            canvas = tk.canvas(root,width=600,height=500)
            canvas.pack(fil="both",expand=True)

            canvas.create_image(0,0, image=self.bg,anchor="nw")
            
            self.frame = ttk.Frame(root, padding=20)
            canvas.create_window(300,250, widow= slef.frame)

        except:
            self.frame= ttk.Frame(root,padding= 20)
            self.frame.pack(pady=20)

        ttk.Label(
                self.frame,
                text="Resturant order management"
                font=("Arial"18 , "bold")

            ).grid(row=0,columsspan=2,pady=10)

            self.qty= {}

            for i , (item,price) in enumerate(self.menue.items(),start = 1):
                tkk.Label(
                    self.frame,
                    text=f"{item} ($ {price})"

                ).grid(row=i, column=0, padx=10, pady=5)
                
                var = tk.IntVar()
                tk.Spinbox(

            tk.Spinbox(

tk.Spinbox(

self.frame,

    from_=0,

to=20,

        width=5,

        textvariable=var

        ).grid(row=i, column=1)
 
            ).grid(row=i, column=1)
            self.qty[item]=var

            ttk.Button(

self.frame,

text="Place Order",

command=self.place_order

).grid(row=8, column=0, pady=15)

ttk.Button(

self.frame,

text="Clear",

command=self.clear

).grid(row=8, column=1)

def place_order(self):

    ttk.Button(

self.frame,

text="Place Order",

command=self.place_order

).grid(row=8, column=0, pady=15)

ttk.Button(

    self.frame,

text="Clear",

command=self.clear

).grid(row=8, column=1)


    def clear(self):

    for var in self.qty.values():

var.set(0)

# Run app

root = tk.Tk()

app = RestaurantApp(root)

root.mainloop()


