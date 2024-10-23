"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import os

from dotenv import load_dotenv
from typing import Optional
from rxconfig import config

from .pages import *

from .essentials import DiscordAuth

load_dotenv()
api = DiscordAuth(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), os.getenv("REDIRECT_URI"), os.getenv("API_ENDPOINT"))


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

app = rx.App(
    style=style,
    )