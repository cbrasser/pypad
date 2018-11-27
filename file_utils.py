from tkinter import filedialog

def save_as(text):

    path=filedialog.asksaveasfilename()

    # TODO: Checkout which exceptions can be thrown here and handle them
    try:
        with open(path, "w+") as file:
            file.write(text)
    except TypeError:
        print('something went wrong at saving file')
    except FileNotFoundError:
        print('file not found')

def save(text, path):
    try:
        with open(path, "w+") as file:
            file.write(text)
    except TypeError:
        print('something went wrong at saving file')
    except FileNotFoundError:
        print('file not found')

def load_from(text_widget):
    path = filedialog.askopenfilename()
    content = ''
    try:
        with open(path, 'r') as file:
             content = file.read()
    except FileNotFoundError:
        print('file not found')
    text_widget.delete(1.0, 'end-1c')
    text_widget.insert('end-1c',content)
