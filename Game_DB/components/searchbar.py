import reflex as rx
from Game_DB.state import State
def search_bar(on_submit= State.submit_search2, on_focus=State.on_search_focus, on_blur = State.on_search_unfocus):
    return rx.hstack(
        rx.cond(
            State.search_disabled,
            rx.input(
                font_size="6.5vh",
                height="11.2vh",
                width="100%",
                value="You can't use both search and sort!",
                on_change=State.on_search_change,
                disabled=State.search_disabled
            ),
            rx.input(
                font_size="6.5vh",
                height="11.2vh",
                width="100%",
                value=State.search_value,
                on_change=State.on_search_change,
                disabled=State.search_disabled
            ),
            
        ),
        
        rx.center(
            
            rx.icon(
                "search",
                size=83
            ) ,
            width="11.2vh",
            height="100%",
            padding="1vh",
            on_click=on_submit
            
        ),
        left="35vw",
        top="4vh",
        position="absolute",
        border="0.109vh solid #CEC8D4",
        height="11.2vh",
        width="63vw",
        border_radius="8px",
        on_blur=on_blur,
        on_focus=on_focus
    ),