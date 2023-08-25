import pickle

def load_inverted_color_dict():
    color_dict = pickle.load(open("ansi_color_dict.pkl", "rb"))
    inverted_color_dict = {}
    for ansi, rgb in color_dict.items():
        inverted_color_dict[str(rgb)] = ansi
    return inverted_color_dict
