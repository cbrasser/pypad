import tkinter as tk
from widgets import init_menubar, init_text_box, init_text_box, init_edit_menu, init_search_bar
from fonts import get_font_from_config
from colors import color_dic

class Text_widget(tk.Text):
    def __init__(self, master = None, file =None):
        super().__init__(master)
        self.master = master
        self.file = file

class Application(tk.Frame):
    def __init__(self, master=None, font_config_from_file = False):
        super().__init__(master)
        self.master = master
        self.pack(fill='both', expand=True)
        self.init_font()
        self.init_colors()

        # TODO: implement file config
        self.init_widgets()
    def init_widgets(self):
        self.menubar = tk.Menu(self.master)
        init_menubar(self)
        init_text_box(self)
        init_edit_menu(self)
        init_search_bar(self)
        self.master.config(menu=self.menubar)
    def init_font(self):
        self.font_config = {}
        self.font_config['family'] = 'Helvetica'
        self.font_config['size'] = 14
        self.font_config['weight'] = 'normal'
    def init_colors(self):
        self.color_config = {}
        self.color_config['bg'] = color_dic['dark_2']
        self.color_config['font'] = color_dic['white']

    def toggle_search_bar(self):
        if not self.search_bar.winfo_ismapped():
            self.search_bar.pack(side='bottom', fill='x')
            self.search_bar.focus()
        else:
            self.search_bar.pack_forget()
            self.text.focus()
