import reflex as rx
class slider(rx.Component):
    library = "nuka-carousel"
    tag = "Carousel"
    autoplay:rx.Var[bool]
    showDots:rx.Var[bool]
    wrapMode:rx.Var[str]
    autoplayInterval:rx.Var[int]
    scrollDistance:rx.Var[str]
Slider = slider.create