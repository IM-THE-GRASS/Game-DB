import reflex as rx

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