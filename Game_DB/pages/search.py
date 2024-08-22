import reflex as rx
from Game_DB.state import State
from Game_DB.components.keybind import Keybind

class Select(rx.Component):
    library = "react-select"
    tag = "Select"
    is_default = True
    options:rx.Var[list[dict[str, str]]]
    isClearable:rx.Var[bool]
    isDisabled:rx.Var[bool]
    isLoading:rx.Var[bool]
    isSearchable:rx.Var[bool]
    onChange: rx.EventHandler[lambda newValue: [newValue]]
    unstyled:rx.Var[bool]
    placeholder:rx.Var[str]
from reflex_lottiefiles import LottieFiles

def loading():
    return rx.center(
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
        
    ),

select = Select.create
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
        border_radius="8px"
    )
@rx.page(on_load=State.on_load)
def search() -> rx.Component:
    return rx.box(
        Keybind(
            
            keys=["Enter"],
            bind=lambda key:State.submit_search2(),
        ),
        rx.moment(
            on_change=State.on_update,
            interval=100,
            opacity="0"  
        ),
        rx.hstack(
            select(
                options = State.sort_options,      
                onChange=State.set_sort,
                width="100%",
                isSearchable=False,
                isClearable=True,
                placeholder = "Search by"
            ),
            select(
                options = State.sort_for_options,          
                onChange=State.set_sort_for,
                width="100%",
                isSearchable=False,
                isClearable=True,
                isDisabled=State.sort_for_disabled,
                placeholder="Sort for"
                
            ),
            position="absolute",
            left="3vw",
            top="17vh",
            width="40vw",
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
        
        rx.hstack(
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
                on_click=State.submit_search2
                
            ),
            left="35vw",
            top="4vh",
            position="absolute",
            border="0.109vh solid #CEC8D4",
            height="11.2vh",
            width="63vw",
            border_radius="8px",
            on_blur=State.on_search_unfocus,
            on_focus=State.on_search_focus
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
