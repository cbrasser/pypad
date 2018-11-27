import tkinter as tk
from file_utils import save_as, load_from
from fonts import *
from colors import color_dic
def init_menubar(frame):
    frame.menubar['borderwidth'] = 0
    init_file_menu(frame)
    init_font_menu(frame)

def init_file_menu(frame):
    file_dialog=tk.Menu(frame.menubar, tearoff=0)
    file_dialog.configure(activebackground=color_dic['purple'],activeforeground=color_dic['white'], border = 0)
    file_dialog.add_command(label='save', command= lambda : save_as(frame.text.get("1.0", "end-1c")))
    file_dialog.add_command(label='open', command= lambda : load_from(frame.text))
    frame.menubar.add_cascade(label='File', menu=file_dialog)
def init_font_menu(frame):
    font_dialog=tk.Menu(frame.menubar, tearoff=0)
    font_dialog.configure(activebackground=color_dic['purple'],activeforeground=color_dic['white'], bd = 0)
    font_dialog.add_command(label='Courier', command= lambda : set_font(frame.text, frame.font_config,'Courier'))
    font_dialog.add_command(label='Helvetica', command=lambda : set_font(frame.text, frame.font_config, 'Helvetica'))
    font_dialog.add_command(label='20', command=lambda : set_font_size(frame.text, frame.font_config, 20))
    font_dialog.add_command(label='10', command=lambda : set_font_size(frame.text, frame.font_config, 10))
    frame.menubar.add_cascade(label='Font', menu=font_dialog)

def init_text_box(frame):
    frame.text = tk.Text(frame)
    frame.text.configure(background=frame.color_config['bg'], foreground = frame.color_config['font'])
    frame.text.font = get_font_from_config(frame.font_config)
    frame.text.pack(side='top')
