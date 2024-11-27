import tkinter as tk

suggestions = ["Paris", "Parthenay", "Paray-le-Monial", "Pau", "Perpignan", "Périgueux", "Poitiers"]

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("When 2 Launch")
        self.geometry("300x200")
        self.widgets()

    def widgets(self):
        self.city_label = tk.Label(self, text="City")
        self.city_label.place(x=10, y=10)

        self.city_entry = tk.Entry(self)
        self.city_entry.bind("<KeyRelease>", self.on_keyrelease)
        self.city_entry.place(x=10, y=35, width=200)

        self.list_box_frame = tk.Frame(self, bg="white", highlightthickness=1, highlightbackground="gray")
        self.list_box = tk.Listbox(self.list_box_frame, height=5, bg="white", bd=0, relief="flat", highlightthickness=0)
        self.list_box.pack(fill=tk.BOTH, expand=True)
        self.list_box.bind("<<ListboxSelect>>", self.on_listbox_select)

    def on_keyrelease(self, event):
        typed_text = self.city_entry.get().lower()
        self.list_box.delete(0, tk.END)

        if typed_text:
            filtered_suggestions = [item for item in suggestions if item.lower().startswith(typed_text)]
            if filtered_suggestions:
                self.list_box_frame.place(x=10, y=60, width=200)
                for suggestion in filtered_suggestions:
                    self.list_box.insert(tk.END, suggestion)
            else:
                self.list_box_frame.place_forget()
        else:
            self.list_box_frame.place_forget()

    def on_listbox_select(self, event):
        if self.list_box.curselection():
            selected_item = self.list_box.get(self.list_box.curselection())
            self.city_entry.delete(0, tk.END)
            self.city_entry.insert(0, selected_item)
            self.list_box_frame.place_forget()

if __name__ == "__main__":
    application = Main()
    application.mainloop()
