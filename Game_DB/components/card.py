import reflex as rx
from Game_DB.components.carousel import Slider
from Game_DB.state import State
def card(info, **kwargs):
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.vstack(
                rx.image(
                    src=info["img"],
                    width="100%",
                    height="27vh",
                    object_fit="contain"
                ),
                rx.vstack(
                    rx.text(
                        info["name"],
                        font_size="2.2vh",
                        font_weight="bold",
                    ),
                    rx.text(
                        info["platform"],
                        font_size="2.2vh",
                    ),
                    rx.text(
                        info["year"],
                        font_size="2.2vh",
                    ),
                    width="11vw",
                    height="8.7vh",
                    spacing="0"
                    
                ),
                padding="0.833vw",
                width="12.5vw",
                height="48vh",
                border="0.109vh solid #444444",
                border_radius="8px",
                **kwargs
            )
        ),
        rx.dialog.content(
            rx.hstack(
                rx.image(
                    src=info["img"],
                    height="50vh",
                    object_fit="contain"
                ),
                rx.vstack(
                    rx.heading(
                        info["name"],
                        font_size="5vh"
                    
                    ),
                    rx.box(
                        
                        rx.text(
                            info["summary"]  
                        ),
                        height="30vh",
                        overflow="hidden"
                    ),
                    rx.link(
                        rx.icon("globe"),
                        href=info["url"]
                    ),
                    
                    rx.hstack(
                        rx.cond(
                            State.int(info, 1),
                            rx.icon("star"),
                            rx.icon("star", color="gray"),
                        ),
                        rx.cond(
                            State.int(info, 2),
                            rx.icon("star"),
                            rx.icon("star", color="gray"),
                        ),
                        rx.cond(
                            State.int(info, 3),
                            rx.icon("star"),
                            rx.icon("star", color="gray"),
                        ),
                        rx.cond(
                            State.int(info, 4),
                            rx.icon("star"),
                            rx.icon("star", color="gray"),
                        ),
                        rx.cond(
                            State.int(info, 5),
                            rx.icon("star"),
                            rx.icon("star", color="gray"),
                        ),
                        rx.text(info['aggregated_rating_count'], color_scheme="gray")
                    ),
                )
            )
            
        )
    )
    