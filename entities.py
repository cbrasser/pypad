import tkinter as tk
from file_utils import *
from edit_commands import *
from fonts import *
from colors import color_dic

class Menubar_submenu(tk.Menu):
    def __init__(self, master = None, tearoff = 0):
        super().__init__(master)
        self.master = master
        self.configure(activebackground=color_dic['purple'],activeforeground=color_dic['white'], border = 0)

class Menubar(tk.Menu):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self['borderwidth'] = 0
        self.init_menus()
        self.init_shortcuts()

    def init_menus(self):
        self.init_file_menu()
        self.init_font_menu()
        self.init_edit_menu()

    def init_shortcuts(self):
        self.master.bind_all('<Control-Shift-S>', lambda event : save_as(self.master.text))
        self.master.bind_all('<Control-s>', lambda event : save(self.master.text))
        self.master.bind_all('<Control-o>', lambda event : load_from(self.master.text))
        self.master.bind_all('<Control-a>', lambda event, arg=self.master.text : select_all(arg, event))
        self.master.bind_all('<Control-f>', lambda event : self.master.toggle_search_bar())

    def init_file_menu(self):
        file_dialog=Menubar_submenu(self)
        file_dialog.add_command(label='save', command= lambda : save(self.master.text))
        file_dialog.add_command(label='save as', command= lambda : save_as(self.master.text))
        file_dialog.add_command(label='open', command= lambda : load_from(self.master.text))
        self.add_cascade(label='File', menu=file_dialog)


    def init_font_menu(self):
        font_dialog=Menubar_submenu(self)
        font_dialog.add_command(label='Courier', command= lambda : set_font(self.master.text, self.master.font_config,'Courier'))
        font_dialog.add_command(label='Helvetica', command=lambda : set_font(self.master.text, self.master.font_config, 'Helvetica'))
        font_dialog.add_command(label='20', command=lambda : set_font_size(self.master.text, self.master.font_config, 20))
        font_dialog.add_command(label='10', command=lambda : set_font_size(self.master.text, self.master.font_config, 10))
        self.add_cascade(label='Font', menu=font_dialog)

    def init_edit_menu(self):
        edit_dialog=Menubar_submenu(self)
        edit_dialog.add_command(label='Undo', command= lambda : self.master.text.edit_undo(), accelerator='ctrl + z')
        edit_dialog.add_command(label='Redo', command= lambda : self.master.text.edit_redo(), accelerator='ctrl + shift + z')
        edit_dialog.add_command(label='Cut', command= lambda : self.master.text.event_generate('<<Cut>>'), accelerator='ctrl + x')
        edit_dialog.add_command(label='Copy', command= lambda : self.master.text.event_generate('<<Copy>>'), accelerator='ctrl + c')
        edit_dialog.add_command(label='Paste', command= lambda : self.master.text.event_generate('<<Paste>>'), accelerator='ctrl + v')
        edit_dialog.add_command(label='Select all', command= lambda : select_all(self.master.text), accelerator='ctrl + a')
        edit_dialog.add_command(label='Search', command= lambda : search(self.master))
        self.add_cascade(label='Edit', menu=edit_dialog)


class Search_bar(tk.Text):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.configure(background=self.master.color_config['bg'], foreground = self.master.color_config['font'], undo=True, height=1)
        self.bind('<Return>', lambda event : search(self.master, event))

class Text_widget(tk.Text):
    def __init__(self, master = None, file =None):
        super().__init__(master)
        self.master = master
        self.file = file
        self.configure(background=self.master.color_config['bg'], foreground = self.master.color_config['font'], undo=True)
        self.font = get_font_from_config(self.master.font_config)
        self.pack(side='top', fill='both', expand = True)
