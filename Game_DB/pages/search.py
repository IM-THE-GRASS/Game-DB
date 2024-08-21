import reflex as rx
from Game_DB.state import State
from Game_DB.components.keybind import Keybind
def card(info):
    return rx.vstack(
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
    )
@rx.page(on_load=State.get_search_results)
def search() -> rx.Component:
    return rx.box(
        rx.text(State.search_resultss),
        Keybind(
            
            keys=["Enter"],
            bind=lambda key:State.submit_search2(),
        ),
        rx.moment(
            on_change=State.print,
            interval=100  
        ),
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
                on_click=State.submit_search2
                
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
                State.search_results,
                card  
            ),
            position="absolute",
            left="3vw",
            top="27vh",
            columns="7",
            spacing="8",
            width="90%"
        )
    )
