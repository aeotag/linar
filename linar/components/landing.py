import reflex as rx

from rxconfig import config



def landing_page(login_url) -> rx.Component:
    return rx.flex(
        rx.desktop_only(
            rx.flex(
                rx.box(
                    rx.flex(
                        rx.box(
                            rx.text(
                                "Lunar Bot Dashboard",
                                as_="div",
                                style={
                                    "font-size": "6.5em",
                                }
                            ),
                            rx.text(
                                "illuminating the path to your dreams.",
                                as_="div",
                                color_scheme="cyan",
                                weight="bold",
                                style={
                                    "font-size": "4em",
                                    "color": "transparent",
                                    "-webkit-text-stroke": ".7px var(--main-color)",
                                }
                            ),
                            rx.text(
                                """Lunar is a Discord Bot that can be used for any purpose.
                                Temporary channels, ticket system, welcome messages, rule assignments, role management and much more.
                                It supports multiple languages ​​and is easy to setup / configure.
                                """,
                                as_="p",
                                width="85%",
                                padding="2.5em 0 1.1em",
                                style={
                                    "font-size": "1.7em",
                                }
                            ),
                            rx.button(
                                rx.text(
                                    "Login",
                                    style={
                                    "font-size": "1.4em",
                                }
                                ),
                                size="4",
                                variant="outline",
                                color_scheme="cyan",
                                radius="medium",
                                width="11em",
                                height="4em",
                                on_click=rx.redirect(login_url),
                            ),
                        ),
                    direction="column",
                    align="center",
                    justify="center",
                    width="100%",
                    ),
                width="100%",
                ),
                rx.box(
                    rx.flex(
                        rx.image(
                            src="Lunar.png",
                            height="auto",
                            width="65%",
                        ),
                    direction="column",
                    align="center",
                    justify="center",
                    width="100%",
                    ),
                width="100%",
                ),
            spacing="4",
            padding="4em",
            width="100%",
            height="100%",
            direction="row",
            align="center",
            justify="center",
            )
        ),
        rx.mobile_and_tablet(
            rx.flex(
                rx.box(
                    rx.flex(
                        rx.image(
                            src="Lunar.png",
                            height="auto",
                            width="65%",
                        ),
                    direction="column",
                    align="center",
                    justify="center",
                    width="100%",
                    ),
                width="100%",
                ),
                rx.box(
                    rx.flex(
                        rx.box(
                            rx.text(
                                "Lunar Bot Dashboard",
                                as_="div",
                                padding="0.4em 1.1em 0",
                                style={
                                    "font-size": "2.7em",
                                }
                            ),
                            rx.text(
                                "illuminating the path to your dreams.",
                                as_="div",
                                color_scheme="cyan",
                                weight="bold",
                                padding="0.4em 1.1em",
                                style={
                                    "font-size": "2.4em",
                                    "color": "transparent",
                                    "-webkit-text-stroke": ".7px var(--main-color)",
                                }
                            ),
                            rx.text(
                                """Lunar is a Discord Bot that can be used for any purpose.
                                Temporary channels, ticket system, welcome messages, rule assignments, role management and much more.
                                It supports multiple languages ​​and is easy to setup / configure.
                                """,
                                as_="p",
                                padding="2.5em 1.1em",
                                style={
                                    "font-size": "1.4em",
                                }
                            ),
                            rx.button(
                                rx.text(
                                    "Login",
                                    style={
                                    "font-size": "1.1em",
                                }
                                ),
                                size="4",
                                variant="outline",
                                color_scheme="cyan",
                                radius="medium",
                                width="10em",
                                height="3.7em",
                            ),
                        ),
                    direction="column",
                    align="center",
                    justify="center",
                    text_align="center",
                    width="100%",
                    ),
                width="100%",
                ),
            spacing="4",
            #padding="4em",
            width="100%",
            height="100%",
            direction="column",
            align="center",
            justify="center",
            ),
        )
    )