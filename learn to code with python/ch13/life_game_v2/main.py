from tkinter import mainloop
from model import model_init
import json

def import_config():
    """
    Load config from config.json.
    """
    with open('config.json') as json_file:
        config = json.load(json_file)
    return config

def main():
    config = import_config()
    # print(type(config))
    # print(config)

    height = config['model_config']['height']
    width = config['model_config']['width']
    cell_size = config['grid_config']['cell_size']

    model = model_init.setup_model(height, width)

if __name__ == "__main__":
    mainloop()
