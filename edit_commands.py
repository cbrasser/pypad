from tkinter import *

def select_all(text_box, event=None):
    text_box.tag_add(SEL, '1.0', END)
    text_box.mark_set(INSERT, '1.0')
    text_box.see(INSERT)
    return 'break'

def search(frame, event=None):
    query = frame.search_bar.get('1.0', 'end-1c')
    if query.startswith('\n'):
        #for whatever reason i cant delete the newline char at the start of the textbox
        query = query[1:]
    frame.search_bar.delete('0.0', 'end')
    index = frame.text.search(query, '1.0')
    try:
        line, char = map(int, index.split('.'))
        frame.text.tag_add(SEL, f'{line}.{char}', f'{line}.{char+len(query)}')
        frame.text.mark_set(INSERT, f'{line}.{char}')
        frame.text.focus()
        frame.toggle_search_bar()
    except ValueError:
        print('No matches')
