import reflex as rx

from rxconfig import config



def guilds_component() -> rx.Component:
    
    return rx.vstack(
        rx.desktop_only(
            rx.flex(
                rx.box(
                    rx.text(
                        "Discord Server",
                        as_="div",
                        align="center",
                        style={
                            "font-size": "6.5em",
                        }
                    ),
                ),
                rx.divider(),
                rx.box(
                    rx.flex(
                        rx.card(
                            rx.flex(
                                rx.box(
                                    rx.image(
                                        src="/Lunar.png",
                                        width="100%",
                                        height="auto",
                                        border_radius="11%",
                                    ),
                                    width="40%",
                                ),
                                rx.flex(
                                    rx.box(
                                        rx.text(
                                            "Server Name",
                                            style={
                                                "font-size": "2.4em",
                                            }
                                        ),
                                    ),
                                    rx.box(
                                        rx.text(
                                            "Deine Rolle",
                                            style={
                                                "font-size": "1.7em",
                                            }
                                        ),
                                    ),
                                    rx.spacer(),
                                    rx.box(
                                        rx.flex(
                                            rx.button(
                                                "Invite",
                                                size="4",
                                                variant="outline",
                                                color_scheme="pink",
                                                radius="medium",
                                            ),
                                            rx.button(
                                                "Configure Server",
                                                size="4",
                                                variant="outline",
                                                color_scheme="cyan",
                                                radius="medium",
                                            ),
                                            spacing="4",
                                            justify="end",
                                            width="100%",
                                        ),
                                    ),
                                    direction="column",
                                    padding="0 0 0 2.4em",
                                    justify="center",
                                    width="100%",
                                ),
                            ),
                            width="33%"
                        ),
                        width="100%",
                        spacing="4",
                        direction="row",
                    ),
                    padding="4em 0 0 0",
                ),
                width="100%",
                justify="center",
                direction="column",
                padding="0 4em 0",
            ),
        ),
        rx.mobile_and_tablet(
            rx.text("Guilds"),
        ),
    )