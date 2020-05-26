import tkinter as tk 

class Application(tk.Frame):
    def __init__(self, parent=None):
        self.parent = parent
        self.parent.title('Quick CNN')
        self.parent.geometry('500x600')
        self.label = tk.Label(parent, text='Enter your search term: ')
        self.label.pack()

    def create_widgets(self):
        text = tk.Label(
            self,
        )
        self.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(parent=root)
    root.mainloop()