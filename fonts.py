from tkinter import font

def get_font_from_config(config):
    return font.Font(family=config['family'], size=config['size'], weight=config['weight'])

def set_font(text, config, font_name):
    config['family'] = font_name
    f = font.Font(family=font_name, size=config['size'], weight=config['weight'])
    text['font'] = f

def set_font_size(text, config,  size):
    config['size'] = size
    f = font.Font(family=config['family'], size=size, weight=config['weight'])
    text['font'] = f

def set_font_weight(text, config, weight):
    config['weight'] = weight
    f = font.Font(family=config['family'], size=config['size'], weight=weight)
    text['font'] = f
