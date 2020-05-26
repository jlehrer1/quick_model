import tkinter as tk 

class Application(tk.Frame):
    def __init__(self, parent=None):
        self.parent = parent
        self.parent.title('Quick CNN')
        self.parent.geometry('500x600')
        self.label = tk.Label(self.parent, text='Enter your search term: ')
        self.label.pack()

        self.entry = tk.Entry(self.parent)
        self.train_model(self.entry.get())


    def train_model(self, text: str):
        if text == None or text.strip() == '':
            return
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(parent=root)
    root.mainloop()