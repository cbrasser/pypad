import tkinter as tk
from file_utils import save_as, load_from, save
from edit_commands import *
from fonts import *
from colors import color_dic
import entities

def init_menubar(frame):
    frame.menubar['borderwidth'] = 0
    init_file_menu(frame)
    init_font_menu(frame)

def init_file_menu(frame):
    file_dialog=tk.Menu(frame.menubar, tearoff=0)
    file_dialog.configure(activebackground=color_dic['purple'],activeforeground=color_dic['white'], border = 0)
    file_dialog.add_command(label='save', command= lambda : save(frame.text))
    file_dialog.add_command(label='save as', command= lambda : save_as(frame.text))
    file_dialog.add_command(label='open', command= lambda : load_from(frame.text))
    frame.bind_all('<Control-Shift-S>', lambda event : save_as(frame.text))
    frame.bind_all('<Control-s>', lambda event : save(frame.text))
    frame.bind_all('<Control-o>', lambda event : load_from(frame.text))
    frame.menubar.add_cascade(label='File', menu=file_dialog)
def init_font_menu(frame):
    font_dialog=tk.Menu(frame.menubar, tearoff=0)
    font_dialog.configure(activebackground=color_dic['purple'],activeforeground=color_dic['white'], bd = 0)
    font_dialog.add_command(label='Courier', command= lambda : set_font(frame.text, frame.font_config,'Courier'))
    font_dialog.add_command(label='Helvetica', command=lambda : set_font(frame.text, frame.font_config, 'Helvetica'))
    font_dialog.add_command(label='20', command=lambda : set_font_size(frame.text, frame.font_config, 20))
    font_dialog.add_command(label='10', command=lambda : set_font_size(frame.text, frame.font_config, 10))

    frame.menubar.add_cascade(label='Font', menu=font_dialog)

def init_edit_menu(frame):
    edit_dialog=tk.Menu(frame.menubar, tearoff=0)
    edit_dialog.configure(activebackground=color_dic['purple'],activeforeground=color_dic['white'], bd = 0)
    edit_dialog.add_command(label='Undo', command= lambda : frame.text.edit_undo(), accelerator='ctrl + z')
    edit_dialog.add_command(label='Redo', command= lambda : frame.text.edit_redo(), accelerator='ctrl + shift + z')
    edit_dialog.add_command(label='Cut', command= lambda : frame.text.event_generate('<<Cut>>'), accelerator='ctrl + x')
    edit_dialog.add_command(label='Copy', command= lambda : frame.text.event_generate('<<Copy>>'), accelerator='ctrl + c')
    edit_dialog.add_command(label='Paste', command= lambda : frame.text.event_generate('<<Paste>>'), accelerator='ctrl + v')
    edit_dialog.add_command(label='Select all', command= lambda : select_all(frame.text), accelerator='ctrl + a')
    edit_dialog.add_command(label='Search', command= lambda : search(frame))
    frame.bind_all('<Control-a>', lambda event, arg=frame.text : select_all(arg, event))
    frame.bind_all('<Control-f>', lambda event : frame.toggle_search_bar())
    frame.menubar.add_cascade(label='Edit', menu=edit_dialog)

def init_text_box(frame):
    frame.text = entities.Text_widget(frame)
    frame.text.configure(background=frame.color_config['bg'], foreground = frame.color_config['font'], undo=True)
    frame.text.font = get_font_from_config(frame.font_config)
    frame.text.pack(side='top', fill='both', expand = True)

def init_search_bar(frame):
    frame.search_bar = tk.Text(frame)
    frame.search_bar.configure(background=frame.color_config['bg'], foreground = frame.color_config['font'], undo=True, height=1)
    frame.search_bar.bind('<Return>', lambda event, arg1 = frame: search(frame, event))
