import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os


class Product:
    def __init__(self, code, name, price, stock, image):
        self.code = code
        self.name = name
        self.price = price
        self.stock = stock
        self.image = image


class VendingMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vending Machine")
        self.root.geometry("1140x720")
        self.root.resizable(False, False)
        self.root.configure(bg="#111")

        self.money = 0
        self.image_cache = {}

        self.products = [
            Product("A1","Lays Classic Chips",5,5,"lays.png"),
            Product("A2","Lays BBQ Chips",5,5,"laysbbq.png"),
            Product("A3","Pringles Original",6,5,"pringles.png"),
            Product("A4","Doritos Nacho",6,5,"doritos.png"),

            Product("B1","KitKat Chocolate",6,4,"kitkat.png"),
            Product("B2","Snickers Bar",6,4,"snickers.png"),
            Product("B3","Mars Chocolate",6,4,"mars.png"),
            Product("B4","Dairy Milk",7,4,"diarymilk.png"),

            Product("C1","Mountain Dew",4,6,"mountaindew.png"),
            Product("C2","Pepsi",4,6,"pepsi.png"),
            Product("C3","Sprite",4,6,"sprite.png"),
            Product("C4","Fanta Orange",4,6,"fanta.png"),

            Product("D1","Masafi Water",3,8,"masafi.png"),
            Product("D2","Al Ain Water",3,8,"alain.png"),
            Product("D3","Nestle Water",3,8,"nestle.png"),
            Product("D4","Aquafina Water",3,8,"aquafina.png"),
        ]

        self.build_ui()

    # GUI
    def build_ui(self):
        container = tk.Frame(self.root, bg="#111")
        container.pack(fill="both", expand=True)

        # PRODUCT PANEL
        self.product_panel = tk.Frame(
            container, bg="#111", width=760, height=700, bd=6, relief="ridge"
        )
        self.product_panel.grid(row=0, column=0, sticky="nw", padx=(5,0), pady=10)
        self.product_panel.grid_propagate(False)

        tk.Label(
            self.product_panel,
            text="VENDING MACHINE",
            fg="white",
            bg="#111",
            font=("Arial", 22, "bold")
        ).pack(pady=6)

        canvas = tk.Canvas(
            self.product_panel, bg="#111",
            highlightthickness=0, width=740, height=650
        )
        scrollbar = tk.Scrollbar(self.product_panel, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both")

        self.products_frame = tk.Frame(canvas, bg="#111")
        canvas.create_window((0, 0), window=self.products_frame, anchor="nw")

        self.products_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        self.draw_products()

        # PAYMENT PANEL
        self.payment_panel = tk.Frame(
            container, bg="#1f2933", width=320, height=680
        )
        self.payment_panel.grid(row=0, column=1, sticky="nw", padx=(0,5), pady=10)
        self.payment_panel.grid_propagate(False)

        tk.Label(
            self.payment_panel, text="PAYMENT",
            fg="white", bg="#1f2933",
            font=("Arial", 22, "bold")
        ).pack(pady=8)

        tk.Label(
            self.payment_panel, text="Enter Item Code",
            fg="white", bg="#1f2933",
            font=("Arial", 12)
        ).pack()

        self.code_entry = tk.Entry(
            self.payment_panel,
            font=("Arial", 22, "bold"),
            justify="center"
        )
        self.code_entry.pack(fill="x", padx=25, ipady=6, pady=6)

        keypad = tk.Frame(self.payment_panel, bg="#1f2933")
        keypad.pack(pady=4)

        for r,row in enumerate([["A","B","C","D"],["1","2","3","4"]]):
            for c,val in enumerate(row):
                tk.Button(
                    keypad, text=val,
                    font=("Arial",10,"bold"),
                    width=5, height=2,
                    command=lambda v=val: self.code_entry.insert(tk.END, v)
                ).grid(row=r, column=c, padx=4, pady=4)

        tk.Button(
            keypad, text="CLEAR",
            bg="#dc2626", fg="white",
            font=("Arial",12,"bold"),
            width=22,
            command=lambda: self.code_entry.delete(0, tk.END)
        ).grid(row=2, column=0, columnspan=4, pady=6)

        tk.Label(
            self.payment_panel, text="Insert Money (AED)",
            fg="white", bg="#1f2933",
            font=("Arial",12)
        ).pack(pady=4)

        self.money_label = tk.Label(
            self.payment_panel, text="AED 0",
            fg="yellow", bg="#1f2933",
            font=("Arial",12,"bold")
        )
        self.money_label.pack()

        money_pad = tk.Frame(self.payment_panel, bg="#1f2933")
        money_pad.pack(pady=4)

        nums = [[1,2,3],[4,5,6],[7,8,9],[0]]
        for r,row in enumerate(nums):
            for c,val in enumerate(row):
                tk.Button(
                    money_pad, text=str(val),
                    font=("Arial",12,"bold"),
                    width=5, height=2,
                    command=lambda v=val: self.add_money(v)
                ).grid(row=r, column=c, padx=4, pady=4)

        tk.Button(
            keypad, text="CLEAR",
            bg="#dc2626", fg="white",
            font=("Arial",12,"bold"),
            width=22,
            command=lambda: self.code_entry.delete(0, tk.END)
        ).grid(row=2, column=0, columnspan=4, pady=6)

        
        tk.Button(
            self.payment_panel, text="PUSH",
            bg="#2563eb", fg="white",
            font=("Arial",12,"bold"),
            height=2,
            command=self.process_payment
        ).pack(fill="x", padx=25, pady=10)

    # PRODUCTS
    def draw_products(self):
        for w in self.products_frame.winfo_children():
            w.destroy()

        r = c = 0
        for p in self.products:
            card = tk.Frame(
                self.products_frame, bg="#222",
                width=220, height=260,
                bd=2, relief="ridge"
            )
            card.grid(row=r, column=c, padx=25, pady=30)
            card.grid_propagate(False)

            img = self.load_image(p.image)
            tk.Label(card, image=img, bg="#222").pack(pady=6)

            tk.Label(
                card, text=p.name,
                fg="white", bg="#222",
                font=("Arial",11,"bold"),
                wraplength=200,
                justify="center"
            ).pack()

            tk.Label(card, text=f"AED {p.price}", fg="#9ca3af", bg="#222", font=("Arial",10)).pack()
            tk.Label(card, text=f"Code: {p.code}", fg="yellow", bg="#222", font=("Arial",10,"bold")).pack()
            tk.Label(card, text=f"Stock: {p.stock}", fg="#9ca3af", bg="#222", font=("Arial",10)).pack()

            c += 1
            if c == 4:
                c = 0
                r += 1

    # LOGIC 
    def load_image(self, filename):
        path = os.path.join(os.path.dirname(__file__), "images", filename)
        if path in self.image_cache:
            return self.image_cache[path]
        try:
            img = Image.open(path).resize((120,70), Image.LANCZOS)
        except:
            img = Image.new("RGB",(120,70),"#444")
        photo = ImageTk.PhotoImage(img)
        self.image_cache[path] = photo
        return photo

    def add_money(self, amt):
        self.money += amt
        self.money_label.config(text=f"AED {self.money}")

    def process_payment(self):
        code = self.code_entry.get().strip().upper()
        item = next((p for p in self.products if p.code == code), None)

        if not item:
            messagebox.showerror("Error","Invalid Code")
            return
        if item.stock <= 0:
            messagebox.showerror("Out of Stock","Item sold out")
            return
        if self.money < item.price:
            messagebox.showerror("Error","Not enough money")
            return

        change = self.money - item.price
        item.stock -= 1

        messagebox.showinfo("Success", f"{item.name} dispensed\nChange: AED {change}")

        self.money = 0
        self.money_label.config(text="AED 0")
        self.code_entry.delete(0, tk.END)
        self.draw_products()


if __name__ == "__main__":
    root = tk.Tk()
    VendingMachineApp(root)
    root.mainloop()