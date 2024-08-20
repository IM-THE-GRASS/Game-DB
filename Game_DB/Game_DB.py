"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import typing
from rxconfig import config
from Game_DB.components.keybind import Keybind
class State(rx.State):
    search_value:str = ""
    search_focus:bool = False
    
    def submit_search(self):
        if self.search_focus:
            return rx.redirect(f"/search?query={self.search_value}")
    def on_search_focus(self):
        self.search_focus = True
    def on_search_unfocus(self):
        self.search_focus = False
    def on_search_change(self, new):
        self.search_value = new
    def print(self):
        print("AAA")
    






def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        Keybind(
            keys=["Enter"],
            bind=lambda key:State.submit_search(),
        ),
        rx.image(
            src="/gamedblogo.svg",
            position="absolute",
            
            left="24vw",
            top="17vh",
            width="52vw",
            height="21vh"
        ),
        rx.box(
            rx.hstack(
                rx.input(
                    font_size="6.5vh",
                    height="11.2vh",
                    width="100%",
                    value=State.search_value,
                    on_change=State.on_search_change,
                ),
                rx.center(
                    rx.link(
                        rx.icon(
                            "search",
                            size=50
                        ),
                        as_child=True
                    ),
                    on_click=State.submit_search,
                    width="auto",
                    height="11.2vh",
                    padding="1vw"
                    
                ),
                on_focus=State.on_search_focus,
                on_blur=State.on_search_unfocus,
                spacing="0"
            ),
            
            position="absolute",
            width="32.604vw",
            height="11.2vh",
            left="32.604vw",
            top="44.4vh",
            border="0.109vh solid #CEC8D4"
        ),
        
        rx.box(
            rx.hstack(
                rx.image(
                    width="7.6vw",
                    height="6.3vh",
                    src="/gamechip.svg"
                ),
                rx.image(
                    width="7.6vw",
                    height="6.3vh",
                    src="/consolechip.svg"
                ),
                rx.image(
                    width="7.6vw",
                    height="6.3vh",
                    src="/eventchip.svg"
                ) ,
                rx.image(
                    width="7.6vw",
                    height="6.3vh",
                    src="/characterchip.svg"
                ) 
            ),
            position="absolute",
            top="57.345vh",
            left="33.75vw",
            width="32vw",
            height="6.3vh"
        ),
    )
def card(_) -> rx.Component:
    rx.box(
        width="12.5vw",
        height="43.199vh",
        border="0.109vh solid #CEC8D4"
    ),  
def search() -> rx.Component:
    return rx.box(
        rx.link(
            rx.image(
                src="/gamedblogo.svg",
                position="absolute",
                
                left="0.3vw",
                top="2.5vh",
                width="35vw",
                height="13.3vh"
            ),
            href="/"
        ),
        
        rx.hstack(
            rx.input(
                font_size="6.5vh",
                height="11.2vh",
                width="100%",
                value=State.search_value,
                on_change=State.on_search_change
            ),
            rx.center(
                
                rx.icon(
                    "search",
                    size=83
                ) ,
                width="11.2vh",
                height="100%",
                padding="1vh",
                on_click=State.submit_search
                
            ),
            left="35vw",
            top="4vh",
            position="absolute",
            border="0.109vh solid #CEC8D4",
            height="11.2vh",
            width="63vw",
            on_blur=State.on_search_unfocus,
            on_focus=State.on_search_focus
        ),
        rx.grid(
            rx.foreach(
                rx.Var.range(14),
                lambda i: rx.vstack(
                    rx.image(
                        src="https://cloud-mdyzmeysm-hack-club-bot.vercel.app/0og.png",
                        width="100%",
                        height="27vh",
                        object_fit="contain"
                    ),
                    rx.vstack(
                        rx.text(
                            "Super Smash Bros.",
                            font_size="2.2vh",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Wii/N64",
                            font_size="2.2vh",
                        ),
                        rx.text(
                            "1999",
                            font_size="2.2vh",
                        ),
                        width="11vw",
                        height="8.7vh",
                        spacing="0"
                        
                    ),
                    padding="0.833vw",
                    width="12.5vw",
                    height="48vh",
                    border="0.109vh solid #CEC8D4"
                ),  
            ),
            position="absolute",
            left="3vw",
            top="27vh",
            columns="7",
            spacing="8",
            width="90%"
        )
    )

app = rx.App(stylesheets=["./styles.css"])
app.add_page(index)
app.add_page(search)
