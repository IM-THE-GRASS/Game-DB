import reflex as rx
from Game_DB.components.carousel import Slider
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
                        Slider(
                            rx.image(
                                src=info["img"],
                                height="30vh",
                                width="25vw",
                                object_fit="contain"
                            ),
                            rx.image(
                                src=info["img"],
                                width="25vw",
                                height="30vh",
                                
                                object_fit="contain"
                            ),
                            rx.image(
                                src=info["img"],
                                width="25vw",
                                height="30vh",
                                object_fit="contain"
                            ),
                            rx.image(
                                src=info["img"],
                                width="25vw",
                                height="30vh",
                                object_fit="contain"
                            ),
                            rx.image(
                                src=info["img"],
                                width="25vw",
                                height="30vh",
                                object_fit="contain"
                            ),
                            rx.image(
                                src=info["img"],
                                width="25vw",
                                height="30vh",
                                object_fit="contain"
                            ),
                            width="20vw",
                            showDots=True
                        ),
                        height="30vh"
                    ),
                    rx.hstack(
                        rx.icon("globe"),
                        rx.text("Site")
                    ),
                    rx.hstack(
                        rx.icon("star"),
                        rx.icon("star"),
                        rx.icon("star"),
                        rx.icon("star", color="gray"),
                        rx.icon("star", color="gray"),
                        rx.text("(100)", color_scheme="gray")
                    ),
                    rx.dialog.description(info["summary"]),
                )
            )
            
        )
    )
    