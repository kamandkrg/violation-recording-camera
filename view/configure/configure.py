import tkinter as tk


class Text(tk.Text):
    def __init__(self, master=None, **kwargs):
        if "bd" not in kwargs:
            kwargs["bd"] = 2

        if "bg" not in kwargs:
            kwargs["bg"] = "#E8EEFC"
        super(Text, self).__init__(master, **kwargs)


class Radiobutton(tk.Radiobutton):
    def __init__(self, master=None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = "#E2EAFC"

        if "activebackground" not in kwargs:
            kwargs["activebackground"] = "#C7D7FE"

        if "width" not in kwargs:
            kwargs["width"] = 15

        super(Radiobutton, self).__init__(master, **kwargs)


class TopLevel(tk.Toplevel):
    def __init__(self, master=None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = "#E2EAFC"
        super(TopLevel, self).__init__(master, **kwargs)


class Button(tk.Button):
    def __init__(self, master=None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = "#D2DFFD"

        if "relief" not in kwargs:
            kwargs["relief"] = "groove"

        if "activebackground" not in kwargs:
            kwargs["activebackground"] = "#C7D7FE"

        if "width" not in kwargs:
            kwargs["width"] = 15

        if "bd" not in kwargs:
            kwargs["bd"] = 2

        super(Button, self).__init__(master, **kwargs)


class Entry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        if "bd" not in kwargs:
            kwargs["bd"] = 2

        if "bg" not in kwargs:
            kwargs["bg"] = "#E8EEFC"
        super(Entry, self).__init__(master, **kwargs)


class Tk(tk.Tk):
    def __init__(self):
        super(Tk, self).__init__()
        self.config(bg="#E2EAFC")


class Frame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = "#E2EAFC"
        super(Frame, self).__init__(master, kwargs)


class Label(tk.Label):
    def __init__(self, master=None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = "#E2EAFC"

        if "font" not in kwargs:
            kwargs["font"] = ('Helvetica', 11, 'bold')
        super(Label, self).__init__(master, kwargs)


class LabelFrame(tk.LabelFrame):
    def __init__(self, master=None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = "#E2EAFC"

        if "font" not in kwargs:
            kwargs["font"] = ('Helvetica', 11)
        super(LabelFrame, self).__init__(master, kwargs)


class Scale(tk.Scale):
    def __init__(self, master=None, **kwargs):
        if "orient" not in kwargs:
            kwargs["orient"] = tk.HORIZONTAL
        if "bg" not in kwargs:
            kwargs["bg"] = "#D2DFFD"
        if "highlightbackground" not in kwargs:
            kwargs["highlightbackground"] = "#E3CF57"
        if "troughcolor" not in kwargs:
            kwargs["troughcolor"] = "#F5F5DC"
        if "activebackground" not in kwargs:
            kwargs["activebackground"] = "#9B9B29"
        if "width" not in kwargs:
            kwargs["width"] = 18
        if "length" not in kwargs:
            kwargs["length"] = 122
        if "orient" not in kwargs:
            kwargs["orient"] = "horizontal"
        super(Scale, self).__init__(master, kwargs)


class Spinbox(tk.Spinbox):
    def __init__(self, master=None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = "#E8EEFC"
        if "highlightbackground" not in kwargs:
            kwargs["highlightbackground"] = "#E3CF57"
        if "activebackground" not in kwargs:
            kwargs["activebackground"] = "#9B9B29"
        if "width" not in kwargs:
            kwargs["width"] = 18
        super(Spinbox, self).__init__(master, kwargs)


class Listbox(tk.Listbox):
    def __init__(self, master=None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = "#f5f3f4"
        if "highlightbackground" not in kwargs:
            kwargs["highlightbackground"] = "black"
        if "highlightthickness" not in kwargs:
            kwargs["highlightthickness"] = 2
        super(Listbox, self).__init__(master, **kwargs)













