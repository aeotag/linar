import reflex as rx
import os

from dotenv import load_dotenv
from rxconfig import config


from ..components import navbar_icons as navbar
from ..components import footer_component, landing_page
load_dotenv()



@rx.page(route="/", title="Linar Dashboard")
def index() -> rx.Component:
    # Landing Page (Index)
    return rx.vstack(
        navbar(),
        landing_page(os.getenv("LOGIN_URL")),
        footer_component(),
    )