"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx 
from rxconfig import config
from Game_DB.components.keybind import Keybind
from Game_DB.state import State
from Game_DB.pages.search import search






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
 

app = rx.App(stylesheets=["./styles.css"])
app.add_page(index)
app.add_page(search)
