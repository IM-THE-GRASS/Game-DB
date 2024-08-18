"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
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
                    width="100%"
                ),
                rx.center(
                    
                    rx.icon(
                        "search",
                        size=83
                    ) ,
                    width="11.2vh",
                    height="100%",
                    padding="0.521vw"
                    
                )
            ),
            
            position="absolute",
            width="32.604vw",
            height="11.2vh",
            left="32.604vw",
            top="44.4vh",
            border="1px solid #CEC8D4"
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
        border="1px solid #CEC8D4"
    ),  
def search() -> rx.Component:
    return rx.box(
        rx.image(
            src="/gamedblogo.svg",
            position="absolute",
            
            left="7px",
            top="24px",
            width="655px",
            height="122px"
        ),
        rx.hstack(
            rx.input(
                font_size="60px",
                height="11.2vh",
                width="100%"
            ),
            rx.center(
                
                rx.icon(
                    "search",
                    size=83
                ) ,
                width="11.2vh",
                height="100%",
                padding="10px"
                
            ),
            left="35vw",
            top="37px",
            position="absolute",
            border="1px solid #CEC8D4",
            height="11.2vh",
            width="62.969"
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
                            font_size="20px",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Wii/N64",
                            font_size="20px",
                        ),
                        rx.text(
                            "1999",
                            font_size="20px",
                        ),
                        width="11vw",
                        height="8.7vh",
                        
                    ),
                    padding="0.833vw",
                    width="12.5vw",
                    height="43.2vh",
                    border="1px solid #CEC8D4"
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
