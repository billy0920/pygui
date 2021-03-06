# -*- coding: utf-8 -*-
import Tkinter as Tk


class Layout(object):
    def __init__(self):
        pass

    def do_layout(self, parent):
        pass

    def add(self, comp, position):
        pass


class BorderLayout(Layout):
    def __init__(self):
        Layout.__init__(self)
        self.__components = {}

    def add(self, comp, position):
        self.__components[position] = comp

    def __place_comp(self, parent, position, pos_para):
        comp = self.__components.get(position)
        if comp:
            pos_comp = comp.make_comp(parent)
            pos_comp.grid(**pos_para)

    def do_layout(self, parent):
        parent.columnconfigure(0, weight=1)
        parent.columnconfigure(1, weight=10)
        parent.columnconfigure(2, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.rowconfigure(1, weight=10)
        parent.rowconfigure(2, weight=1)
        self.__place_comp(parent, "north", {"row": 0, "column": 0, "columnspan": 3, "sticky": Tk.NSEW})
        self.__place_comp(parent, "south", {"row": 2, "column": 0, "columnspan": 3, "sticky": Tk.NSEW})
        self.__place_comp(parent, "west", {"row": 1, "column": 0, "sticky": Tk.NSEW})
        self.__place_comp(parent, "east", {"row": 1, "column": 2, "sticky": Tk.NSEW})
        self.__place_comp(parent, "center", {"row": 1, "column": 1, "sticky": Tk.NSEW})


class Component(object):
    def __init__(self):
        self.layout = Layout()

    def set_layout(self, layout):
        self.layout = layout

    def make_comp(self, parent):
        pass

    def add(self, comp, position=None):
        self.layout.add(comp, position)


class TextField(Component):
    def __init__(self, text=""):
        Component.__init__(self)
        self.text = text

    def make_comp(self, parent):
        text_filed = Tk.Entry(parent, text=self.text)
        return text_filed


class Label(Component):
    def __init__(self, text=""):
        Component.__init__(self)
        self.text = text

    def make_comp(self, parent):
        label = Tk.Label(parent, text=self.text)
        return label


class Button(Component):
    def __init__(self, text="", action=None):
        Component.__init__(self)
        self.text = text
        self.action = action

    def make_comp(self, parent):
        button = Tk.Button(parent, text=self.text, command=self.action)
        return button


class Frame(Component):
    def __init__(self, title="PyGUI", width=800, height=400):
        Component.__init__(self)
        self.width = width
        self.height = height
        self.root = Tk.Tk(className=title)
        self.frame = Tk.Frame(self.root)
        self.set_center()

    def set_center(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        pos_x = (screen_width - self.width) / 2
        pos_y = (screen_height - self.height) / 2
        self.root.geometry("%sx%s+%s+%s" % (self.width, self.height, pos_x, pos_y))

    def show(self):
        self.frame.grid(row=0, column=0, sticky=Tk.NSEW)
        root = self.root
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.layout.do_layout(self.frame)

        self.root.mainloop()


class Panel(Component):
    def __init__(self, width=800, height=400):
        Component.__init__(self)
        self.width = width
        self.height = height

    def make_comp(self, parent):
        panel = Tk.PanedWindow(parent, width=self.width, height=self.height)
        self.layout.do_layout(panel)
        return panel


def hello():
    print "hello world"


if __name__ == "__main__":
    FRAME = Frame(width=800, height=400)
    FRAME.set_layout(BorderLayout())
    FRAME.add(Button("center", action=hello), "center")
    FRAME.add(Button("north"), "north")
    FRAME.add(Button("south"), "south")
    FRAME.add(Button("west"), "west")
    FRAME.add(Button("east"), "east")
    for pos in ["center", "south", "north", "east", "west"]:
        PANEL = Panel()
        PANEL.set_layout(BorderLayout())
        PANEL.add(Button("center", action=hello), "center")
        PANEL.add(Button("north"), "north")
        PANEL.add(Button("south"), "south")
        PANEL.add(Button("west"), "west")
        PANEL.add(Button("east"), "east")
        FRAME.add(PANEL, pos)
    FRAME.show()
