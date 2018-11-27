import tkinter as tk
from entities import Text_widget, Search_bar, Menubar
from colors import color_dic

class Application(tk.Frame):
    def __init__(self, master=None, font_config_from_file = False):
        super().__init__(master)
        self.master = master
        self.font_config = {}
        self.color_config = {}
        self.pack(fill='both', expand=True)
        self.init_font()
        self.init_colors()
        # TODO: implement file config
        self.init_widgets()
        #register menubar at root
        self.master.config(menu=self.menubar)

    def init_widgets(self):
        #initializing main text container, search bar, & menu bar
        self.text = Text_widget(self)
        self.search_bar = Search_bar(self)
        self.menubar = Menubar(self)

    def init_font(self):
        self.font_config['family'] = 'Helvetica'
        self.font_config['size'] = 14
        self.font_config['weight'] = 'normal'
    def init_colors(self):
        self.color_config['bg'] = color_dic['dark_2']
        self.color_config['font'] = color_dic['white']

    def toggle_search_bar(self):
        if not self.search_bar.winfo_ismapped():
            self.search_bar.pack(side='bottom', fill='x')
            self.search_bar.focus()
        else:
            self.search_bar.pack_forget()
            self.text.focus()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
