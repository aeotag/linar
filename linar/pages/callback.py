import reflex as rx
import os

from dotenv import load_dotenv
from rxconfig import config

load_dotenv()



class State(rx.State):
    """The app state."""

    @rx.var
    def get_code(self):
        code = self.router.page.params.get("code")
        if code == "":
            print("error")

        return code 


@rx.page(route="/callback", title="Linar Dashboard")
def callback():

    data = {
            "client_id": os.getenv("CLIENT_ID"),
            "client_secret": os.getenv("CLIENT_SECRET"),
            "grant_type": "authorization_code",
            "code": State.get_code,
            "redirect_uri": os.getenv("REDIRECT_URI"),
        }

    return rx.vstack(
        rx.text(data),
    )