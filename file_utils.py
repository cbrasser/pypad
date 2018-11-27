from tkinter import filedialog

def save_as(text_widget):

    path=filedialog.asksaveasfilename()

    # TODO: Checkout which exceptions can be thrown here and handle them
    try:
        with open(path, "w+") as file:
            file.write(text_widget.get("1.0", "end-1c"))
        text_widget.file = path
    except TypeError:
        print('something went wrong at saving file')
    except FileNotFoundError:
        print('file not found')

def save(text_widget):
    #This textbox is already registered to a file
    if text_widget.file:
        try:
            with open(text_widget.file, "w+") as file:
                file.write(text_widget.get("1.0", "end-1c"))
        except TypeError:
            print('something went wrong at saving file')
        except FileNotFoundError:
            print('file not found')
    else:
        save_as(text_widget)

def load_from(text_widget):
    path = filedialog.askopenfilename()
    content = ''
    try:
        with open(path, 'r') as file:
             content = file.read()
        text_widget.file = path
    except FileNotFoundError:
        print('file not found')
    text_widget.delete(1.0, 'end-1c')
    text_widget.insert('end-1c',content)

def new_file():
    pass

def quit():
    pass
