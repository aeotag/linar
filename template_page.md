import reflex as rx

from rxconfig import config

class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Landing Page (Index)
    return rx.vstack(

    )

style = {
    "--bg-color": "#081b29",
    "--second-bg-color": "#112e42",
    "--third-bg-color": "#0a0b18",
    "--fourth-bg-color": "#212339",
    "--text-color": "#ededed",
    "--main-color": "#00abf0",

    "font_family": "Nunito",
    "background_color": "#081b29",
}

app = rx.App(style=style)
app.add_page(index)