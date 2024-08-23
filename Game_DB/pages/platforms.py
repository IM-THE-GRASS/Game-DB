import reflex as rx
from Game_DB.state import State
from Game_DB.components.keybind import Keybind
from Game_DB.components.select import select
from Game_DB.components.card import card
from Game_DB.components.searchbar import search_bar
from reflex_lottiefiles import LottieFiles



@rx.page()
def platforms() -> rx.Component:
    return rx.box(
        Keybind(
            
            keys=["Enter"],
            bind=lambda key:State.on_platform_submit(),
        ),
        rx.moment(
            on_change=State.on_update,
            interval=100,
            opacity="0"  
        ),
        search_bar(on_submit=State.on_platform_submit),
        rx.hstack(
            select(
                options = State.platform_sort_options,      
                onChange=State.platform_set_sort,
                width="20vw",
                isSearchable=True,
                isClearable=True,
                placeholder = "Sort"
            ),
            select(
                options = State.platform_sort_for_options,          
                onChange=State.platform_set_sort_for,
                width="20vw",
                isSearchable=True,
                isClearable=True,
                isDisabled=State.sort_for_disabled,
                placeholder="Sort for"
                
            ),
            position="absolute",
            left="3vw",
            top="17vh",
            width="90vw",
            height="7.4vh",
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
        
        
        rx.box(
            rx.cond(
                State.search_results_loading,
                rx.center(
                    rx.vstack(
                        rx.heading("Loading, please wait"),
                        LottieFiles(
                            src="https://lottie.host/5ff06a80-3f45-4dd3-8737-f4cf62ba3d48/X5hdVEjbNK.lottie",
                            autoplay=True,
                            loop=True,
                            width="20vw",
                            height="20vw",
                        )
                    ),
                    
                    width="100%",
                    height="90vh"
                    
                )
            ),
            
            position="absolute",
            left="3vw",
            top="27vh",
            width="90%"
        ),
        rx.grid(
            rx.foreach(
                State.platforms_search_results,
                lambda info :card(info, bg="#000000")  
            ),
            
            position="absolute",
            left="3vw",
            top="27vh",
            columns="7",
            spacing="8",
            width="90%",
        ),
        overflow="hidden"
    )
