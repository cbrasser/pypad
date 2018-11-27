import tkinter as tk
from widgets import init_menubar, init_text_box, init_text_box
from fonts import get_font_from_config
from colors import color_dic

class Application(tk.Frame):
    def __init__(self, master=None, font_config_from_file = False):
        super().__init__(master)
        self.master = master
        self.pack()
        self.init_font()
        self.init_colors()
        # TODO: implement file config
        self.init_widgets()
    def init_widgets(self):
        self.menubar = tk.Menu(root)
        init_menubar(self)
        init_text_box(self)
        root.config(menu=self.menubar)
    def init_font(self):
        self.font_config = {}
        self.font_config['family'] = 'Helvetica'
        self.font_config['size'] = 14
        self.font_config['weight'] = 'normal'
    def init_colors(self):
        self.color_config = {}
        self.color_config['bg'] = color_dic['dark_2']
        self.color_config['font'] = color_dic['white']


root = tk.Tk()
app = Application(master=root)
app.mainloop()
