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
@rx.page(on_load=State.get_search_results)
def search() -> rx.Component:
    return rx.box(
        Keybind(
            
            keys=["Enter"],
            bind=lambda key:State.submit_search2(),
        ),
        rx.moment(
            on_change=State.print,
            interval=100,
            opacity="0"  
        ),
        rx.hstack(
            select(
                options = [
                    {
                        "value":"first_release_date",
                        "label":"Release date"
                    },
                ],            
                onChange=State.set_sort,
                width="100%",
                isSearchable=False,
                isClearable=True,
                placeholder = "Sort for"
            ),
            select(
                options = [
                    {
                        "value":"asc",
                        "label":"Ascending"
                    },
                    {
                        "value":"desc",
                        "label":"Decending"
                    }
                ],            
                onChange=State.set_sort_order,
                width="100%",
                isSearchable=False,
                isClearable=True,
                placeholder="Sort order"
                
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
