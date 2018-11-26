import tkinter as tk
from tkinter import filedialog

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.init_widgets()

    def init_widgets(self):
        self.text = tk.Text(self)
        self.text.pack(side="top")
        self.button=tk.Button(root, text="Save", command=self.saveas)
        self.button.pack(side="bottom")


    def saveas(self):
        text = self.text.get("1.0", "end-1c")
        path=filedialog.asksaveasfilename()

        # TODO: Checkout which exceptions can be thrown here and handle them
        with open(path, "w+") as file:
            file.write(text)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
