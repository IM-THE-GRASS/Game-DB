import reflex as rx

class State(rx.State):
    search_value:str = ""
    search_focus:bool = False
    
    def submit_search(self):
        if self.search_focus:
            return rx.redirect(f"/search")
    def on_search_focus(self):
        self.search_focus = True
    def on_search_unfocus(self):
        self.search_focus = False
    def on_search_change(self, new):
        self.search_value = new
    def print(self):
        print("AAA")