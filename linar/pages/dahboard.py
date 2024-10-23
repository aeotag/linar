import reflex as rx
import os

from dotenv import load_dotenv
from rxconfig import config

load_dotenv()



class State(rx.State):
    """The app state."""

    ...


@rx.page(route="/dahboard", title="Linar Dashboard")
def guilds() -> rx.Component:

    return rx.vstack(
        rx.text("Hello Dashboard")
    )