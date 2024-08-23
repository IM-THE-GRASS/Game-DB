import reflex as rx
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