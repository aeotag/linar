import reflex as rx
import os

from dotenv import load_dotenv
from rxconfig import config


from ..components import navbar_icons as navbar
from ..components import footer_component, guilds_component
load_dotenv()



@rx.page(route="/guilds", title="Linar Dashboard")
def guilds() -> rx.Component:

    return rx.vstack(
        navbar(),
        guilds_component(),
        footer_component(),
    )