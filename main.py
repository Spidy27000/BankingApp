import tkinter as tk
print("Tkinter Version:", tk.TkVersion)

class Page(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

    def show(self):
        self.lift()

class StartPage(Page):
    def __init__(self, parent, *args, **kwargs):
        Page.__init__(self, parent, *args, **kwargs)
        self.label = tk.Label(self, text="This is the start page")
        self.label.pack(side="top", fill="both", expand=True)

        self.page1_button = tk.Button(self, text="Go to Page 1", command=lambda: parent.show_page(Page1))
        self.page1_button.pack(side="top", fill="both", expand=True)

        self.page2_button = tk.Button(self, text="Go to Page 2", command=lambda: parent.show_page(Page2))
        self.page2_button.pack(side="top", fill="both", expand=True)

class Page1(Page):
    def __init__(self, parent, *args, **kwargs):
        Page.__init__(self, parent, *args, **kwargs)
        self.label = tk.Label(self, text="This is page 1")
        self.label.pack(side="top", fill="both", expand=True)

        self.page2_button = tk.Button(self, text="Go to Page 2", command=lambda: parent.show_page(Page2))
        self.page2_button.pack(side="top", fill="both", expand=True)

        self.start_button = tk.Button(self, text="Go to Start Page", command=lambda: parent.show_page(StartPage))
        self.start_button.pack(side="top", fill="both", expand=True)

class Page2(Page):
    def __init__(self, parent, *args, **kwargs):
        Page.__init__(self, parent, *args, **kwargs)
        self.label = tk.Label(self, text="This is page 2")
        self.label.pack(side="top", fill="both", expand=True)

        self.page1_button = tk.Button(self, text="Go to Page 1", command=lambda: parent.show_page(Page1))
        self.page1_button.pack(side="top", fill="both", expand=True)

        self.start_button = tk.Button(self, text="Go to Start Page", command=lambda: parent.show_page(StartPage))
        self.start_button.pack(side="top", fill="both", expand=True)

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.pages = {}
        for PageClass in (StartPage, Page1, Page2):
            page = PageClass(container, self)
            self.pages[PageClass] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page(StartPage)

    def show_page(self, page_class):
        page = self.pages[page_class]
        page.show()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()