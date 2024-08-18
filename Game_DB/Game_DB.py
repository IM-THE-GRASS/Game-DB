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
                    font_size="60px",
                    height="103px",
                    width="100%"
                ),
                rx.center(
                    
                    rx.icon(
                        "search",
                        size=83
                    ) ,
                    width="103px",
                    height="100%",
                    padding="10px"
                    
                )
            ),
            
            position="absolute",
            width="626px",
            height="103px",
            left="647px",
            top="408px",
            border="1px solid #CEC8D4"
        ),
        
        rx.box(
            rx.hstack(
                rx.image(
                    width="146px",
                    height="58px",
                    src="/gamechip.svg"
                ),
                rx.image(
                    width="146px",
                    height="58px",
                    src="/consolechip.svg"
                ),
                rx.image(
                    width="146px",
                    height="58px",
                    src="/eventchip.svg"
                ) ,
                rx.image(
                    width="146px",
                    height="58px",
                    src="/characterchip.svg"
                ) 
            ),
            position="absolute",
            top="527px",
            left="648px",
            width="625px",
            height="58px"
        ),
    )


app = rx.App(stylesheets=["./styles.css"])
app.add_page(index)
